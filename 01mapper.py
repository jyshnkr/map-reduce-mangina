# JayaShankar's Mapper Function
import sys

for line in sys.stdin:  
    dataList = line.strip().split(",") 
    
    if (len(dataList) == 7) :
        TotalMoney,GameName,Genre,PlayerNo,TournamentNo,Top_Country,Top_Country_Earnings = dataList 
        print (Top_Country,"\t", Top_Country_Earnings)