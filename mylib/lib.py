"""
library
"""
import os
import requests
import pandas as pd
from pyspark.sql import SparkSession

from pyspark.sql.types import (
     StructType, 
     StructField, 
     StringType, 
     DateType,
     FloatType
)

LOG_FILE = "pyspark_output.md"


def log_output(operation, output, query=None):
    """adds to a markdown file"""
    with open(LOG_FILE, "a") as file:
        file.write(f"The operation is {operation}\n\n")
        if query: 
            file.write(f"The query is {query}\n\n")
        file.write("The truncated output is: \n\n")
        file.write(output)
        file.write("\n\n")

def start_spark(appName):
    spark = SparkSession.builder.appName(appName).getOrCreate()
    return spark

def end_spark(spark):
    spark.stop()
    return "stopped spark session"

def extract(url="https://data.cdc.gov/api/views/8pt5-q6wp/rows.csv?accessType=DOWNLOAD", 
            file_path="data/MH.csv", directory = "data"):
    """"Extract a url to a file path"""
    if not os.path.exists(directory):
        os.makedirs(directory)
    with requests.get(url) as r:
        with open(file_path, 'wb') as f:
            f.write(r.content)
    df = pd.read_csv(file_path)
    df_subset = df.loc[(df["Group"] == "By State") \
        & (df["Time Period Start Date"] == "05/07/2020"), \
        ["Indicator", "Group", "State", "Time Period Start Date", \
        "Time Period End Date", "Value", "High CI"]]
    df_subset.to_csv(file_path, index=False)
    print("Successfully extracted data")   
    return file_path

def load_data(spark, data="data/MH.csv", name="MentalHealthCOVID"):
    """load data"""
    # data preprocessing by setting schema
    schema = StructType([
        StructField("Indicator", StringType(), True),
        StructField("Group", StringType(), True),
        StructField("State", StringType(), True),
        StructField("Time Period Start Date", DateType(), True),
        StructField("Time Period End Date", DateType(), True),
        StructField("Value", FloatType(), True),
        StructField("High CI", FloatType(), True)
    ])

    df = spark.read.option("header", "true").schema(schema).csv(data)

    log_output("load data", df.limit(10).toPandas().to_markdown())

    return df


def query(spark, df, query, name): 
    """queries using spark sql"""
    df = df.createOrReplaceTempView(name)

    log_output("query data", spark.sql(query).toPandas().to_markdown(), query)

    return spark.sql(query).show()

def describe(df):
    summary_stats_str = df.describe().toPandas().to_markdown()
    log_output("describe data", summary_stats_str)

    return df.describe().show()

def example_transform(df):
    avgs = df.groupby(by='Indicator')['Value'].transform('mean') 
    df['Average Value for Indicator'] = avgs
    log_output("transform data", df.limit(10).toPandas().to_markdown())

    return df.show()


