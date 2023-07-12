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

######################################

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
        
######################################

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
    
    beginingIndex = html.find(openingTag)
    
    if beginingIndex == -1:
        return 0
    
    endIndex = html.find(closingTag, beginingIndex)
    
    if endIndex == -1:
        return 0
    
    lastHTML = html[endIndex + len(closingTag):]
    return 1 + countTag(lastHTML, tag)

