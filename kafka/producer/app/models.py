from dataclasses import dataclass

@dataclass
class Trade:
    pair: str
    price: float
    volume: float
    timestamp_ms: int
    side: str
    order_type: str
    misc: str
    source: str = "kraken"