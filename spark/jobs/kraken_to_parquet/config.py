import os

class Settings:
    def __init__(self):
        self.kafka_bootstrap_servers = self._get("KAFKA_BOOTSTRAP_SERVERS")
        self.kafka_topic = self._get("KAFKA_TOPIC")

        self.base_output_path = self._get("BASE_OUTPUT_PATH")
        self.exchange = self._get("EXCHANGE")
        self.symbol = self._get("SYMBOL")

        self.spark_app_name = self._get("SPARK_APP_NAME")

    @staticmethod
    def _get(key: str) -> str:
        value = os.getenv(key)
        if not value:
            raise RuntimeError(f"Missing required env var: {key}")
        return value

settings = Settings()
