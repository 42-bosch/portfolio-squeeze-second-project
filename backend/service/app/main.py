from read_data import ExcelReader
from database import database

Test = ExcelReader(file_path="temp/clients.xlsx")
sheet_names = Test.get_sheet_names()
dataframes = Test.get_dataframes()

for i in range(len(sheet_names)):
    collection = database[sheet_names[i]]
    collection.insert_many(dataframes[i].to_dict(orient="records"))
