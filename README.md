# project2
The code provided is a combination of different steps involving data processing, visualization, and an attempt at consuming messages from a Kafka topic
The script first loads and processes datasets, performs basic data inspection, visualizes data, and includes commented-out code for consuming messages from a Kafka topic. If uncommented, the Kafka consumer code would allow you to listen to a Kafka topic and process new messages (for example, orders being placed in an e-commerce system).
1.The first part of the code is focused on loading CSV data into Pandas DataFrames and combining or merging them.
Steps in this section:
      1.Loading CSV Files
      2.Combining DataFrames
      3.Merging DataFrames 
      4.Displaying Merged Data
2. Data Inspection and Cleaning
3. Data Visualization
4. Kafka Consumer: The last part of the code is for setting up a Kafka consumer to consume messages from a Kafka topic.
    1.Kafka Consumer Configuration
    2.Create the Kafka Consumer
    3.Subscribe to Kafka Topic
    4.Polling for Messages
    5.Error Handling
    6.Graceful Shutdown

Purpose of the Code:

This code seems to be part of a larger pipeline or workflow where:
    Data related to e-commerce orders, details, and sales targets is being loaded and processed.
    After processing and merging the data, basic exploratory data analysis (EDA) is performed (checking for missing values, visualizing the data).
    Finally, a Kafka consumer is used to continuously listen for new order data coming into the orders_topic Kafka topic, and the consumer processes those messages in real-time.


