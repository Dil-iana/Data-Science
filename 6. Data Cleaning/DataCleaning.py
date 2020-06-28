import pandas as pd
import numpy as np
import io
import requests

#Import csv-Datei
url = "https://raw.githubusercontent.com/edlich/eternalrepo/master/DS-WAHLFACH/dsm-beuth-edl-demodata-dirty.csv"
s = requests.get(url).content
df = pd.read_csv(io.StringIO(s.decode('utf-8')))
print(df)

#NaNs in der Spalte 'gender' durch 'male' erstetzen
df["gender"].fillna( value = 'Male', inplace = True)
print(df)

#Löschen alle Zeilen, die NaN enthalten
df.dropna(inplace=True)
print(df)

#Werte ersetzen
df.replace(to_replace='-78', value = '78', inplace= True)
print(df)

#Duplikate löschen
df.drop_duplicates(['full_name'], inplace=True)
print(df)

#Werte ersetzen
df.replace(to_replace=17.0, value = 16, inplace= True)
df.replace(to_replace=19.0, value=17, inplace=True)
df.replace(to_replace=20.0, value=18, inplace=True)
print(df)
# Age
# Check if there is a number or other things
c = 0
for row in df['age']:
    try:
        int(row)
        # Check if Age is older than 0
        if (int(row) < 0):
            df.loc[c, 'age'] = np.nan
    except ValueError:
        # If no number change to NaN
        df.loc[c, 'age'] = np.nan
        pass

    c += 1

# Age (Missing Age => old and minus Age)
# Fill the NaN with the Median in the age column
df['age'] = df['age'].fillna(int(df['age'].median()))
print(df)
