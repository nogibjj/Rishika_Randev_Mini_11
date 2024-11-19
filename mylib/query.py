"""
library
"""
from pyspark.sql import SparkSession

def query(query): 
    """Queries using spark sql"""
    spark = SparkSession.builder.appName("Query").getOrCreate()
    return spark.sql(query).show()


if __name__ == "__main__":
    sql_query = "SELECT Indicator, MAX(Value) Max_Value_Across_States \
        FROM mental_health_covid_delta \
        GROUP BY Indicator"
    query(sql_query)


