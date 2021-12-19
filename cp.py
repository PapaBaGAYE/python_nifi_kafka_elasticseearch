import pandas as pd

df = pd.read_csv('c:/Users/Papa Ba GAYE/Desktop/airline.csv')
# print(df)

# print(df[df['CarrierDelay'] == 2000]['Year'].sum())
print("- ", df[df['Year'] == 2000]['CarrierDelay'])
print("- ", df[df['CarrierDelay'] == 2000]['Year'].sum())
print(df.CarrierDelay)