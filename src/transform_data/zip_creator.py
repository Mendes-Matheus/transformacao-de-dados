import os
import zipfile

class ZipFileCreator:
    def create_zip(self, zip_name, file_name):
        if os.path.exists(file_name):
            with zipfile.ZipFile(zip_name, 'w') as zp:
                zp.write(file_name, os.path.basename(file_name))
        else:
            raise FileNotFoundError("O arquivo não existe.")