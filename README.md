# map-reduce-mangina
Dataset URL : https://www.kaggle.com/rushikeshhiray/esport-earnings

## DataSet Details
The Dataset contains the information about Top earnings of Various ESport Games in Top countries.

## Analysis
I have processed the raw data using the Mapping technique and mapped two columns Top_Country, Top_Country_Earnings. Now, we have Total earnings coming from top countries. By using reducing technique, i have reduced data and displayed Count.

## How to run the script
> 1. Clone the repo to your system
> 2. Navigate to the project/repo directory on your system. Open Powershell/VS Code terminal at the project directory
> 3. Now, copy and paste the below commands in your terminal to run the scripts:

> For Mapping :

```cat ESport_Earnings.csv | Python 01mapper.py > ManginaOutput1.txt```

> For Reducing:

```cat ESport_Earnings.csv | Python 01mapper.py | sort | Python 01reducer.py > ManginaOutput2.txt```

## Chart
![Picture1](https://user-images.githubusercontent.com/79549340/152569637-956453e5-85b2-42f2-94e2-7ffc4fd9a0b5.png)
