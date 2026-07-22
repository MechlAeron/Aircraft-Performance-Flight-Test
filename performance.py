import pandas as pd
import numpy as np

def calc_load_factor(bank_angle_deg):
  phi_rad=
  np.radians(bank_angle_deg)
  return 1 / np.cos(phi_rad)

def calc-climb_rate(alt_ft, time_s):
roc = np.gradient(alt_ft, time_s)
*60
return roc

df = pd.read_csv('data/sample_flight_data.csv')
df['Load_Factor']= calc_load_factor(df['Bank_deg'])
df['ROC_ftmin']= calc_climb_rate(df['Alt_ft'],df['time_s'])
print(df.head())
df.to_csv('data/processed_data.csv',index=False)
