import csv
import matplotlib.pyplot as mp
import plotly.express as px
import pandas as pd
from mimetypes import init
from sklearn.cluster import KMeans
from random import random
import seaborn as se
#making a file 
mass = []
radius = []
with open("dwarf_stars.csv", "r") as f:
    csv_reader = csv.reader(f)
    for i in csv_reader:
        radius.append(i)
with open("bright_stars.csv", "r") as f2:
    csv_reader = csv.reader(f2)
    for i in csv_reader:
        mass.append(i)

radius1 = radius[2]
mass1 = mass[3]
for i in radius1:
    final_radius = float(i)*6.957+8

for i in mass1:
    final_mass = float(i)* 1.989+30

gravity = []
g = 6.67*10**-11
gravity = g*final_mass/final_radius
for i in gravity:
    gravity.append(i)
#print(gravity)

#data science 2
planet_mass = []
planet_radius = []
planet_gravity = []

for i in mass:
    planet_mass.append(i)

for i in radius:
    planet_radius.append(i)

for i in gravity:
    planet_gravity.append(i)
planet_mass = planet_mass.sort("mass", ascending = False)
planet_radius = planet_radius.sort("radius", ascending = False )

fig = px.scatter(x = planet_mass, y = planet_radius)
#fig.show()

#kmeans clustering

list1 = []
for i, mass in enumerate(planet_mass):
    list2 = [planet_radius[i], mass]
    list1.append(list2)
wcss = []
for i in range(1,11):
    k = KMeans(n_clusters = i, init = "k-means++", random_state = 42)
    k.fit(list1)
    wcss.append(k.inertia_)

mp.figure(figsize=(10, 5))
se.lineplot(range(1, 11), wcss, marker = "o", color = "blue")
mp.title("KMeans clustering")
mp.xlabel("x = Number of cluster")
mp.ylabel("y = wcss")
#mat.show()

bright_distance = []
dwarf_distance = []
final_distance = []

with open("bright_stars.csv", "r") as f:
    csv_reader = csv.reader(f)
    for i in csv_reader:
        bright_distance.append(i[2])

with open("dwarf_stars.csv", "r") as f:
    csv_reader = csv.reader(f)
    for i in csv_reader:
        dwarf_distance.append(i[2])
    
for i in bright_distance:
    final_distance.append(i)

for i in dwarf_distance:
    final_distance.append(i)

final_distance.remove("Distance")
#print(final_distance)

for i in final_distance:
    if i <= 100:
        print(i)

#star vs mass
star_name = []
df = pd.read_csv("bright_stars.csv")
for i in df:
    star_name.append(i[1])
fig = px.bar(x = star_name, y = planet_mass)
fig.show()

#star name vs radius
star_name2 = []
df2 = pd.read_csv("dwarf_stars.csv")
for i in df2:
    star_name2.append(i[2])
fig2 = px.bar(x = star_name2, y = planet_radius)
fig2.show

#star name vs distance

star_name3 = star_name + star_name2

fig3 = px.bar(x = star_name3, y = final_distance)
fig3.show()

#star name vs gravity

star_name4 = star_name3

fig4 = px.bar(x = star_name4, y = planet_gravity)
fig4.show()

#making dictioneries

