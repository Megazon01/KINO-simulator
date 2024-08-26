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



fn.create_column('Car Brand', ['Mazda', 'Ferrari', 'BMW', 'Mercedes'], df)
print(df)



while True:
    inp = input("Enter Client's name: ")
    if inp in df.Name.tolist():
        client = df.loc[df['Name'] == inp]
        print(client.to_string(index=False))
    elif inp == 'n':
        break
    else:
        print('Invalid Input')


#new_df = df("Children's age":[childrens_column])