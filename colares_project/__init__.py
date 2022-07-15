import pandas as pd
import numpy as np
from subprocess import Popen, PIPE
import sys
import pyarrow as pa
import pyarrow.parquet as pq


def downloadData():
    #define url to open (request csv file)
    url = "https://snirh.pt/snirh/_dadosbase/site/paraCSV/dados_csv.php?sites=920685260&pars=1436794570,1520200094&tmin=01/10/1965&tmax=10/03/2022&formato=csv"

    #open url calling curl from the command line
    get = Popen(['curl', '-k', url], stdout=PIPE)

    #read, decode and store the result in a variable
    result = get.stdout.read().decode('latin')

    return result


def cleanDownloadedData(downloaded):
    #clean the data
    #convert result into lines
    result_lines = downloaded.splitlines()

    #split each line at the commas
    result_lines_split = [i.split(',') for i in result_lines]

    #delete lines that do not represent actual data (eg. header and footer)
    final_result = [i for i in result_lines_split if len(i)==6]

    #conver to pandas dataframe
    final_result_df = pd.DataFrame(final_result)

    #make 1st row to be the header
    final_result_df = final_result_df.rename(columns=final_result_df.iloc[0]).drop(final_result_df.index[0])

    #replace empty values with np.nan
    final_result_df.replace('',np.nan, inplace=True)
    #remove columns that only contain empty values
    final_result_df.dropna(how='all',axis=1, inplace=True)

    #rename first column to 'Date'
    final_result_df.rename(columns={final_result_df.columns[0]: "Date", 
                                    final_result_df.columns[1]: "Precipitation",
                                    final_result_df.columns[2]: "Temperature"}, inplace = True)

    return final_result_df


def saveDownloadedAndCleanedData(path = "Export_test.csv"):
    if len(sys.argv) >= 2:
        path= sys.argv[1]
    cleanDownloadedData(downloadData()).to_csv(path)

def saveAsParquet(path = "Export_test.parquet"):
    if len(sys.argv) >= 2:
        path= sys.argv[1]
    df = cleanDownloadedData(downloadData())
    df_parquet = pa.Table.from_pandas(df)
    pq.write(df_parquet, path)

    