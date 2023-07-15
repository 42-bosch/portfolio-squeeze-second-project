from read_data import ReadExcel
from pymongo import MongoClient

Clients = ReadExcel("~/Desktop/labs/second_challenge/backend/service/temp/clients.xlsx")

print(Clients.get_sheets())