import pandas as pd
from typing import List

class ExcelReader:
    def __init__(self, file_path, num_sheets=0):
        self.file_path = file_path
        self.num_sheets = num_sheets

        self.excel_file = self._open_excel_file()
        self.sheet_names = self.excel_file.sheet_names
        self.dataframes = self._read_dataframes()

    def _open_excel_file(self) -> pd.ExcelFile:
        try:
            return pd.ExcelFile(self.file_path)
        except FileNotFoundError:
            raise FileNotFoundError("File not found or path is incorrect.")

    def _read_dataframes(self) -> List[pd.DataFrame]:
        total_sheets = len(self.sheet_names)
        num_sheets_to_read = self.num_sheets
        dataframes : List[pd.DataFrame] = []

        if self.num_sheets == 0:
            num_sheets_to_read = total_sheets
        elif self.num_sheets > total_sheets:
            raise ValueError("The number of sheets to read is greater than the number of sheets in the file.")
        else:
            num_sheets_to_read = self.num_sheets

        for i in range(num_sheets_to_read):
            dataframe = pd.read_excel(self.excel_file, sheet_name=self.sheet_names[i])
            dataframes.append(dataframe)

        return dataframes

    def get_dataframes(self):
        return self.dataframes

    def read_sheet(self, sheet_name):
        return pd.read_excel(self.excel_file, sheet_name=sheet_name)

    def get_excel_file(self):
        return self.excel_file

    def get_dataframe(self, sheet_number):
        return self.dataframes[sheet_number]

    def get_sheet_names(self):
        return self.sheet_names
