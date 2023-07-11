######################################
# Mohammad Abdelkhalek Assignment 02 #
######################################

def displayMenu():
    print("1. Count Digits \n" +
          "2. Find Max \n" +
          "3. Count Tags \n" +
          "4. Exit")
    print("- " * 15, end="\n")
    print("Enter a choice: ")

##################################################################################

#Choice 1

def countDigits(integer):
    count = 0
    if integer < 10:
        return 1
    else:
        count = 1 + countDigits(integer // 10)
    return count      

##################################################################################

#Choice 2

def findMax(list1):    
    if len(list1) == 1:
        return list1[0]    
    else:
        max = findMax(list1[1:])
        if list1[0] > max:  
            return list1[0]
        else:
            return max

