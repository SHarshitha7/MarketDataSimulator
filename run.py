from app import initialize_app

app = initialize_app()
if __name__=='__main__':
    app.run(debug=True) 

'''

from kafka import KafkaProducer
import json
import time
import random
from datetime import datetime
import config

producer = KafkaProducer(
    bootstrap_servers=config.KAFKA_BOOTSTRAP_SERVERS,
    security_protocol=config.KAFKA_SECURITY_PROTOCOL,
    sasl_mechanism=config.KAFKA_SASL_MECHANISM,
    sasl_plain_username=config.KAFKA_SASL_USERNAME,
    sasl_plain_password=config.KAFKA_SASL_PASSWORD,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def generate_market_data():
    tickers = ["AAPL", "GOOG", "MSFT", "AMZN"]
    while True:
        data = {
            "ticker": random.choice(tickers),
            "bid_price": round(random.uniform(100, 500), 2),
            "ask_price": round(random.uniform(100, 500), 2),
            "last_trade_price": round(random.uniform(100, 500), 2),
            "volume": random.randint(1000, 10000),
            "timestamp": datetime.utcnow().isoformat()
        }
        producer.send('equity_market_data', value=data)
        print(f"Produced: {data}")
        time.sleep(1)

if __name__ == "__main__":
    generate_market_data()
    '''