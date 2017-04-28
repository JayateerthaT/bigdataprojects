# bigdataprojects

## Project related to SimpliLearn courses 
_(I have shared the two project details in this readme.md file)_  

### Analyze health reports across years for the US market _(PigLatin)_
A insurance provider has decided to launch a new medical insurance program targeting various customers. To help this customer understand the current realities and the market better. We have to perform a series of data analytics tasks using Hadoop. The customer has provided the data set.
### Project goals:
1) Calculate the average % of people, aged between 18 and 64, who have obtained insurance from private players from 2001 to 2011
2) Calculate the average percentage of people, aged 65 years or more, who are solely covered by public insurance from the year 2001 to 2011

Get the "Retail and food services sales" dataset from "Monthly retail trade report" tab
Data set in xls format from the URL :
[Retail Data Set](http://www.census.gov/retail/index.html)

### Steps followed
   * Conversion xls to csv files. For conversion linux gnumeric was used.
     * Example : _ssconvert -S 2001.xls 2001.csv_
   * Data cleaning performed:
     * The original file has hierarchical data stored in csv format. The Tab4 (after split <year>.csv.3) contains the data to be     processed. For a given requirement there multiple records are present. We need to fetch the specific parent child relation records. Hence I took data cleaning approach to analyze the data set. Read the parent value append it to child value (logic listed in python code). So that data becomes normalized. On this data set DML operations can be performed. Refer the image of insurance_clean_data.py to clean data. Once the data is cleaned upload to CloudLab for further processing using Pig.
   * Above python code converts *.3 files *.3.csv files
   * Upload the *.csv.3.csv files to cloudlab in insurance folder
   * Execute pig scripts on these files 
     * Refer insurance_project_report.pdf & insurance_project_sourcecode.pdf files for Report and PigLatin Scripts for each goals. 


### Analyze monthly retail trade report for the US market _(Hive)_
   * A US-based online retailer wants to launch a new product category and wants to understand the potential growth areas and areas that have stagnated over a period of time. 
   * It wants to use this information to ensure its product focus is aligned to opportunities that will grow over the next 5–7years. 
   * The customer has also provided pointers to the data set you can use. 

### Project goals:
   1) Analyze the entire data set and arrive at products that have experienced a consolidated yearly growth of 10% or more in sales since 2000.
   2) Analyze the entire data set and arrive at products that have experienced a consolidated yearly drop of 5% or less since 2000.
   3) Arrive at products that have experienced a growth of 10% or more in sales from 2000 to 2005, and then subsequently experienced a drop of at least 2% in sales from 2006 to 2013.

Data set in xls format from the URL :
[Insurance Data Set](http://www.census.gov/hhes/www/hlthins/data/utilization/tables.html)

### Steps followed
   * Conversion xls to csv files. For conversion linux gnumeric was used.
     * Example : _ssconvert -S Test_Data.xls Test_Data.csv_
     * _ssconvert created one csv per excel sheet. Hence 0 to 23 csv files were created for each year 1992 to 2015._
   * Data cleaning performed:
     * Using _sed_ command csv files were cleaned. 
     * Additional step performed: 
       *I was experience too many timeouts while loading the data to hive. Hence decided to merge the all the required files into one csv with year as new column. 
          * Upload the merged data csv file to cloudlab
          * Create a generic table tran_generic 
          * Load the data to generic table
          * load respective year data to specific tables to meet the project requirement.
          * Upload this file to couldLab retril_proj folder
          

_These above steps helped me to speed up the processing. And also provided me an opportunity to enhance my python skills._
     * Refer retail_project_report.pdf & retail_project_sourcecode.pdf files for Report and Hive Scripts for each goals. 
     
