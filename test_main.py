"""
Test goes here

"""
import pytest

from mylib.lib import (
    start_spark,
    end_spark,
    extract,
    load_data,
    describe,
    example_transform,
    query,
)

@pytest.fixture(scope="module")
def spark():
    spark = start_spark("MH")
    yield spark
    end_spark(spark)

def test_extract():
    extracted_data = extract()
    assert extracted_data == "data/MH.csv"


def test_load_data(spark):
    df = load_data(spark)
    assert df is not None


def test_describe(spark):
    df = load_data(spark)
    assert describe(df) is None


def test_transform(spark):
    df = load_data(spark)
    assert example_transform(df) is None


def test_query(spark):
    df = load_data(spark)
    result = query(
        spark,
        df,
        "SELECT Indicator, MAX(Value) Max_Value_Across_States \
        FROM MentalHealthCOVID \
        GROUP BY Indicator",
        "MentalHealthCOVID",
    )
    assert result is None


if __name__ == "__main__":
    test_extract()
    test_load_data(spark)
    test_describe(spark)
    test_transform(spark)
    test_query(spark)
