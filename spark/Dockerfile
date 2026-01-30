FROM apache/spark:3.5.1

USER root

# Instalar curl e wget 
RUN apt-get update && apt-get install -y curl wget

# Criar diretório temporário
WORKDIR /tmp

# Baixar JARs do Kafka usando wget
RUN wget -q https://repo1.maven.org/maven2/org/apache/spark/spark-sql-kafka-0-10_2.12/3.5.1/spark-sql-kafka-0-10_2.12-3.5.1.jar && \
    wget -q https://repo1.maven.org/maven2/org/apache/kafka/kafka-clients/3.6.0/kafka-clients-3.6.0.jar && \
    wget -q https://repo1.maven.org/maven2/org/apache/spark/spark-token-provider-kafka-0-10_2.12/3.5.1/spark-token-provider-kafka-0-10_2.12-3.5.1.jar && \
    wget -q https://repo1.maven.org/maven2/org/apache/commons/commons-pool2/2.11.1/commons-pool2-2.11.1.jar

# Mover JARs para o diretório correto
RUN mv spark-sql-kafka-0-10_2.12-3.5.1.jar \
       kafka-clients-3.6.0.jar \
       spark-token-provider-kafka-0-10_2.12-3.5.1.jar \
       commons-pool2-2.11.1.jar \
       /opt/spark/jars/

# Limpeza
RUN rm -rf /tmp/*

USER spark

WORKDIR /opt/spark/work-dir