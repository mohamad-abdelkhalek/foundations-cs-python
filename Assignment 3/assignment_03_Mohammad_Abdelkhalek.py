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