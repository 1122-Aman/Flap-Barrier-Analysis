# Flap-Barrier-Analysis
About Spintly:
Spintly is a third-party agency whose flap barriers we use, basically it’s the access system that you are using while coming to office which helps in monitoring a particular user_id access time and location or moreover covers an attendance detail and also encompass, the user_name and location from which he has accessed flap barrier thus helping an institute for maintaining record in the future.

Project Objective: 
1) % People giving complete time.
2) % of population who does entry & exit in a day and comparing with other day data in a week
3) % of population moving in and out during office hours
4) Count of people accessing flap barrier using mobile or card
5) Time Spent in office by an user 

Data Source: "E:\Python files\raw_data\spintly_data_2023_3_months.csv" Tools: Excel, Python, Jupyter Notebook
Data approach:
In the given data, we’ll first segregate the data by applying df[‘company_id’] == 202, to get only those data which is related to smartworks employees and the we will divide the data into different centres like bangalore, Noida, Gurgaon centre data.
Here is the code to filter the data from raw database.
 

Here is the snippet of Bangalore csv data-

 

1)	Access_Type Data
Access type data denotes that how employees access the flap barrier like by using card or mobile. From the data it is observed that there are 4 ways of accessing flap barrier, namely, by card, card_access, mobile and by mobile_access.
a)
In first scenario we will study how employees access the barriers using card and mobile.
Thus, it is observed that out of 55000 entries 42.73% of employees are accessing flap barrier for entry purpose using mobile whereas only 10.91% barrier employees use card. And when compared with exit percentage it stands at 12.73% and 2.73% respectively.
Thus it can be inferred from above data that only 25% of employees are using the flap barrier for entry & exit purpose using mobile &  card mode over a period of 3 months and rest 75 % employees are not using the same.
b)
Now in we’ll take look into mobile_access and card_access scenario.
It is observed from the data that 14.55% (out of 55000) of employees are accessing flap barrier for entry using "mobile_access" & 4.55% are using card_access. And when comparing their respective exit percentage data, it stands at 9.09% & 2.73% respectively which means that only 60% and 50% employees are using mobile_access and card_access mode for doing entry & exit for over a period of 3 months.

2)	Number of Entry & Exit within 3 months

When the spintly flap barrier data is plotted for consecutive 3 months, i.e, for June, July & august it is observed that only 43.57% out of 14000 of employees are doing exit after entry. And when doing the same analysis for remaining two months it is inferred that number stands at 
58.21% out of 5286 & 40.22% out of 1801.

Similary Data for other city is inferred.
