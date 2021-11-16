from pyarrow import csv
import numpy as np
import pandas as pd

def cleaning(x):
    if str(x).isdigit() :
        return x
    return 0
def convert(x):
    try:
        return x.astype(np.int64)
    except:
        return x

opts = csv.ConvertOptions(strings_can_be_null = False,null_values={""," "," ","#N/A", "#N/A N/A", "#NA",     "-1.#IND", "-1.#QNAN", 
                        "-NaN", "-nan", "1.#IND",   "1.#QNAN", "N/A",     "NA", 
                        "NULL", "NaN",  "n/a",      "nan",     "null"})
#c_df = csv.read_csv('C:/FTC_downloads/20001002/2021-06-29/battlefield_relic_detail_log.csv')
c_df = csv.read_csv('C:/FTC_downloads/battlefield_relic_detail_log.csv')
#print(c_df)
#print(c_df.column ('param3').null_count)
df = c_df.to_pandas()
#df = df.fillna(0)
#df = df.fillna(0)
print("===="*30)
print(df.info())

  
#df['param3']=df['param3'].apply(cleaning)
#df = df.astype({'param3':np.str})
#df['param3'] = df['param3'].apply(pd.to_numeric)
print("===="*30)
df['param3'] = df['param3'].fillna(-19876543210)
print(df['param3'] )
print("===="*30)
df = df.astype({'param3':np.int64})
print(df['param3'] )
print("===="*30)
df = df.astype({'param3':'object'})
df.loc[(df['param3'] ==-19876543210),'param3' ] =''
#df[(df['param3'] == -19876543210)] = ''
print("===="*30)
print(df['param3'] )
#print(df][.astype('int32'))
#print(df][.astype('int32'))

df.to_csv('C:/FTC_downloads/test22.csv',index=False, sep='\t')
#print(df['param11'].astype('int64'))
