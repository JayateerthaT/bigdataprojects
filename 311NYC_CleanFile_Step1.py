import numpy as np
import pandas as pd
import datetime

NYC311_df = pd.read_csv(r'C:\Users\SeemaJT\Downloads\Python\Final project\submission\311_SR_2009_Cleaned.csv')

#Get the count for Complaint type & City
new_Type_City_df = pd.core.frame.DataFrame({'count' : 
                        NYC311_df.groupby( [ "Complaint Type", "City"] ).size()}).reset_index()

new_Type_City_df.to_csv(r'C:\Users\SeemaJT\Downloads\Python\Final project\submission\311_SR_2009_new_Type_City_df.csv', sep=',', encoding='utf-8')

#get the count for Complaint Type only
new_CompType_df = pd.core.frame.DataFrame({'count' : 
        NYC311_df.groupby( [ "Complaint Type"] ).size()}).reset_index()

new_CompType_df.to_csv(r'C:\Users\SeemaJT\Downloads\Python\Final project\submission\311_SR_2009_new_CompType_df.csv', sep=',', encoding='utf-8')

#Get the count for Complaint type, City & days
new_Type_City_days_df = pd.core.frame.DataFrame({'count' : 
                        NYC311_df.groupby( [ "Complaint Type", "City","day"] ).size()}).reset_index()

new_Type_City_days_df.to_csv(r'C:\Users\SeemaJT\Downloads\Python\Final project\submission\311_SR_2009_new_Type_City_days_df.csv', sep=',', encoding='utf-8')

#Get the count for Complaint type, City & days
new_Type_days_df = pd.core.frame.DataFrame({'count' : 
                        NYC311_df.groupby( [ "Complaint Type", "day"] ).size()}).reset_index()

new_Type_days_df.to_csv(r'C:\Users\SeemaJT\Downloads\Python\Final project\submission\311_SR_2009_new_Type_days_df.csv', sep=',', encoding='utf-8')



