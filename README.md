docker exec -it kafka kafka-topics --bootstrap-server kafka:9092 --list

docker exec -it kafka kafka-console-consumer --bootstrap-server kafka:9092 --topic kraken.trades --from-beginning

docker exec -it kafka kafka-topics --bootstrap-server kafka:9092 --describe --topic kraken.trades

docker exec -it kafka kafka-run-class kafka.tools.GetOffsetShell --broker-list kafka:9092 --topic kraken.trades


docker exec -it kafka kafka-run-class kafka.tools.GetOffsetShell --broker-list kafka:9092 --topic kraken.trades

{"pair": "XXBTZUSD", "price": "89795.50000", "volume": "0.00022052", "timestamp": 1769624687.8442967, "side": "b", "order_type": "l", "misc": "", "source": "kraken"}