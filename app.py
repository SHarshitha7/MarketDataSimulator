import json
import random
from datetime import datetime, timezone
from kafka import KafkaProducer

# Kafka Configuration
KAFKA_TOPIC = "equity_market_data"
KAFKA_SERVER = ["pkc-w77k7w.centralus.azure.confluent.cloud:9092"]
KAFKA_USERNAME = "BHGH5GP6T5ERDQLI"
KAFKA_PASSWORD = "D40AFZISgQBVgbFh617ZBMOSkGw0FU77GFr3HBsHLbqAkXJqvl+b/LSEMfP/wXl1"

# Initialize Kafka Producer
producer = KafkaProducer(
    bootstrap_servers=KAFKA_SERVER,
    security_protocol="SASL_SSL",
    sasl_mechanism="PLAIN",
    sasl_plain_username=KAFKA_USERNAME,
    sasl_plain_password=KAFKA_PASSWORD,
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
    request_timeout_ms=60000,  # Increase request timeout
    metadata_max_age_ms=300000  # Increase metadata max age
)

# Function to generate simulated market data
def generate_market_data():
    tickers = ["AAPL", "GOOG", "MSFT", "TSLA", "AMZN"]
    ticker = random.choice(tickers)
    bid_price = round(random.uniform(100, 1500), 2)
    ask_price = round(bid_price + random.uniform(1, 10), 2)
    last_trade_price = round(random.uniform(bid_price, ask_price), 2)
    volume = random.randint(100, 10000)
    timestamp = datetime.now(timezone.utc).isoformat()

    return {
        "ticker": ticker,
        "bid_price": bid_price,
        "ask_price": ask_price,
        "last_trade_price": last_trade_price,
        "volume": volume,
        "timestamp": timestamp
    }

# Publish simulated data to Kafka
def publish_data():
    try:
        while True:
            market_data = generate_market_data()
            producer.send(KAFKA_TOPIC, market_data)
            print(f"Published: {market_data}")
    except KeyboardInterrupt:
        print("Market data simulation stopped.")
    finally:
        producer.close()

if __name__ == "__main__":
    publish_data()