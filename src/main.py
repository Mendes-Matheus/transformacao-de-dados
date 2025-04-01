from transform_data.data_extractor import PDFDataExtractor
from transform_data.data_saver import CSVDataSaver
from transform_data.zip_creator import ZipFileCreator
from transform_data.data_processing import DataProcessing
import os

# Definindo o diretório de dados
data_directory = 'data'
pdf_file_path = os.path.join(data_directory, 'Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf')
csv_file_name = os.path.join(data_directory, 'Anexo.csv')
zip_file_name = os.path.join(data_directory, 'Teste_Matheus_Mendes.zip')

# Instanciando as classes
pdf_extractor = PDFDataExtractor(pdf_file_path)
csv_saver = CSVDataSaver()
zip_creator = ZipFileCreator()

# Criando uma instância da classe de processamento de dados
data_processor = DataProcessing(pdf_extractor, csv_saver, zip_creator)

# Executando o processamento
if __name__ == "__main__":
    data_processor.process(csv_file_name, zip_file_name)