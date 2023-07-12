import pandas as pd

class ReadExcel:
    def __init__(self, path, sheets_amount=0):
        self.path = path
        self.sheets_amount = sheets_amount

        self._xls_file = self._open_excel_file()
        self._sheets = self._read_sheets()

    def _open_excel_file(self):
        try:
            return pd.ExcelFile(self.path)
        except FileNotFoundError:
            raise FileNotFoundError("File not found or path is incorrect.")

    def _read_sheets(self):
        sheet_names = self._xls_file.sheet_names
        sheets_amount_all = len(sheet_names)
        sheets_amount_to_read = self.sheets_amount
        dataframes = []

        if sheets_amount_to_read == 0:
            sheets_amount_to_read = sheets_amount_all
        elif sheets_amount_to_read > sheets_amount_all:
            raise ValueError(
                "The number of sheets to read is greater than the number of sheets in the file."
            )

        for i in range(sheets_amount_to_read):
            dataframe = pd.read_excel(self._xls_file, sheet_name=sheet_names[i])
            dataframes.append(dataframe)

        return dataframes

    def get_sheets(self):
        return self._sheets

    def get_sheet(self, sheet_number):
        return self._sheets[sheet_number]

