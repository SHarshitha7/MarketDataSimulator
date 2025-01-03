import json
from kafka import KafkaProducer
import time
import random
from datetime import datetime, timezone
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("MarketDataSimulator")

# Kafka configuration
KAFKA_TOPIC = "stock_orders"
KAFKA_BOOTSTRAP_SERVERS = "localhost:9092"

# Kafka producer configuration
producer = KafkaProducer(
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
)

def delivery_report(err, msg):
    """
    Delivery report callback to confirm message delivery or log any errors.
    """
    if err is not None:
        logger.error(f"Message delivery failed: {err}")
    else:
        logger.info(f"Message delivered to {msg.topic()} [partition={msg.partition()} offset={msg.offset()}]")

def simulate_market_data():
    """
    Simulates equity market data and publishes it to a Kafka topic.
    """
    tickers = ["AAPL", "GOOG", "AMZN", "MSFT", "NFLX"]
    try:
        while True:
            # Generate simulated data
            data = {
                "ticker": random.choice(tickers),
                "bid_price": round(random.uniform(100, 1500), 2),
                "ask_price": round(random.uniform(100, 1500), 2),
                "last_trade_price": round(random.uniform(100, 1500), 2),
                "volume": random.randint(100, 10000),
                "timestamp": datetime.now(timezone.utc).isoformat()
            }
            
            # Log data being published
            logger.info(f"Publishing data: {data}")
            
            # Send the message to Kafka
            producer.send(KAFKA_TOPIC, value=data)
            
            # Simulate real-time updates with a delay
            time.sleep(2)
    except KeyboardInterrupt:
        logger.info("Simulation stopped by user.")
    finally:
        logger.info("Flushing remaining messages and shutting down producer.")
        producer.flush()

if __name__ == "__main__":
    simulate_market_data()