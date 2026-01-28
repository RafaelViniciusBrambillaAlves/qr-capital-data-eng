import requests
from typing import Any, Dict, Optional
from app.config import settings

class KrakenClient:
    def fetch_trades(self, since: Optional[str] = None) -> Dict[str, Any]:
        params = {"pair": settings.kraken_pair}
        if since:
            params["since"] = since

        response = requests.get(
            settings.kraken_api_url, 
            params = params,
            timeout = 10
        )
        response.raise_for_status()
        return response.json()