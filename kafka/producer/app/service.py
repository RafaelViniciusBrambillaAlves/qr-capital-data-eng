import time
import logging
from app.kraken_client import KrakenClient
from app.kafka_producer import create_kafka_producer
from app.config import settings
from app.models import Trade

logging.basicConfig(
    level = logging.INFO,
    format = "%(asctime)s | %(levelname)s | %(message)s"
)

class TradeProducerService:
    def __init__(self):
        self.client = KrakenClient()
        self.producer = create_kafka_producer()
        self.last_since = None

    def run(self):
        while True:
            try:
                self._poll_and_publish()
                time.sleep(settings.poll_interval_seconds)
            except Exception as e:
                logging.exception("Unexpected error in producer loop")
                time.sleep(10)

    def _poll_and_publish(self):
        data = self.client.fetch_trades(self.last_since)
        result = data.get("result", {})

        pair_key = next(k for k in result.keys() if k != "last")
        trades = result.get(pair_key, [])
        self.last_since = result.get("last", self.last_since)

        sent = 0

        for trade in trades:
            trade_obj = Trade(
                pair = settings.kraken_pair,
                price = float(trade[0]),
                volume = float(trade[1]),
                timestamp_ms = int(trade[2] * 1000),
                side = trade[3],
                order_type = trade[4],
                misc = trade[5]
            )

            self.producer.send(
                settings.kafka_topic,
                value = trade_obj.__dict__
            )
            sent += 1

        self.producer.flush()
        logging.info(f"Sent {sent} trades | since={self.last_since}")