#Name: Jack Bui 

#Lab 5 – Task 1


def open_file_read(file_name):
    target = open(file_name, 'r')
    return target

def open_file_write(file_name):
    target = open(file_name, 'w')
    return target

def open_file_append(file_name):
    target = open(file_name, 'a')
    return target

def main():
    names_and_values_list = []
    names_and_values = open_file_read("scores.txt")
    for line in names_and_values:
        names_and_values_list.append(line.split())
    print(names_and_values_list)
    

main()