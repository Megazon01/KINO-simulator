import pandas as pd


def get_Jens_data(df:pd.DataFrame) -> pd.DataFrame:
    result = df.loc[df['Name'] == 'Jen', ['Name', 'Age']]
    return(result)