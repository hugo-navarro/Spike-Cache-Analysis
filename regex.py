import re
import pandas as pd
import matplotlib.pyplot as plt

def txt_filter(index):
    with open("cache_configs_efficiancy_data.txt") as data_file:
        #*flop é um acrônimo que significa FLoating-point Operations Per Second
        data = {
            "Cache Total Size": [],
            "Gflops/s": [],
            "DCache miss rate": [],
            "ICache miss rate": []
        }

        data_lines = data_file.read()

        for config in index:
            elements = config.split(":")

            cache_size = int(elements[0]) * int(elements[1]) * int(elements[2])
            data["Cache Total Size"].append(cache_size)

        rates_pattern = r'\d+(?:\.\d+)?%'
        rates_matches = re.findall(rates_pattern, data_lines, re.MULTILINE)

        for dmisses, imisses in zip(rates_matches[0::2]\
                                    , rates_matches[1::2]):
            data["DCache miss rate"].append(dmisses)
            data["ICache miss rate"].append(imisses)

        gflops_pattern = r'400,\s*(\d+(?:\.\d+)?)'
        gflops_matches = re.findall(gflops_pattern, data_lines)

        for gflops in gflops_matches:
            data["Gflops/s"].append(gflops)

        df = pd.DataFrame(data, index=index)\
        .sort_values(by=['DCache miss rate'], ascending=True)

        print(df)

        df.plot(x="Cache Total Size", y="DCache miss rate",\
                 kind='scatter')
        plt.show()
            
def main():
    sets = ["1024", "2048", "4096"]
    ways = ["8", "4", "2"]
    block_sizes = ["32", "16", "8"]
    index_lines = []

    for set in sets:
        for way in ways:
            for block_size in block_sizes:
                index_line = (f'{way}:{set}:{block_size}') 
                index_lines.append(index_line)

    txt_filter(index_lines)

if __name__ == '__main__':  
    main() 
    