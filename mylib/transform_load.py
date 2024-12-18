"""
Transforms and Loads data into a Databricks database
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import monotonically_increasing_id


def load(dataset="/tmp/MH_COVID.csv"):
    """ Transforms and Loads data into Databricks delta lake table"""
    spark = SparkSession.builder.appName("MH").getOrCreate()
    mh_df = spark.read.csv(dataset, header=True, inferSchema=True)
    mh_df = mh_df.withColumn("id", monotonically_increasing_id())
    mh_df = mh_df.drop("Phase", "Time Period", "Time Period Label", \
        "Time Period Start Date", \
        "Time Period End Date", "Low CI", "High CI", \
        "Confidence Interval", "Quartile Range")
    mh_df = mh_df.filter(mh_df.Group == "By State")
    mh_df.write.format("delta").mode("overwrite").saveAsTable("mental_health_covid_delta")
    print("Successfully transformed and loaded data to Databricks")
    return "Success"

if __name__=="__main__":
    load()