from read_data import ExcelReader
from database import database

Data = ExcelReader(file_path="temp/clients.xlsx")
sheet_names = Data.get_sheet_names()
dataframes = Data.get_dataframes()

for i, sheet_name in enumerate(sheet_names):
    collection = database[sheet_name]
    if len(dataframes[i]) == 0:
        collection.insert_many(dataframes[i].to_dict(orient="records"))
        print(f"Successfully inserted {sheet_name}")
    else:
        print(f"Collection {sheet_name} already exists")
