"""
Extract
"""
import urllib.request


def extract(url="https://data.cdc.gov/api/views/8pt5-q6wp/rows.csv?accessType=DOWNLOAD", 
            file_path="/dbfs/tmp/MH_COVID.csv"):
    """"Extract a url to a DBFS file path"""
    urllib.request.urlretrieve(url, file_path)
    print("Successfully extracted data")   
    print(file_path)

if __name__=="__main__":
    extract()


