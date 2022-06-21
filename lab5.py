#Name: Jack Bui 

#Lab 5 – Task 1

#open to read 
def open_file_read(file_name):
    target = open(file_name, 'r')
    return target

#open to write 
def open_file_write(file_name):
    target = open(file_name, 'w')
    return target

#open to append 
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
    for data in names_and_values_list: #iterate through list for the list 
        total = 0
        for x in range(1,4): #interate through the inside list 
            try:
                total += int(data[x]) 
            except ValueError:  #error check for int value, then float, then set value as 0 
                try:
                    total += float(data[x]) 
                except ValueError:
                    total += 0
        average = round(total/3,2)
        data.append(average)
        new_names_and_values_list.append(data)
    
    names_and_values.close()   #close to reopen to overwrite old data 

    print(new_names_and_values_list)

    new_file_average = open_file_write("scoresAve.txt")
    for data in new_names_and_values_list:
            for x in data:
                new_file_average.write(str(x) + " ")
            new_file_average.write("\n")
#main()


#Lab 5 – Task 2

def main2():
    new_values = []
    user_file = input("Enter a file name: ")
    try:
        target_file = open_file_read(user_file)
    except FileNotFoundError:
        print("File is not found")
    
    for lines in target_file:
        try:
            float(lines)    #check if value is float 
        except ValueError:
            continue
        new_values.append(float(lines.rstrip()))    #append to list that will be calculated for min max mean 
    print(len(new_values))
    target_file.close()     #close to open to append to end of data set 
    target_file =open_file_append(user_file)

    max_value = max(new_values)
    min_value = min(new_values)         #calculations for min, max mean 
    average_value = round(sum(new_values)/len(new_values), 3)
    
    target_file.write("Max value: " + str(max_value) + "\n")
    target_file.write("Min value: " + str(min_value) + "\n")    #append to end the min max mean 
    target_file.write("Average value: " + str(average_value) + "\n")
main2()