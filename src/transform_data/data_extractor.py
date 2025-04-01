import os
import tabula
import pandas as pd

class IDataExtractor:
    def extract_data(self):
        pass

class PDFDataExtractor(IDataExtractor):
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def extract_data(self):
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"Arquivo '{self.file_path}' não encontrado.")
        
        self.data = tabula.read_pdf(self.file_path, pages='3-180', lattice=True)
        if not self.data:
            raise ValueError("Nenhum dado foi extraído da tabela.")
        
        self.data = pd.concat(self.data, ignore_index=True)
        self.data.columns = [col.replace("\r", " ") for col in self.data.columns]
        self.data = self.data.rename(columns={'OD': 'Seg. Odontologico', 'AMB': 'Seg. Ambulatorial'})
        return self.data