import pandas as pd


def get_Jens_data(df:pd.DataFrame) -> pd.DataFrame:
    result = df.loc[df['Name'] == 'Jen', ['Name', 'Age']]
    return(result)

def create_column(col_name, col_values, df):
    df[col_name] = col_values
    return df

def create_txt_files(location):
    with open(location, 'w') as file:
        file.writelines('[]')
    print(f"File created in location: {location}")

### Generate file locations.
x = 6

while x < 13:
    create_txt_files(f"KINO_{x}_results.txt")
    x=x+1