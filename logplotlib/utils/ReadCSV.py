import glob
import os

class ReadCSV:    
    def __init__(self, path):
        self.path = path
        self._csv_files = glob.glob(os.path.join(f'{self.path}csv', "*.csv"))

    @property
    def get_csv_files(self):
        return self._csv_files
