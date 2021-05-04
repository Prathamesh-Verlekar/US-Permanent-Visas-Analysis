# Big-Data-Architecture-and-Governance

## Project Objective
1)To clean and validate the data extracted from USCIS website
2)Create a data model based on the dataset
3)Create a database in Neo4j and load the data using Cypher queries
4)Create a data pipeline for connecting Neo4j to Python
5)Build an interactive dashboard for better insights
6)Integration and Acceptance testing for data validation

## Data Overview using Pandas Profiling
1) This Dataset gives detailed information of around 374K visa applications and its decision.
2) Data covers 2011-2016 and includes information on employer, position, wage offered, job posting history, employee education and past visa history, and final decision. 
3) we can analyze that the dataset has 374362 observations out of which 373025 are unique observations. The dataset has 154 variables out of which only 21 variables have more than 330000 non-missing observations. 
4) The Dataset has,
116 Categorical values
2 Date Time values
10 Numerical values
26 Boolean values


## Technical Vision Diagram
![Group_Vision_Diagram (4)](https://user-images.githubusercontent.com/55213702/116940272-b4205d80-ac3b-11eb-8800-daaa61023cf3.png)

## Graph Data Model
![US Perm Visa Data Model](https://user-images.githubusercontent.com/55213702/116940654-40328500-ac3c-11eb-8495-938c57d766a4.png)

## Database Schema in Neo4j
![image](https://user-images.githubusercontent.com/55213702/116942971-a28d8480-ac40-11eb-8226-6d194d3bf308.png)

## Interactive Dashboard
![Full Dashboard Image](https://user-images.githubusercontent.com/55213702/116943116-e54f5c80-ac40-11eb-8454-8825c8ddffb4.png)

### Target Audience
1) US Citizenship and Immigration Services</br>
2) Corporates of different sectors </br>
3) Immigrants applying for US Visa </br>

### Dashboard Insights
1) We found that H-1B is the top visa application that is applied through the different companies and has most approved visas.
2) Amazon is amongst top 5 companies that file the highest number of visa applications. 
3) Computer Engineering is the hottest job for which companies are filling visa application and has highest rate of approval.
4) India is the country with the most visa applications filed throughout the world and has the most approved cases.


