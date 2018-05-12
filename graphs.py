import matplotlib.pyplot as pt
import pandas as pd
import numpy as np
import operator

def line_graph_countries():
    colnames=['Country','Year','Infant_mortality_rate','Neonatal_mortality_rate','Under-five_mortality_rate']
    data=pd.read_csv("WHOSIS_MDG_000003.csv",names=colnames)#reading the data from file
    country=data.Country.tolist()
    year=data.Year.tolist()
    IM=data.Infant_mortality_rate.tolist()
    IM_bar=[]
    country_bar=[]
    # extraing the info for specific year
    for x in range(len(year)):
        if year[x] == '1990':
            temp=IM[x].split("[")
            IM_bar.append(float(temp[0]))
            country_bar.append(country[x])
    dictionary = dict(zip(country_bar,IM_bar))

    sorted_x = sorted(dictionary.items(), key=operator.itemgetter(1))
    country=[]
    IM=[]
    for x in range(0,len(sorted_x),10):
        country.append(sorted_x[x][0])
        IM.append(sorted_x[x][1])

    pt.plot(country,IM)
    pt.xticks(country, country, rotation='vertical')
    pt.xlabel("Country")
    pt.ylabel("mortality rate")
    pt.title("Country VS mortality rate")
    pt.show()

def bar_graph_countries(inyear):
    colnames=['Country','Year','Infant_mortality_rate','Neonatal_mortality_rate','Under-five_mortality_rate']
    data=pd.read_csv("WHOSIS_MDG_000003.csv",names=colnames)#reading the data from file
    country=data.Country.tolist()
    year=data.Year.tolist()
    IM=data.Infant_mortality_rate.tolist()
    # varible name with _bar is the lists that are used in the graph plotting
    IM_bar=[]
    country_bar=[]
    # extrating the info for year 1990
    for x in range(len(year)):
        if year[x] == inyear:
            temp=IM[x].split("[")
            IM_bar.append(float(temp[0]))
            country_bar.append(country[x])
    dictionary = dict(zip(country_bar,IM_bar))
    # sorting the information
    sorted_x = sorted(dictionary.items(), key=operator.itemgetter(1))
    country=[]
    IM=[]
    for x in range(0,len(sorted_x),10):
        country.append(sorted_x[x][0])
        IM.append(sorted_x[x][1])

    pt.bar(country,IM)
    pt.xticks(country, country, rotation='vertical')
    pt.xlabel("Country")
    pt.ylabel("mortality rate")
    pt.title("Country VS mortality rate")
    pt.show()



def compare_plot():
    colnames=['Country','Year','Infant_mortality_rate','Neonatal_mortality_rate','Under-five_mortality_rate']
    data=pd.read_csv("WHOSIS_MDG_000003.csv",names=colnames)#reading the data from file
    country=data.Country.tolist()
    year=data.Year.tolist()
    IM=data.Infant_mortality_rate.tolist()
    IM_bar1=[]
    IM_bar2=[]
    IM_bar3=[]
    year_bar1=[]
    year_bar2=[]
    year_bar3=[]
    for x in range(len(country)):
        if country[x] == 'Japan':
            temp=IM[x].split("[")
            IM_bar1.append(float(temp[0]))
            year_bar1.append(year[x])
        elif country[x] == "Fiji":
            temp=IM[x].split("[")
            IM_bar2.append(float(temp[0]))
            year_bar2.append(year[x])
        elif country[x] == "Czech Republic":
            temp=IM[x].split("[")
            IM_bar3.append(float(temp[0]))
            year_bar3.append(year[x])

    pt.plot(year_bar1[::-1],IM_bar1,color="orange",label="Japan")
    pt.plot(year_bar2[::-1],IM_bar2,color="red",label="Fiji")
    pt.plot(year_bar3[::-1],IM_bar3,color="black",label="Czech Republic")
    pt.legend()
    pt.xticks(year_bar1,year_bar1, rotation='vertical')
    pt.xlabel("years")
    pt.ylabel("mortality rate")
    pt.title("years VS mortality rate")
    pt.show()

def reductoin_in_MR():
    colnames=['Country','Year','Infant_mortality_rate','Neonatal_mortality_rate','Under-five_mortality_rate']
    data=pd.read_csv("WHOSIS_MDG_000003.csv",names=colnames)#reading the data from file
    country=data.Country.tolist()
    year=data.Year.tolist()
    IM=data.Infant_mortality_rate.tolist()

    for x in range(len(country)):
        if country[x] == 'Japan':
            if year[x]=='1990':
                temp=IM[x].split("[")
                initial1=float(temp[0])
            elif year[x]=='2015':
                temp=IM[x].split("[")
                final1=float(temp[0])
        elif country[x] == "Fiji":
            if year[x]=='1990':
                temp=IM[x].split("[")
                initial2=float(temp[0])
            elif year[x]=='2015':
                temp=IM[x].split("[")
                final2=float(temp[0])
        elif country[x] == "Czech Republic":
            if year[x]=='1990':
                temp=IM[x].split("[")
                initial3=float(temp[0])
            elif year[x]=='2015':
                temp=IM[x].split("[")
                final3=float(temp[0])

    reduction_rate=[initial1-final1,initial2-final2,initial3-final3]
    countries=['Japan','Fiji','Czech Republic']
    pt.bar(countries,reduction_rate)
    pt.xlabel("Countries")
    pt.ylabel("Reduction Rate")
    pt.show()
    
line_graph_countries()
bar_graph_countries('1990')
bar_graph_countries('2015')
compare_plot()
reductoin_in_MR()
