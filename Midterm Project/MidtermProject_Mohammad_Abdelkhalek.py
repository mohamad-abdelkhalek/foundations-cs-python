# Project link on Replit: https://replit.com/join/bzokxuredl-mohammad-abdelkhalek

# Import sys module to use it to exit the program
import sys

# Import daytime module to get the current date
# reference: https://www.geeksforgeeks.org/python-datetime-module/
import datetime

# Function to import tickets from the text file into the list without user intervention
# Inspired from https://www.youtube.com/watch?v=hUyopAoOpG4
def importTicketsFile(path):
    ticketsList = []
    
    with open(path, 'r') as file:
        for line in file:
            item = line.strip().split(', ')
            
            ticket = {
                'ticketID': item[0],
                'eventID': item[1],
                'username': item[2],
                'timeStamp': item[3],
                'priority': int(item[4])
            }

            ticketsList.append(ticket)

    return ticketsList
        

# Function to display the Admin's menu
def displayAdminMenu():
     print("1. Display Statistics\n"
           "2. Book a Ticket\n"
           "3. Display all Tickets\n"
           "4. Change Ticket’s Priority\n"
           "5. Disable Ticket\n"
           "6. Run Events\n"
           "7. Exit")


# Function to display the normal user's menu
def displayUserMenu():
    print("1. Book a Ticket\n"
          "2. Exit")


# Function to show the event ID with the highest number of tickets    
# Inspired by: https://stackoverflow.com/questions/3496518/using-a-dictionary-to-count-the-items-in-a-list
def displayStatistics(ticketsList):
    # Initialize an empty dictionary to store the ticket counts
    ticketsCount = {}

    # Count the occurrences of the event ID in the list of tickets by looping through the list
    for ticket in ticketsList:
        eventID = ticket['eventID']
        if eventID in ticketsCount:
            ticketsCount[eventID] += 1
        else:
            ticketsCount[eventID] = 1

    # Find the event ID with the highest count
    highestCount = 0
    highestEvent = None
    for eventID, count in ticketsCount.items():
        if count > highestCount: # Compare the counts values
            highestCount = count
            highestEvent = eventID

    # Return the event ID with the highest count
    return highestEvent 
    

# Function to increment the ticket ID automatically
def autoIncrementID(ticketsList):
    if not ticketsList:
        return 'tick101' # Incase the ticket's list is empty start with ID tick101 as default

    lastTicketID = ticketsList[-1]['ticketID'] # Get the last ticket's ID from the ticket's list
    ticketNum = int(lastTicketID[4:]) + 1  # Increment the last ticket number by 1 for the new one
    newTicketID = f'tick{ticketNum:03d}' # create the new ticket ID using f-string formatting and assign it to newTicketID variable
    return newTicketID # Return the new ID

# Function to allow the admin to book a new ticket
def bookTicket(ticketsList):
    # Ask the admin to enter ticket information
    username = input("Enter username: ")
    eventID = input("Enter event ID: ")
    eventDate = input("Enter date of the event (YYYYMMDD): ")
    priority = int(input("Enter priority: "))

    # Generate auto-incremented ticket ID by autoIncrementID function
    ticketID = autoIncrementID(ticketsList)

    # Create a new ticket dictionary for the booked ticket
    newTicket = {
        'ticketID': ticketID,
        'eventID': eventID,
        'username': username,
        'timeStamp': eventDate,
        'priority': priority
    }

    # Append the new ticket to the list of tickets
    ticketsList.append(newTicket)

    print("A new ticket was booked successfully!")


# Function to show all tickets registered in the system, ordered by
# event’s date and event ID (Today, Tomorrow, etc.). Old tickets should not be shown.
def displayTickets(ticketsList):
    # Get the cuurent date using datetime module 
    # # reference: https://www.geeksforgeeks.org/python-datetime-module/
    today = datetime.datetime.now().strftime('%Y%m%d') 

    # Filter out old tickets (Remove tickets with a timeStamp earlier than the current date)
    freshTickets = [ticket for ticket in ticketsList
                    if ticket['timeStamp'] >= today]

    # Sort tickets by priority using merge sort algorithm function
    ticketsSorted = mergeSort(freshTickets)

    # Display the tickets info
    for ticket in ticketsSorted:
        print(f"{ticket['ticketID']}, {ticket['eventID']}, "
              f"{ticket['username']}, {ticket['timeStamp']}, {ticket['priority']}")


# Function to allow the admin to change the priority of a ticket
def changePriority(ticketsList, ticketID, newPriority):
    # First we set the foundTicket flag to false (by default)
    foundTicket = False

    # Search for the ticket with the ID entered by the admin by looping through the tickets list
    for ticket in ticketsList:
        if ticket['ticketID'] == ticketID:
            ticket['priority'] = newPriority
            # Set the foundTicket flag to true (ticket was found in the list)
            foundTicket = True

    # Display the appropriate message
    if foundTicket:
        print(f"Priority of {ticketID} changed to {newPriority}")
    else:
        print(f"Ticket {ticketID} not found")



# Function to allow the admin to remove a ticket from the system by providing the ticket ID. 
def disableTicket(ticketsList, ticketID):
    ticketRemoved = [ticket for ticket in ticketsList # Search for the ticket id in the ticket's list by looping through it
                     if ticket['ticketID'] == ticketID]

    if ticketRemoved:
        # Remove the ticket from the list
        ticketsList.remove(ticketRemoved[0])
        print(f"Ticket with ID {ticketID} has been removed.")
    else:
        print(f"Ticket with ID {ticketID} not found.")


# Function to return the priority of a ticket to be compared
def comparePriority(ticket):
    return ticket['priority']


# Merge Sort Algorithm function
def mergeSort(tickets):
    if len(tickets) <= 1:
        return tickets

    mid = len(tickets) // 2
    leftHalf = tickets[:mid]
    rightHalf = tickets[mid:]

    leftHalf = mergeSort(leftHalf)
    rightHalf = mergeSort(rightHalf)

    return merge(leftHalf, rightHalf)

# Merge of two sorted sublists function
def merge(left, right):
    result = []
    leftIndex, rightIndex = 0, 0

    while leftIndex < len(left) and rightIndex < len(right):
        if comparePriority(left[leftIndex]) <= comparePriority(right[rightIndex]):
            result.append(left[leftIndex])
            leftIndex += 1
        else:
            result.append(right[rightIndex])
            rightIndex += 1

    result.extend(left[leftIndex:])
    result.extend(right[rightIndex:])
    return result


# Function to allow the admin to remove a ticket from the system by providing the ticket ID.
def runEvents(ticketsList):
    today = datetime.date.today().strftime('%Y%m%d')

    # Filter tickets with today's date
    todayEvents = [ticket for ticket in ticketsList
                   if ticket['timeStamp'] == today]

    # if no events today
    if not todayEvents:
        print("No events today!")
        return

    # Sort today's tickets by priority using Merge Sort algorithm function
    todayEvents = mergeSort(todayEvents)

    # Display today's events
    for ticket in todayEvents:
        print(f"Todays events: {ticket['eventID']}")

    # Remove today's events from the list
    for ticket in todayEvents:
        ticketsList.remove(ticket)
    print("Todays events removed from the list")        
  

def userBookTicket(ticketsList, username):
    # Ask the user for the ID and date of the event
    eventID = input("Enter the event ID: ")
    eventDate = input("Enter the date of the event (YYYYMMDD): ")

    # Setting default priority to 0
    priority = 0

    # Generate a new ticket ID by autoIncrementID function
    newTicketID = autoIncrementID(ticketsList)

    # Create the new ticket dictionary
    newUserTicket = {
        'ticketID': newTicketID,
        'eventID': eventID,
        'username': username,
        'timeStamp': eventDate,
        'priority': priority
    }

    # Append the new ticket dictionary to the list of tickets
    ticketsList.append(newUserTicket)

    print("A new ticket was booked successfully!")
    print(f"By the username: {username}, in: {eventDate}")
    
    

# reference: https://www.pythontutorial.net/python-basics/python-write-text-file/
def saveNewTickets(ticketsList):
    with open("tickets.txt", "w") as file:
        for ticket in ticketsList:
            newTicket = f"{ticket['ticketID']}, {ticket['eventID']}, {ticket['username']}, {ticket['timeStamp']}, {ticket['priority']}\n"
            file.write(newTicket)
     
# Function to exit the program
def exitProgram():
    print("Thank you for using our program :)")
    # Exit the program using sys module
    # reference: https://www.scaler.com/topics/exit-in-python/
    sys.exit(0)


# Main Function - Program start        
def main():
    # First we import the tickets (in the form of list of dictionaries) from the text file and assign it to tickets variable
    tickets = importTicketsFile('tickets.txt')
    # print(tickets)

    # Intialize count variable to count the login attempts
    count = 0

    while True:
        print("Welcome to Corrupted Ticketing System :)")
        print("----------------------------------------")
        username = input("Enter Username: ") # Ask for the username
        password = input("Enter Password: ") # Ask for the password

        if username == "admin" and password == "admin123123":
            # Reset the counter to zero if the admin successfully logged in
            count = 0
            # while true loop to make the menu displayed again after each option
            while True:
                displayAdminMenu()
                option = input("Choose an option: ")

                if option == '1':
                    print("The event ID with the highest number of tickets:", displayStatistics(tickets))
                    print("-" * 55) # I have used printing of dashes to make the output comfortable to look at
                    
                elif option == '2':
                    bookTicket(tickets)
                    print("-" * 55)
                    
                elif option == '3':
                    displayTickets(tickets)
                    print("-" * 55)
                    
                elif option == '4':
                    ticketID = input("Enter ticket ID to change its priority: ")
                    priority = input("Enter new priority: ")
                    changePriority(tickets, ticketID, priority)
                    print("-" * 55)
                    
                elif option == '5':
                    ticketID = input("Enter ticket ID to remove it from the system: ")
                    disableTicket(tickets, ticketID)
                    print("-" * 55)
                    
                elif option == '6':
                    runEvents(tickets)
                    
                elif option == '7':
                    exitProgram()
                    
                else:
                    print("Invalid option. Please try again.")
        
        # If the username was anything and password was empty            
        elif username != "":
            print("Welcome", username)
            while True:
                displayUserMenu()
                option = input("Choose an option: ")

                if option == '1':
                    userBookTicket(tickets, username)
                    print("-" * 30)
                elif option == '2':
                    saveNewTickets(tickets)
                    print("Saving...")
                    exitProgram() # Exit the program
                else:
                    print("Invalid option. Please try again.")
        else:
            print("Incorrect Username and/or Password")
            count += 1 # Increment the counter by one attempt

        if count > 5:
            print("You have reached the maximum attempts!")
            exitProgram()  # Exit the program

# To ensure the run of the proram main function as a script (A good habit)       
if __name__ == "__main__":
    main()