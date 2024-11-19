"""
ETL-Query script
"""

from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import query



def main():
    extracted_data = extract()
    assert extracted_data == "/dbfs/tmp/MH_COVID.csv"
    result = load()
    assert result == "Success"
    print(
        query(
            "SELECT Indicator, MAX(Value) Max_Value_Across_States \
        FROM MentalHealthCOVID \
        GROUP BY Indicator",
            "MentalHealthCOVID",
        )
    )


if __name__ == "__main__":
    main()
