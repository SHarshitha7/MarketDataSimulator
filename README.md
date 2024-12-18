## Market Data Simulator - Kafka Producer
## Overview
This project simulates stock market data and publishes it to a Kafka topic. It includes market data such as stock tickers, bid price, ask price, last trade price, trading volume, and timestamps. The producer sends this simulated data every 2 seconds to the Kafka topic equity_market_data.

## Installation
``````````````````````````````````````````````````````````````````````````````````
Install Dependencies:


pip install confluent-kafka

Run the Producer:
python market_data_simulator.py

Create Kafka Topic (if not already created):

kafka-topics.sh --create --topic equity_market_data --bootstrap-server <your-kafka-bootstrap-server> --partitions 1 --replication-factor 1

```````````````````````````````````````````````````````````````````````````````````
## Example Data
Sample simulated data published to Kafka:


{
  "ticker": "AAPL",
  "bid_price": 1200.56,
  "ask_price": 1201.25,
  "last_trade_price": 1200.99,
  "volume": 2000,
  "timestamp": "2024-12-18T14:30:00Z"
}
## License
This project is licensed under the MIT License.

