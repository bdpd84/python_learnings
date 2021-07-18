file_name='readme.txt'

with open(file_name) as file_obj:
    print(file_obj.read())

with open(file_name) as file_obj:
    for line in file_obj:
        print(line.rstrip())

with open(file_name) as file_obj:
    lines = file_obj.readlines()
    for line in lines:
        print(line.rstrip())
