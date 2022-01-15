
def file_reader(file_name):
    for row in open(file_name, "r"):
        yield row

for f in file_reader('../Solidity/Storage.json'):
    print(f)