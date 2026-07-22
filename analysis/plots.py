import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv('data/processed_data.csv')
os.makedirs('plots', exist_ok=True)

#1. G-G Diagram 
plt.figure(figsize=(8,6))
plt.scatter(df['Load_factor'],df['ROC_ftmin'])
plt.title('Load Factor vs Rate of Climb')
plt.xlabel('Load_Factor [n]')
plt.ylabel('Rate of Climb [ft/min]')
plt.grid(True)
plt.savefig('plots/gg_diagram.png')

#2. Speed vs Altitude
plt.figure(figsize=(8,6))
plt.plot(df['Alt_ft'],df['IAS_kts'], marker='o')
plt.title('Indicated Airspeed vs Altitude')
plt.xlabel('Altitude [ft]')
plt.ylabel('IAS [kts]')
plt.grid(True)
plt.savefig('plots/speed_altitude.png')

print("Plots saved to /plots folder")
