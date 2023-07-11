######################################
# Mohammad Abdelkhalek Assignment 02 #
######################################

"""def displayMenu():
    print("1. Count Digits \n" +
          "2. Find Max \n" +
          "3. Count Tags \n" +
          "4. Exit")
    print("- " * 15, end="\n")
    print("Enter a choice: ")"""
    
#displayMenu()

######################################

#Choice 1

def countDigits(integer):
    count = 0
    if integer < 10:
        return 1
    else:
        count = 1 + countDigits(integer // 10)
    return count
       
print(countDigits(252))