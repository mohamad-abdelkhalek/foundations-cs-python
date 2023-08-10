######################################
# Mohammad Abdelkhalek Assignment 04 #
######################################



def displayMenu():
    print("1. Add a user to the platform\n"
          "2. Remove a user from the platform\n"
          "3. Send a friend request to another user\n"
          "4. Remove a friend from your list\n"
          "5. View your list of friends\n"
          "6. View the list of users on the platform\n"
          "7. Exit")


class Graph:
    
    def __init__(self):
        self.adj_list = {}

    def addEdge(self, u, v):
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    # Choice 1
    def addUser(self, username):
        if username in self.adj_list:
            print(f"Username '{username}' is already taken. Please choose another username.")
        else:
            self.adj_list[username] = []
            print(f"User '{username}' has been added to the platform.")

    # Choice 2
    def removeUser(self, username):
        if username in self.adj_list:
            for w in self.adj_list[username]:
                self.adj_list[w].remove(username)
            del self.adj_list[username]
            print(f"User '{username}' has been removed from the platform with their connections.")
        else:
            print(f"Username '{username}' does not exist in the platform. Please make sure of the username.")

    # Choice 3
    def addConnection(self, user1, user2):
        if user1 in self.adj_list and user2 in self.adj_list:
            self.addEdge(user1, user2)
            print(f"Connection added between '{user1}' and '{user2}'.")
        else:
            print("Both users must be in the platform to add a connection between them.")

    # Choice 4
    def removeConnection(self, user1, user2):
        if user1 in self.adj_list and user2 in self.adj_list:
            if user2 in self.adj_list[user1]:
                self.adj_list[user1].remove(user2)
                self.adj_list[user2].remove(user1)
                print(f"Connection between '{user1}' and '{user2}' has been removed.")
            else:
                print(f"There is no connection between '{user1}' and '{user2}'.")
        else:
            print("Both users must exist in the platform to remove a connection.")

    # Choice 5
    def friendsWith(self, username):
        if username in self.adj_list:
            return self.adj_list[username]
        else:
            print(f"Username '{username}' does not exist in the platform. Please make sure of the username.")
            return []

    # Choice 6
    def printAllUsers(self):
        print("Registered Users:")
        for user in self.adj_list:
            print(user)

    def DFS(self, vertex, visited=None):
        if visited is None:
            visited = set()
        visited.add(vertex)
        print(vertex, end=" ")

        for w in self.adj_list.get(vertex, []):
            if w not in visited:
                self.DFS(w, visited)


# Choice 7
def exitProgram():
    print("Exiting the program...")
    sys.exit(0)
                                   

def main():
    
    platform = Graph()
    
    while True:
        displayMenu()
        print("- " * 15)
        choice = input("Enter a choice: ")
        
        if choice == '1':
            username = input("Enter username to add to the platform: ")
            platform.addUser(username)
            
        elif choice == '2':
            username = input("Enter username to remove it from the platform: ")
            platform.removeUser(username)
            
            
        elif choice == '3':
            user1 = input("Enter first user: ")
            user2 = input("Enter second user to add connection with first user: ")
            platform.addConnection(user1, user2)
            
        elif choice == '4':
            user1 = input("Enter first user to remove connection: ")
            user2 = input("Enter second user to remove connection with first user: ")
            platform.removeConnection(user1, user2)
            
        elif choice == '5':
            username = input("Enter a username to list all the users who are currently friends with: ")
            print(platform.friendsWith(username))
            
        elif choice == '6':
            platform.printAllUsers()
        
        elif choice == '7':
            exitProgram()
               
        else:
            print("Invalid input! Please try again")

    
main()