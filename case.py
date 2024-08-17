#місце для твого коду
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Space_Corrected.csv')
df.info()
df["Rocket"].fillna(-1, inplace = True)
df.dropna(inplace = True)
df.info()
def get_time(date):
    time = date.split()
    if len(time) > 4:
        time = time[4]
        return int(time[:2])
    else:
        return -1
df['Time'] = df['Datum'].apply(get_time)
def status_mission(mission):
    if mission == "Success":
        return 1
    if mission == 'Failure':
        return 0
    if mission== 'Partial Failure':
        return -1
    if mission == 'Prelaunch Failure':
        return -2
df['Status Mission'] = df['Status Mission'].apply(status_mission) 
df.info()
df.to_csv('cleaned.csv')
df.plot(x = 'Time', y = 'Status Mission', kind = 'scatter')
plt.show()