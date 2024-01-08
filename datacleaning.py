import pandas as pd
df = pd.read_csv('partialclean.csv')

df.drop_duplicates(inplace=True)

df['coll'] = df['coll'].str.replace(r'(?i)phd', 'Ph.D', regex=True)
df['coll'] = df['coll'].str.replace(r'\d+', '', regex=True)

df['age'] = df['age'].str.replace(r'\D', '', regex=True)

for index, row in df.iterrows():
    if str(row['gender']).isdigit():
        numeric_value = row['gender']
        df.at[index, 'gender'] = df.at[index - 1, 'gender']
        df.at[index - 1, 'gender'] = numeric_value
        
col_num = df.select_dtypes(include=['number']).columns
df[col_num] = df[col_num].fillna(df[col_num].mean())
col_without_num = df.select_dtypes(exclude=['number']).columns
df[col_without_num] = df[col_without_num].fillna("Unknown")


df.to_csv("cleanedasg7.csv", index=False)
