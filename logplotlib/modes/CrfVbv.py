import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'
from pandas.core.frame import DataFrame

class CrfVbv:
    def __init__(self, left_join_df) -> None:
        self.crf_vbv_df = left_join_df.loc[left_join_df['rate_mode']=='crfVbv']
        self.compute()
        pass
    
    @property
    def get_df(self) -> DataFrame:
        return self.crf_vbv_df

    def compute(self):
        self.crf_vbv_df[['param', 'target_bitrate']] = self.crf_vbv_df['param'].str.split('_', expand=True)
        self.crf_vbv_df['target_bitrate'] = self.crf_vbv_df['target_bitrate'].str.replace('K','', regex=False)

        self.crf_vbv_df = self.crf_vbv_df.loc[self.crf_vbv_df['param'].isin(['17', '23'])]

        self.crf_vbv_df['frame_index'] = pd.to_numeric(self.crf_vbv_df['frame_index'], downcast="integer")
        self.crf_vbv_df['size'] = pd.to_numeric(self.crf_vbv_df['size'], downcast="integer")
        self.crf_vbv_df['target_bitrate'] = pd.to_numeric(self.crf_vbv_df['target_bitrate'], downcast="integer")
