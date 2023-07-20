from read_data import ExcelReader
from database import database


class ExcelToDatabase:
    def __init__(self, file_path):
        self.data = ExcelReader(file_path=file_path)
        self.sheet_names = self.data.get_sheet_names()
        self.dataframes = self.data.get_dataframes()


    def import_to_database(self):
        for i, sheet_name in enumerate(self.sheet_names):
            collection = database[sheet_name]
            collection.cars.insert_many(self.dataframes[i].to_dict(orient="records"))
            print(f"Successfully inserted {sheet_name}")

