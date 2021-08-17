import statistics as st
import pandas as pd
import csv
import random
import plotly.figure_factory as ff
import plotly.graph_objects as go
df=pd.read_csv("newdata.csv")
data=df["average"].tolist()
population_mean=st.mean(data)
population_stdev=st.stdev(data)
print(population_stdev,population_mean)
def random_set_mean(counter):
    dataset=[]
    for i in range(0,100):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)
    mean=st.mean(dataset)
    return(mean)
def show_graph(meanlist):
    data=meanlist
    mean=st.mean(data)
    stdev=st.stdev(data)
    print(mean,stdev)
    graph=ff.create_distplot([data],["temp"],show_hist=False)
    graph.add_trace(go.Scatter(x=[mean,mean],y=[0,10],mode="lines",name="mean"))
    graph.show()
def setup():
    meanlist=[]
    for i in range(0,1000):
        setofmean=random_set_mean(100)
        meanlist.append(setofmean)
    show_graph(meanlist)
setup()