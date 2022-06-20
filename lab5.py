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
    names_and_values = []
    scores = open_file_read("scores.txt")
    for line in scores:
        names_and_values.append(line.split())
    print(names_and_values)


main()