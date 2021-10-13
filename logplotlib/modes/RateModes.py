import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'
from pandas.core.frame import DataFrame

class RateModes:
    def __init__(self, left_join_df) -> None:
        self.rate_modes_df = left_join_df.loc[left_join_df['rate_mode'].isin(["2pass", "2passVbv", "abr", "abrVbv"])]
        self.compute()
        pass
    
    @property
    def get_df(self) -> DataFrame:
        return self.rate_modes_df

    def compute(self):
        self.rate_modes_df['target_bitrate'] = self.rate_modes_df["param"].str.replace("K", "")
        self.rate_modes_df.drop('param', axis=1, inplace=True)

        self.rate_modes_df = self.rate_modes_df.loc[self.rate_modes_df['target_bitrate'].isin(['3000', '7500'])]
        self.rate_modes_df.reset_index(inplace=True)
        self.rate_modes_df.index = self.rate_modes_df.index+1
        self.rate_modes_df.drop('index', axis=1, inplace=True)

        self.rate_modes_df['frame_index'] = pd.to_numeric(self.rate_modes_df['frame_index'], downcast="integer")
        self.rate_modes_df['size'] = pd.to_numeric(self.rate_modes_df['size'], downcast="integer")
        self.rate_modes_df['target_bitrate'] = pd.to_numeric(self.rate_modes_df['target_bitrate'], downcast="integer")
