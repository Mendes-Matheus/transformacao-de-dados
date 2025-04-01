import pandas as pd

class IDataSaver:
    def save(self, data, file_name):
        pass

class CSVDataSaver(IDataSaver):
    def save(self, data, file_name):
        data.to_csv(file_name, index=False, encoding='utf-8-sig')