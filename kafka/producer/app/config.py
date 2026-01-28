import os
from dotenv import load_dotenv

load_dotenv()

class Settings():
    def __init__(self):
        self.kafka_bootsrap_servers = self._get("KAFKA_BOOTSTRAP_SERVERS") 
        self.kafka_topic = self._get("KAFKA_TOPIC") 
        self.kraken_pair = self._get("KRAKEN_PAIR") 

        self.kraken_api_url = self._get("KRAKEN_API_URL") 
        self.poll_interval_seconds = int(os.getenv("POLL_INTERVAL_SECONDS", 5))

    @staticmethod
    def _get(key: str) -> str:
        value = os.getenv(key)
        if not value:
            raise RuntimeError(f"Missing required env var: {key}")
        return value

settings = Settings()