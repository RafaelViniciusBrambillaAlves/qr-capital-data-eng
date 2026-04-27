# 🚀 Desafio Data Engineer – Streaming de Bitcoin (Kraken)

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Kafka](https://img.shields.io/badge/Kafka-000000?style=for-the-badge&logo=apachekafka&logoColor=white)
![Spark](https://img.shields.io/badge/Apache_Spark-FDEE21?style=for-the-badge&logo=apachespark&logoColor=black)
![Airflow](https://img.shields.io/badge/Airflow-017CEE?style=for-the-badge&logo=apacheairflow&logoColor=white)
![Parquet](https://img.shields.io/badge/Parquet-50ABF1?style=for-the-badge&logo=apachearrow&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Streaming](https://img.shields.io/badge/Real_Time-Streaming-FF6F00?style=for-the-badge)

---

## 📌 Visão Geral
Este projeto foi desenvolvido com base no **Desafio Data Engineer da QR Capital**, disponível em: ([repositório oficial do desafio](https://github.com/qrcapital/desafios/blob/main/desafio-data-eng.md)) 



Este projeto implementa um **pipeline de streaming de dados em tempo real** para coletar cotações de Bitcoin da exchange **Kraken**, processar os eventos via **Apache Kafka** e **Apache Spark Structured Streaming**, e armazenar os dados de forma **particionada e otimizada em formato Parquet**, com **orquestração via Apache Airflow**, tudo executando em ambiente **Docker**.

O objetivo vai além do requisito mínimo do desafio, aplicando **boas práticas de engenharia de dados**, organização de código, escalabilidade e observabilidade.

---

## 🧠 Entendimento do Desafio Original

### Desafio Proposto
- Consumir dados em tempo real da API da Kraken
- Utilizar uma plataforma de streaming (Kafka ou Flink)
- Persistir os dados em arquivos `.csv`
- Utilizar Docker
- (Opcional) Orquestrar com Airflow

### Domínio do Problema
Criar um stream de dados que coleta preço do Bitcoin em tempo real e registra os dados em arquivos estruturados.

---

## 🔄 Principais Evoluções em Relação ao Desafio

### ❌ CSV → ✅ Parquet
Embora o desafio solicite arquivos CSV, optamos por **Parquet**, pois:

- É um **formato colunar**, ideal para analytics
- Melhor **compressão **
- Melhor performance em leitura
- Padrão amplamente utilizado em **Data Lakes**
- Compatível com Spark, Athena, BigQuery, etc.

> 💡 Em cenários reais de Engenharia de Dados, CSV é geralmente evitado para grandes volumes e dados históricos.

---

### 📂 Estrutura de Dados Particionada
Os dados são organizados seguindo boas práticas de Data Lake:

```text
data/
└── KRAKEN/
    └── year=2026/
        └── month=1/
            └── day=30/
                └── hour=18/
                    └── symbol=BTC_USD/
                        └── part-*.parquet
```

Isso permite:
- Queries mais rápidas
- Leitura seletiva por período
- Facilidade de integração com ferramentas analíticas

---

## 🏗 Arquitetura da Solução

```text
Kraken API
   │
   ▼
Kafka Producer (Python)
   │
   ▼
Apache Kafka (Topic: kraken.trades)
   │
   ▼
Apache Spark Structured Streaming
   │
   ▼
Parquet (Data Lake)
   │
   ▼
Orquestração via Apache Airflow

```
---

## 🗂 Estrutura do Projeto

```
.
├── airflow/
│   ├── dags/
│   │   └── kraken_spark_parquet_dag.py
│   └── logs/
│
├── data/
│   └── KRAKEN/
│       └── year=YYYY/month=MM/day=DD/hour=HH/symbol=BTC_USD
│
├── kafka/
│   └── producer/
│       ├── app/
│       │   ├── config.py
│       │   ├── kafka_producer.py
│       │   ├── kraken_client.py
│       │   ├── models.py
│       │   └── service.py
│       ├── Dockerfile
│       └── requirements.txt
│
├── spark/
│   ├── jobs/
│   │   └── kraken_to_parquet/
│   │       ├── config.py
│   │       ├── main.py
│   │       ├── reader.py
│   │       ├── schema.py
│   │       ├── transformer.py
│   │       └── writer.py
│   └── Dockerfile
│
├── docker-compose.yml
└── README.md
```

---

## 🧰 Tecnologias Utilizadas
Python 3.10

Apache Kafka

Apache Spark 3.5 (Structured Streaming)

Apache Airflow 2.8

Docker & Docker Compose

Parquet + Snappy

Kraken API

---
## ⚙️ Variáveis de Ambiente

Crie um arquivo .env na raiz do projeto:

```env
# Kraken
KRAKEN_API_URL=https://api.kraken.com
KRAKEN_PAIR=BTC/USD
POLL_INTERVAL_SECONDS=5

# Kafka
KAFKA_BOOTSTRAP_SERVERS=kafka:9092
KAFKA_TOPIC=kraken.trades

# Spark
SPARK_APP_NAME=KrakenKafkaToPARQUET
BASE_OUTPUT_PATH=/data
EXCHANGE=KRAKEN
SYMBOL=BTC_USD
```
---

## ▶️ Como Rodar o Projeto
1️⃣ Subir os serviços
```
docker-compose up -d --build
```

2️⃣ Kafka Producer

O producer inicia automaticamente e começa a publicar trades no Kafka.

Logs:
```
docker logs -f kafka-producer
```

3️⃣ Spark Streaming (manual)
```
docker exec -it spark-master \
/opt/spark/bin/spark-submit \
--master spark://spark-master:7077 \
--packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.1 \
/opt/spark/jobs/kraken_to_parquet/main.py
```

4️⃣ Spark UI

Acesse:
```
http://localhost:4040
```

---

## ⏱ Orquestração com Airflow
Acessar o Airflow

```
http://localhost:8080
```


```
Usuário: admin
Senha: admin
```

DAG Disponível

kraken_spark_streaming

Essa DAG:

Verifica serviços

Executa o Spark Streaming

Monitora o job

---

## 🧪 Organização e Qualidade

Código modular e desacoplado

Separação clara de responsabilidades

Configurações centralizadas

Docker como padrão de execução

Formato de dados pronto para analytics

---

## ✅ Critérios de Avaliação Atendidos

✔ Organização do projeto

✔ Clareza no README

✔ Uso de streaming real

✔ Boas práticas de engenharia de dados

✔ Orquestração com Airflow

✔ Código legível e extensível

---

## 📄 Licença

Este projeto está sob a licença **MIT**. Sinta-se livre para usar, estudar e adaptar.

---

👨‍💻 Desenvolvido para fins de estudo e evolução técnica.