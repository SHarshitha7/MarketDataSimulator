## Market Data Simulator - Kafka Producer
##  Overview
This project simulates market data for stocks and publishes the data to a Kafka topic. The data includes the stock ticker, bid price, ask price, last trade price, trading volume, and a timestamp. The producer sends this simulated data to the Kafka topic equity_market_data every 2 seconds.

## Prerequisites
Python 3.x
Kafka (Apache Kafka or Confluent Kafka)
Confluent Kafka Python library (confluent-kafka)
## Installation
1. Install Python Dependencies
Before running the producer script, make sure you have installed the required Python libraries.

bash
Copy code
pip install confluent-kafka
2. Kafka Setup
Ensure your Kafka broker is running and accessible. You need to configure the following Kafka parameters:

KAFKA_BOOTSTRAP_SERVERS: The Kafka cluster you want to connect to.
KAFKA_USERNAME and KAFKA_PASSWORD: Your Kafka authentication credentials.
KAFKA_TOPIC: The Kafka topic to which the market data will be published (equity_market_data).
If you do not have a running Kafka cluster, you can set up one on platforms like Confluent Cloud, or use an on-premise Kafka cluster.

## Configuration
You need to configure the Kafka connection parameters in the script. These are already set in the script, but you should check and modify them as necessary:

python
Copy code
KAFKA_TOPIC = "equity_market_data"
KAFKA_BOOTSTRAP_SERVERS = "pkc-w77k7w.centralus.azure.confluent.cloud:9092"
KAFKA_USERNAME = "YOUR_KAFKA_USERNAME"
KAFKA_PASSWORD = "YOUR_KAFKA_PASSWORD"
KAFKA_TOPIC: The Kafka topic where the market data will be sent.
KAFKA_BOOTSTRAP_SERVERS: The address of your Kafka broker.
KAFKA_USERNAME: Your Kafka username for authentication.
KAFKA_PASSWORD: Your Kafka password for authentication.
## Running the Market Data Simulator
1. Run the Producer
To start the producer and begin simulating market data, simply run the Python script:

bash
Copy code
python market_data_simulator.py
This will start simulating market data for the following tickers: AAPL, GOOG, AMZN, MSFT. The script will continuously generate random bid, ask, and trade prices along with volumes and timestamps every 2 seconds, and publish them to the Kafka topic equity_market_data.

2. Kafka Topic
Ensure that the topic equity_market_data exists in your Kafka broker. If the topic does not exist, you can either create it manually or let Kafka create it automatically.

If you are using the Kafka command line tools, you can create the topic with:

bash
Copy code
kafka-topics.sh --create --topic equity_market_data --bootstrap-server <your-kafka-bootstrap-server> --partitions 1 --replication-factor 1
## Example of Simulated Data
The market data being sent to the Kafka topic will look like this:

json
Copy code
{
  "ticker": "AAPL",
  "bid_price": 1200.56,
  "ask_price": 1201.25,
  "last_trade_price": 1200.99,
  "volume": 2000,
  "timestamp": "2024-12-18T14:30:00Z"
}
## Troubleshooting
Kafka Connection Errors: Ensure that your Kafka connection details (username, password, bootstrap server) are correct.
Topic Not Found: If Kafka cannot find the topic, make sure the equity_market_data topic exists in your Kafka broker.
## License
This project is licensed under the MIT License - see the LICENSE file for details.