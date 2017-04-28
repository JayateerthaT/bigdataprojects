
# bigdataprojects

## Project related to SimpliLearn courses 
### Analyze health reports across years for the US market
A insurance provider has decided to launch a new medical insurance program targeting various customers. To help this customer understand the current realities and the market better. We have to perform a series of data analytics tasks using Hadoop. The customer has provided the data set.
### Project goals:
1) Calculate the average % of people, aged between 18 and 64, who have obtained insurance from private players from 2001 to 2011
2) Calculate the average percentage of people, aged 65 years or more, who are solely covered by public insurance from the year 2001 to 2011

Data set in xls format from the URL :
[Insurance Data Set](http://www.census.gov/hhes/www/hlthins/data/utilization/tables.html)

### Steps followed
   * Conversion xls to csv filesFor conversion linux gnumeric was used.
     * Example : ssconvert -S 2001.xls 2001.csv
   * Data cleaning performed:
     * The original file has hierarchical data stored in csv format. The Tab4 (after split <year>.csv.3) contains the data to be     processed. For a given requirement there multiple records are present. We need to fetch the specific parent child relation records. Hence I took data cleaning approach to analyze the data set. Read the parent value append it to child value (logic listed in python code). So that data becomes normalized. On this data set DML operations can be performed. Refer the image of insurance_clean_data.py to clean data. Once the data is cleaned upload to CloudLab for further processing using Pig.
   * Above python code converts *.3 files *.3.csv files
   * Upload the *.csv.3.csv files to cloudlab in insurance folder
   * Execute pig scripts on these files 
     * Refer insurance_project_report.pdf & insurance_project_sourcecode.pdf files for Report and PigLatin Scripts for each goals. 


