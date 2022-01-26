from edi_835_parser import parse
import os

# path = 'input'
#
# for file in os.listdir(path):
#     if file.endswith('.txt'):
#         file_path = f'{path}/{file}'
#         transaction_set = parse(file_path)
#         data = transaction_set.to_dataframe()
#         data.to_csv(f'output/{file}')

path = 'input/quadax_sample_835.txt'

transaction_set = parse(path)

data = transaction_set.to_dataframe()
data.to_csv("output/quadax_sample_835.txt")
