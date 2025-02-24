#1.load the data from kaggle
import pandas as pd
# Load the dataset (assuming it's in CSV format)
df1 = pd.read_csv('/home/amitha/Downloads/e-commerce_datasets/List of Orders.csv')  # Replace with your dataset path
df2 = pd.read_csv('/home/amitha/Downloads/e-commerce_datasets/Order Details.csv')
df3 = pd.read_csv('/home/amitha/Downloads/e-commerce_datasets/Sales target.csv')

# Check the first few rows of the dataset
# print(df1.head())
# print(df2.head())
# print(df3.head())

# Combine the datasets by concatenating vertically (if they have the same columns)
combined_df = pd.concat([df1, df2, df3], ignore_index=True)
# Optionally, print the combined DataFrame to check
# print(combined_df.head())

# Merge the datasets (assuming they have common columns to merge on)
merged_df = pd.merge(df1, df2, on='Order ID', how='outer')
merged_df = pd.merge(merged_df, df3, on='Category', how='outer')

# Save the combined DataFrame (concatenated version) to a CSV file
combined_df.to_csv('/home/amitha/Downloads/e-commerce_datasets/combined_file.csv', index=False)

# Optionally, save the merged DataFrame to a CSV file
merged_df.to_csv('/home/amitha/Downloads/e-commerce_datasets/merged_file.csv', index=False)
print(merged_df.head())

#2.data inspection and cleaning

# Check basic info of the dataset (e.g., data types, non-null counts)
print(merged_df.info())

# Check summary statistics for numerical columns
print(merged_df.describe())

# Check for null or missing values in the dataset
print(merged_df .isnull().sum())

#3.data visualization

import matplotlib.pyplot as plt
import seaborn as sns

# Example: Plot a bar chart for a categorical column
sns.countplot(data=merged_df, x='Category')
plt.show()

# merged_df['Sales'].hist(bins=20)  # Plot a histogram of the 'Sales' column
# plt.show()

from confluent_kafka import Consumer, KafkaError

# Kafka consumer configuration
consumer_config = {
    'bootstrap.servers': 'localhost:9092',  # Change with your Kafka server address
    'group.id': 'order-consumer-group',
    'auto.offset.reset': 'earliest'  # Start from the earliest message
}

# Create the consumer
consumer = Consumer(consumer_config)

# Subscribe to the topic
consumer.subscribe(['orders_topic'])  # Change with your Kafka topic name

# Consume messages in a loop
while True:
    msg = consumer.poll(timeout=1.0)  # Poll for new messages
    if msg is None:
        continue
    if msg.error():
        if msg.error().code() == KafkaError._PARTITION_EOF:
            continue
        else:
            print(msg.error())
    else:
        # Process the message
        print(f"Received order: {msg.value().decode('utf-8')}")
        # You can parse and store it here

consumer.close()





