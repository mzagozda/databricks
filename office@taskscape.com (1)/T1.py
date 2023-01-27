# Databricks notebook source
# MAGIC %md
# MAGIC ## Intro

# COMMAND ----------

# MAGIC %scala
# MAGIC 
# MAGIC Class.forName("org.apache.spark.sql.eventhubs.EventHubsSource")

# COMMAND ----------

eventHubConnectionString = "Endpoint=sb://szkolenie.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=PP6hHYu3EL0Wm6dETcGr6V5CCOW8UktxCfqb1aglCzw=" + ";EntityPath=eventhubszkolenie"

eventHubOptions = { 'eventhubs.connectionString' : sc._jvm.org.apache.spark.eventhubs.EventHubsUtils.encrypt(eventHubConnectionString) }

# COMMAND ----------

input = (spark.readStream.format("eventhubs").options(**eventHubOptions).load())

# COMMAND ----------

input.isStreaming

# COMMAND ----------

streamingMemoryQuery = (input.writeStream.queryName("MemoryQuery").format("memory").start())

# COMMAND ----------

display(input, streamName="DisplayMemoryQuery", processingTime = '10 seconds')
