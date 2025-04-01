class DataProcessing:
    def __init__(self, extractor, saver, zip_creator):
        self.extractor = extractor
        self.saver = saver
        self.zip_creator = zip_creator

    def process(self, csv_file_name, zip_file_name):
        try:
            data = self.extractor.extract_data()
            self.saver.save(data, csv_file_name)
            self.zip_creator.create_zip(zip_file_name, csv_file_name)
            print("Processo concluído com sucesso!")
        except Exception as e:
            print(f"Erro durante a execução: {e}")