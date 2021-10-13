
import pandas as pd
from pandas.core.frame import DataFrame


class BitratesCSV:
    def __init__(self, path) -> None:
        self.path = path
        self.bitates_df = pd.DataFrame(columns=["bitrate", "input_file", "rate_mode", "param"])
        self.compute()
        pass
    
    @property
    def get_df(self) -> DataFrame:
        return self.bitates_df
    
    def compute(self):
        bitrates_overview = pd.read_csv(f"{self.path}bitrates.csv", usecols=['filename', 'bitrate'])
        self.bitates_df = pd.DataFrame(columns=["bitrate", "input_file", "rate_mode", "param"])
        basename = bitrates_overview.filename.str.replace(".mp4", "", regex=False).str.replace("videos/", "", regex=False)
        self.bitates_df[['input_file', 'rate_mode', 'param']] = basename.str.split('-', expand=True)
        self.bitates_df.bitrate = bitrates_overview.bitrate.div(1000)
        self.bitates_df.index = self.bitates_df.index+1