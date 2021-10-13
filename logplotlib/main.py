import pandas as pd

from preprocess.CombinedCSV import CombinedCSV
from preprocess.BitratesCSV import BitratesCSV

from modes.RateModes import RateModes
from modes.QualityModes import QualityModes
from modes.CrfVbv import CrfVbv

from utils.Graph import Graph

graphs_dir = 'graphs'

# Preprocess csv files
combined_csv_df = CombinedCSV(path='').get_df

# Preprocess bitrates.py file
bitrates_df = BitratesCSV(path='').get_df


# apply left join between d and combined_df
left_join_df = pd.merge(bitrates_df, combined_csv_df, how='left')
left_join_df.index = left_join_df.index+1


# Preprocess as per modes and generate graphs
rate_modes_df = RateModes(left_join_df).get_df
Graph.run(data=rate_modes_df, save_name = f'{graphs_dir}/rate_modes.png', input_file = 'target_bitrate')

quality_modes_df = QualityModes(left_join_df).get_df
Graph.run(data=quality_modes_df, save_name = f'{graphs_dir}/quality_modes.png', input_file = 'param')

crf_vbv_df = CrfVbv(left_join_df).get_df
Graph.run(data=crf_vbv_df, save_name = f'{graphs_dir}/crf_vbv.png', input_file = 'param')