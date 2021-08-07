import pandas as pd
import csv

df = pd.read_csv('total_stars.csv')


gravity = []


##### As one of the radius value was '1,158' it was failing. So written following function to replace ','.

df['Radius']=df['Radius'].apply(lambda x: x.replace(',', '')).astype('float')
mass = df['Mass'].to_list()
radius = df['Radius'].to_list()

########converting solar mass and radius into km & kg
def convert_to_si(radius,mass):
    for i in range(0,len(radius)-1):
        radius[i] = float(radius[i])*6.957e+8
        mass[i] = mass[i]*1.989e+30
        
convert_to_si(radius,mass)

def gravityformula(mass, radius):
    G = 6.674e-11
    for i in range(0, len(mass)):
        g = (mass[i]*G)/((radius[i])**2)
        gravity.append(g)

gravityformula(mass, radius)

df["gravity"] = gravity
df.to_csv("starswithgravity.csv")
