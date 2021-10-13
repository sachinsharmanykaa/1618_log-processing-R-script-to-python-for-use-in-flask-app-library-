
import pandas as pd
from pandas.core.frame import DataFrame
from utils.ReadCSV import ReadCSV

class CombinedCSV:
    def __init__(self, path) -> None:
        self.path = path
        self.combined_df = pd.DataFrame(columns=['pts', 'size', 'frame_type', 'input_file', 'rate_mode', 'param', 'frame_index'])
        self.compute()
        pass

    @property
    def get_df(self) -> DataFrame:
        return self.combined_df
    
    def compute(self):
        csv_files = ReadCSV(self.path).get_csv_files
        for csv_file in csv_files:
            df = pd.read_csv(csv_file)
            df.index = df.index+1
            df.rename(columns={'pts_time':'pts', 'type':'frame_type'}, inplace=True)
            file_name = csv_file.replace('.csv', '').replace('csv/','')
            input_file, rate_mode, param = file_name.split('-', 2)
            df['input_file'], df['rate_mode'], df['param'] = input_file, rate_mode, param
            df['frame_index'] = range(1, 1+len(df))
            df.drop('frame', axis=1, inplace=True)
            self.combined_df = pd.concat([self.combined_df, df], ignore_index=True, sort=False)
        self.combined_df.index = self.combined_df.index+1