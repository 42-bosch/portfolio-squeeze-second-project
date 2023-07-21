from read_data import ExcelReader
from database import database
from pprint import pprint

class ExcelToDatabase:
    def __init__(self, file_path):
        self.data = ExcelReader(file_path=file_path)
        self.sheet_names = self.data.get_sheet_names()
        self.dataframes = self.data.get_dataframes()
        self.coluns = ["YEAR", "MODEL", "MARKET"]

    def import_to_database(self):
        collection = database["cars"]
        for i, sheet_name in enumerate(self.sheet_names):
            field = collection[sheet_name]
            df_without_titles = self.dataframes[i].iloc[1:]
            filtered_dataframe = df_without_titles[["YEAR", "MODEL", "MARKET"]]
            field.insert_many(filtered_dataframe.to_dict(orient="records"))

    def print_database(self, max: int = 1):
        for i in range(max):
            df_without_titles = self.dataframes[i].iloc[1:]
            filtered_dataframe = df_without_titles[["YEAR", "MODEL", "MARKET"]]
            pprint(filtered_dataframe)
