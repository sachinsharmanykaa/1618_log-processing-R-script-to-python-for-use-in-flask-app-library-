import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'
from pandas.core.frame import DataFrame

class QualityModes:
    def __init__(self, left_join_df) -> None:
        self.quality_modes_df = left_join_df.loc[left_join_df['rate_mode'].isin(['crf', 'qp'])]
        self.compute()
        pass
    
    @property
    def get_df(self) -> DataFrame:
        return self.quality_modes_df

    def compute(self):
        self.quality_modes_df = self.quality_modes_df.loc[self.quality_modes_df['param'].isin(['17', '23'])]
        self.quality_modes_df.reset_index(inplace=True)
        self.quality_modes_df.index = self.quality_modes_df.index+1
        self.quality_modes_df.drop('index', axis=1, inplace=True)

        self.quality_modes_df['frame_index'] = pd.to_numeric(self.quality_modes_df['frame_index'])
