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

path = 'input/sample_835.txt'

transaction_set = parse(path)

data1, data2 = transaction_set.to_dataframe()
data1.to_csv("output/sample_remits_835.txt")

data2.to_csv("output/sample_payers_835.txt")


