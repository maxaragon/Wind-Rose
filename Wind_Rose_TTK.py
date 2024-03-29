from windrose import WindroseAxes
from windrose import plot_windrose
from matplotlib import pyplot as plt 
import matplotlib.cm as cm 
import numpy as np 
import pandas as pd 


df = pd.read_csv(r'C:\Users\max_a\Dropbox\MAX\Earth Sciences\4th\Hydromet\Wind rose\Data\2018_06.csv', #Path of the csv file 
header=0, index_col=None, low_memory=False, na_values='nincsadat')
df = df.dropna(subset=['Wgd', 'Wg']) # Eliminate nincsadat values from columns Wgd and Wg

df = df.drop(['Tg3', 'Tg2', 'Tg1', 'Ta', 'Rh', 'Sr', 'Td'], axis=1)

bins = [ 0, 12.25, 34.75, 57.25, 79.75, 102.25, 124.75, 147.25, 169.75, 192.25, 214.75, 237.25, 259.75, 282.25, 304.75, 327.25, 349.75, 360]
wind = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW', 'N']

df['Direction'] = pd.cut(df['Wgd'], bins, labels = pd.Categorical(wind)) #Add a new column and use pd.Categorical to fix the required uniqueness


Directions = pd.value_counts(df['Direction'], normalize=True, sort =False).reindex(['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW']) #Count values 


Normalize_percentage = (Directions*100).plot(kind = 'bar')

plt.title("Normalized wind direction Pécs 12/2018") #Name of the bar plot!
Normalize_percentage.set(xlabel=None, ylabel='Percentage %')

binss = [ 0, 2, 4, 6, 8, 10, 12]
speed = ['0-2', '2-4', '4-6', '6-8', '8-10', '10+']


df['Speed'] = pd.cut(df['Wg'], binss, labels = speed)



DirSpeed = df.groupby(['Direction','Speed']).size() #Number of events per direction and speed category

#DirSpeed.to_csv(r'C:\Users\max_a\Dropbox\MAX\Earth Sciences\4th\Hydromet\Wind rose\Data\January_96.csv', index = False)

print(DirSpeed)

D = df.groupby(['Direction'])['Wg'].mean().reindex(['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW']) 
print(D)


ws = df["Wg"].values
wd = df["Wgd"].values


df = pd.DataFrame({'speed': ws, 'direction': wd})
ax = plot_windrose(df, kind='contourf', bins=np.arange(0.01,10,1), cmap=cm.YlGn) 
plt.title('December 2018') #Name of the Wind Rose!

plt.legend(title='Wind speed (m/s)', loc='best', fancybox=True) 
plt.show()