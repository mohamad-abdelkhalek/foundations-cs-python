######################################
# Mohammad Abdelkhalek Assignment 03 #
######################################

#Display Menu function

def displayMenu():
    print("1. Sum Tuples\n2. Export JSON\n3. Import JSON\n4. Exit")
    print("- " * 15)

##################################################################

#Choice 1

def sumTuples(tuple1, tuple2):
    lst = []
    for i in range(len(tuple1)):
        sum = tuple1[i] + tuple2[i]
        lst.append(sum)
    return tuple(lst)

##################################################################

#Choice 2

def exportJson(dictionary, name):
    resultJson = "{\n"
    
    for key, value in dictionary.items():
        jsonValue = '"' + value + '"' if isinstance(value, str) else str(value)
        resultJson += '  "' + key + '": ' + jsonValue + ',\n'
    
    resultJson = resultJson.rstrip(",\n") + "\n}"
    
    print(name, "=", resultJson)
    
##################################################################

#Choice 3

def importJson(file_name):
    data_list = []

    with open(file_name, 'r') as file:
        json_str = file.read()

    json_str = json_str.replace(" ", "").replace("\n", "")

    if not json_str:
        return data_list

    def find_next_object_start_index(start_index):
        stack = 0
        while start_index < len(json_str):
            if json_str[start_index] == '{':
                stack += 1
            elif json_str[start_index] == '}':
                stack -= 1

            if stack == 0:
                return start_index

            start_index += 1
        return -1

    index = 0
    while index < len(json_str):
        if json_str[index] == '{':
            next_object_index = find_next_object_start_index(index)
            if next_object_index != -1:
                json_object_str = json_str[index:next_object_index+1]
                data_list.append(eval(json_object_str))
                index = next_object_index + 1
            else:
                break
        else:
            index += 1

    return data_list

##################################################################

#Choice 4

def exitProgram():
    print("Exiting the program...")
    sys.exit(0)

