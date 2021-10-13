from skmisc.loess import loess
from plotnine import *

input_file_mapping = {
        'BigBuckBunny0': "BBB 1",
        'BigBuckBunny120': "BBB 2",
        'BigBuckBunny240': "BBB 3",
        'TearsOfSteel10': "ToS 1",
        'TearsOfSteel120': "ToS 2",
        'TearsOfSteel240': "ToS 3"
        }

class Graph:
    def __init__(self) -> None:
        pass
    
    @classmethod
    def run(self, data, save_name, input_file):
        (
            ggplot(data, aes(x = 'frame_index', y = 'size', color = 'rate_mode'))
            + geom_smooth(method = "loess", se = False)
        #     + scale_color_discrete(
        #         "Rate Control Mode",
        #         breaks = ["2pass", "2passVbv", "abr", "abrVbv"],
        #         labels = ["2-pass", "2-pass + VBV", "ABR", "ABR + VBV"]
        #     )
            + facet_grid(f'input_file~{input_file}', labeller = labeller(
                input_file = input_file_mapping
            ))
            + xlab("Frame Index")
            + ylab("Frame Size") 
        #     + theme(legend.position = "bottom")
        ).save(filename = save_name, width = 8, height = 10, dpi = 100)