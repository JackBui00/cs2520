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
    new_names_and_values_list = []
    for data in names_and_values_list:
        total = 0
        for x in range(1,4):
            try:
                total += int(data[x])
            except ValueError:
                try:
                    total += float(data[x])
                except ValueError:
                    total += 0
        average = round(total/3,2)
        data.append(average)
        new_names_and_values_list.append(data)

    names_and_values.close()

    print(new_names_and_values_list)

    new_file_average = open_file_write("scoresAve.txt")
    for data in new_names_and_values_list:
            for x in data:
                new_file_average.write(str(x) + " ")
            new_file_average.write("\n")
main()