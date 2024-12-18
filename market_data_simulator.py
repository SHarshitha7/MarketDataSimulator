from confluent_kafka import Producer
import json
import time
import random
from datetime import datetime

# Kafka configuration
KAFKA_TOPIC = "equity_market_data"
KAFKA_BOOTSTRAP_SERVERS = "pkc-w77k7w.centralus.azure.confluent.cloud:9092"
KAFKA_USERNAME = "BHGH5GP6T5ERDQLI"
KAFKA_PASSWORD = "D40AFZISgQBVgbFh617ZBMOSkGw0FU77GFr3HBsHLbqAkXJqvl+b/LSEMfP/wXl1"

# Kafka producer configuration
producer = Producer({
    'bootstrap.servers': KAFKA_BOOTSTRAP_SERVERS,
    'security.protocol': 'SASL_SSL',
    'sasl.mechanisms': 'PLAIN',
    'sasl.username': KAFKA_USERNAME,
    'sasl.password': KAFKA_PASSWORD
})

def simulate_market_data():
    tickers = ["AAPL", "GOOG", "AMZN", "MSFT"]
    while True:
        data = {
            "ticker": random.choice(tickers),
            "bid_price": round(random.uniform(100, 1500), 2),
            "ask_price": round(random.uniform(100, 1500), 2),
            "last_trade_price": round(random.uniform(100, 1500), 2),
            "volume": random.randint(100, 10000),
            "timestamp": datetime.utcnow().isoformat()
        }
        print("Publishing:", data)
        producer.produce(KAFKA_TOPIC, value=json.dumps(data))
        producer.flush()  # Ensure message is sent immediately
        time.sleep(2)  # Simulate delay

if __name__ == "__main__":
    simulate_market_data()
