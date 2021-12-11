import csv
import plotly.figure_factory as ff
import pandas as pd
import statistics
import random
import plotly.graph_objects as go

df = pd.read_csv("medium_data.csv")
data = df["id"].tolist()


mean = statistics.mean(data)
std_deviation = statistics.stdev(data)

def randomSetOfMean(counter):
    dataset = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data)- 1)
        value = data[random_index]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean

mean_list = []
for i in range (0,1000):
    setOfMeans= randomSetOfMean(100)
    mean_list.append(setOfMeans)




mean = statistics.mean(data)
std_deviation = statistics.stdev(data)
print(mean)
print(std_deviation)

std_deviation = statistics.stdev(mean_list)

mean = statistics.mean(mean_list)
print(mean)
print(std_deviation)

first_std_deviation_start, first_std_deviation_end = mean-std_deviation, mean+std_deviation
second_std_deviation_start, second_std_deviation_end = mean-(2*std_deviation), mean+(2*std_deviation)
third_std_deviation_start, third_std_deviation_end = mean-(3*std_deviation), mean+(3*std_deviation)
print("std1",first_std_deviation_start, first_std_deviation_end)
print("std2",second_std_deviation_start, second_std_deviation_end)
print("std3",third_std_deviation_start,third_std_deviation_end)




fig = ff.create_distplot([mean_list], ["student marks"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_start], y=[0, 0.17], mode="lines", name="MEAN OF STUDNETS WHO GOT FUNSHEETS"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END"))
fig.show()


