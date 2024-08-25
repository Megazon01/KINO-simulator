import pandas as pd
import functions as fn

df = pd.DataFrame(
    {'Name':['James', 'Jen', 'Stamos', 'Sylian'],
     'Age':[22,34,55,83],
     'Gender':['m', 'f', 'm', 'o'],
     'Height': [174,188,165,157]}
)

print(df)

print(f"This is how you get Jen's data: {fn.get_Jens_data(df)}")

childrens_column = df['Age']/2
print(childrens_column)
#new_df = df("Children's age":[childrens_column])