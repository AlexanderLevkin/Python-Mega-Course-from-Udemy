import glob

myfiles = glob.glob('files/*.txt')
for filepath in myfiles:
    with open(filepath, 'r') as file_local:
        print(file_local.readlines())
