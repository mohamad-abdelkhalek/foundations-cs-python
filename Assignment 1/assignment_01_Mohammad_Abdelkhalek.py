######################################
# Mohammad Abdelkhalek Assignment 01 #
######################################

#Problem 1
def getFactorial(num):
    fact = 1
    if num < 0:
        print("Negative number!")
    else:
        for i in range(1,num+1):
            fact = fact * i
        print("The factorial of ", num, " is ", fact)

getFactorial(4)

##################################################################################

#Probelm 2
num = int(input("Enter an integer: "))

def getDivisors(num):
    divisors = []
    for i in range(1,num+1):
        if(num % i == 0):
         divisors.append(i)
    return divisors

print(getDivisors(num))

##################################################################################

#Problem 3
user_string = input("Enter a string to reverse: ")

def reverseString(user_string):
    reversed_string = ""
    for i in range(len(user_string) - 1, -1, -1):
        reversed_string += user_string[i]
    return reversed_string

print(reverseString(user_string))

##################################################################################

#Problem 4
input_numbers = input("Enter elements of the list separated by space: ")
user_list = input_numbers.split()
print(user_list)

def getEvenList(user_list):
    even_list = []
    for i in user_list:
        i = int(i)
        if (i % 2 == 0):
            even_list.append(i)
    return even_list
        
print(getEvenList(user_list))

##################################################################################

#Problem 5
#re.search() function that locates a match anywhere in the string, we should IMPORT it first to use it.
#reference: https://bit.ly/3PLb2ts

import re

def checkPassword(password):
    if (
        len(password) > 8
        and any(c.isupper() for c in password)
        and any(c.islower() for c in password)
        and any(c.isdigit() for c in password)
        and bool(re.search('[#$?!]', password))
    ):
        return "Strong Password"
    else:
        return "Weak Password"

psd = "Password$123"
print(checkPassword(psd))

##################################################################################

#Problem 6 - BONUS QUESTION
def isValidIpv4(address):
    octets = address.split(".")
    
    if len(octets) != 4:
        return False
    
    for octet in octets:
        if not octet.isdigit():
            return False
        
        if octet.startswith('0') and len(octet) > 1:
            return False
        
        if int(octet) < 0 or int(octet) > 255:
            return False
    
    return True

print(isValidIpv4("192.168.1.1"))

##################################################################################