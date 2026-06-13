# analysis
import csv 
import pandas as pd

df = pd.read_csv("RAW-DATA-bev570od5702.csv")

# printing out basic details to get an initial idea 
print(df.head())
print(df.shape)
print(df.dtypes)
print(df.columns)

# translating german columns to english 
eng_df = df.rename(columns={"EreignisDatJahr": "year", 
                    "QuarCd": "district_code", 
                    "QuarLang": "district_name", 
                    "AlterVMutterCd": "mother_age",
                    "SexCd": "child_sex",
                    "HerkunftCd": "child_origin",
                    "HerkunftMutterCd": "mother_origin",
                    "LebensfaehigkeitCd": "viability",
                    "AnzGebuWir": "births"})

# check for updates
print(eng_df.head())

# checking
print(eng_df["viability"].unique()) 
# the unique values are only 1, since this specific data set only looks at live births. 
# all cell entries under this column are J, which is german for ja, which means yes. 

eng_df = eng_df.drop(columns=["viability"])
print(eng_df)

# dictionary for columns 
#df['column'].map() 

#    for row in reader:
#        print(row)
