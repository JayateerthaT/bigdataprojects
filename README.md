# bigdataprojects

Project related to SimpliLearn courses 311 NYC Service calls
## Dataset file is 311_Service_Requests_for_2009.csv. File size is 876 MB.
### Steps followed
   * Created a subset of the large file by removing umwanted data variables. After whcih file size was 149 MB.
   * Use this process file for the further analysis.
   
Dataset has observations 1783133 and variables 52. There are few observations for which close date is null. Means those tickets are not closed status. I have considered closed tickets for analysis. After removing “open / pending” observations from dataset. 59331 observations did not have the closed date value. I have considered Complaint Type & City variables for analysis. There are 152 complaint types are present in the data set.

