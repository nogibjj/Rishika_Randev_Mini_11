# Rishika Randev's Python Script for IDS706 Week 11

## ☑️ Requirements (Mini Project 11):
1. Create a data pipeline using Databricks
2. Include at least one data source and one data sink

## ☑️ The Dataset
The dataset used in this project shows the frequency of depression and anxiety symptoms for various different groups across the US over the course of several 7 day intervals in 2020. It was collected by the U.S. Census Bureau as part of the Household Pulse Survey to capture the impact of COVID on Americans, and is freely available through data.gov at this link: https://catalog.data.gov/dataset/indicators-of-anxiety-or-depression-based-on-reported-frequency-of-symptoms-during-last-7-.

## ☑️ Steps
1. Prepare the necesary configuration files like the Dockerfile, devcontainer.json, Makefile, requirements.txt, and main.yml for GitHub Actions integration. Ensure that the requirements.txt lists all necessary packages (for example, pyspark, python-dotenv, databricks-sql-connector).
2. Create a library folder with a lib.py file which contains the following functions:
   * An extract function, which pulls the above csv from the Internet, and writes some the following columns to a temporary location in the Databricks DBFS.
   * A load function which transforms (by dropping a few columns and adding an ID column) and loads the data from DBFS into a Databricks delta lake.
   * A general query function which allows any Spark SQL query to be run against the Databricks delta lake.
4. Create a main.py script which calls all of the library functions.
5. Create a test_main.py script which ensures that the Databricks DBFS file path is accessible.

## ☑️ Databricks
Databricks notebooks were used to create the Python scripts and then run them on a personal compute. The changes on Databricks were later synced to GitHub. To set up a personal compute, follow these settings:
<img width="1106" alt="Screenshot 2024-11-18 at 8 04 15 PM" src="https://github.com/user-attachments/assets/60e929fd-70b7-4088-a0c4-cfa5eeaad2bb">


The extract, transform/load, and query steps were then put into a job to demonstrate that the ETL pipeline could run successfully.
<img width="858" alt="Screenshot 2024-11-18 at 7 54 42 PM" src="https://github.com/user-attachments/assets/294763e1-f200-4884-8a18-669238de6bd0">

To create a job:
1. On Databricks, navigate to Workflows and click "Create a job."
2. Give the task a relevant name, such as "Extract." Then select the type as "Python script" and source as "Workspace" with the path being the location in the Databricks workspace hwere you have saved your extract.py script.
3. Change the compute to your personal compute.
4. Add any required dependent libraries for your Python script from PyPI, such as python-dotenv and databricks-sql-connector.
5. Click "Create task." Then add any following tasks in the same way, but set their "dependent on" setting to previous tasks (for example, when you create the transform_load task, you can set it to be dependent on the extract task).
<img width="824" alt="Screenshot 2024-11-18 at 8 02 43 PM" src="https://github.com/user-attachments/assets/82fb2d39-e067-4f01-89a0-057ca83c32cc">
