######################################
# Mohammad Abdelkhalek Assignment 02 #
######################################

import sys

#Display Menu function

def displayMenu():
    print("1. Count Digits\n2. Find Max\n3. Count Tags\n4. Exit")
    print("- " * 15)

###########################################################

#Choice 1

def countDigits(integer):
    count = 0
    if integer < 10:
        return 1
    else:
        count = 1 + countDigits(integer // 10)
    return count

###########################################################

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
        
###########################################################

#Choice 3

HTMLCode = """
<html>
<head>
<title>My Website</title>
</head>
<body>
<h1>Welcome to my website!</h1>
<p>Here you'll find information about me and my hobbies.</p>
<h2>Hobbies</h2>
<ul>
<li>Playing guitar</li>
<li>Reading books</li>
<li>Traveling</li>
<li>Writing cool h1 tags</li>
</ul>
</body>
</html>"""

def countTag(html, tag):
    openingTag = "<{}>".format(tag)
    closingTag = "</{}>".format(tag)

    beginningIndex = html.find(openingTag)

    if beginningIndex == -1:
        return 0

    endingIndex = html.find(closingTag, beginningIndex)

    if endingIndex == -1:
        return 0

    lastHTML = html[endingIndex + len(closingTag):]
    return 1 + countTag(lastHTML, tag)

###########################################################

#Choice 4

def exitProgram():
    print("Exiting the program...")
    sys.exit(0)


###########################################################
#Main function

def main():
    while True:
        displayMenu()
        choice = input("Enter a choice: ")

        if choice == '1':
            integer = int(input("Enter an integer: "))
            print(countDigits(integer))
        elif choice == '2':
            list1 = input("Enter elements of the list separated by space: ")
            userList = list1.split()
            print(findMax(userList))
        elif choice == '3':
            tag = input("Enter the name of the HTML tag to find its occurrence: ")
            occurrences = countTag(HTMLCode, tag)
            print("Occurrences of <{}>: {}".format(tag, occurrences))
        elif choice == '4':
            exitProgram()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
    
###########################################################
