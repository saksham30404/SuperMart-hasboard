import pandas as pd

csv_file = 'SampleSuperstore.csv' 

df = pd.read_csv(csv_file)

excel_file = 'data_converted.xlsx'  
df.to_excel(excel_file, index=False)

print(f"Excel file saved as '{excel_file}'")
