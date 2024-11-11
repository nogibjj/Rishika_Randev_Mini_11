[![CI](https://github.com/nogibjj/Rishika_Randev_Mini_10/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/Rishika_Randev_Mini_10/actions/workflows/cicd.yml)
# Rishika Randev's Python Script for IDS706 Week 10

## ☑️ Requirements (Mini Project 10):
1. Use PySpark to perform data processing on a large dataset
2. Include at least one Spark SQL query and one data transformation

## ☑️ The Dataset
The dataset used in this project shows the frequency of depression and anxiety symptoms for various different groups across the US over the course of 7 days (05/07 - 05/14) in 2020. It was collected by the U.S. Census Bureau as part of the Household Pulse Survey to capture the impact of COVID on Americans, and is freely available through data.gov at this link: https://catalog.data.gov/dataset/indicators-of-anxiety-or-depression-based-on-reported-frequency-of-symptoms-during-last-7-.

## ☑️ Steps
1. Prepare the necesary configuration files like the Dockerfile, devcontainer.json, Makefile, requirements.txt, and main.yml for GitHub Actions integration. Ensure that the requirements.txt lists all necessary packages (for example, pyspark).
2. Create a library folder with a lib.py file which contains the following functions:
   * An extract function, which pulls the above csv from the Internet, and writes some the following columns to a data/MH.csv file.
       * Indicator, which represents whether the row's data is related to anxiety, depression, or both
       * Group, which is always "By State" in this case since I wanted to analyze the data statewise
       * State 
       * Time Period Start Date, which is always 05/07/2020
       * Time Period End Date, which is always 05/14/2020
       * Value, which is the frequence value of the Indicator mentioned above
       * & High CI, which is the upper bound of the 95% confidence interval for this value
   * Start and end functions which start and end a PySpark session, respectively.
   * A load function which loads the data from data/MH.csv into PySpark.
   * A general query function which allows any Spark SQL query to be run against the data.
   * A describe function which generates basic summary statistics on the data for the output markdown file.
   * A transformation function which adds a column to the dataset with the average value of each indicator across the states.
4. Create a main.py script which calls all of the lib functions.
5. Create a test_main.py script which ensures that the lib functions run successfully.
