"""
ETL-Query script
"""

from mylib.lib import (
    start_spark,
    end_spark,
    extract,
    load_data,
    describe,
    example_transform,
    query,
)


def main():
    spark = start_spark("MentalHealthCOVID")
    print(extract())
    df = load_data(spark)
    print(describe(df))
    print(
        query(
            spark,
            df,
            "SELECT Indicator, MAX(Value) Max_Value_Across_States \
        FROM MentalHealthCOVID \
        GROUP BY Indicator",
            "MentalHealthCOVID",
        )
    )
    example_transform(df)
    end_spark(spark)


if __name__ == "__main__":
    main()
