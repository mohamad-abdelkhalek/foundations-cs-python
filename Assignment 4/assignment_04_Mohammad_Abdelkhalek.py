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

    def __init__(self, vertices):
        self.adj_list = {}
        self.vertices = vertices

        for vertex in range(vertices):
            self.adj_list[vertex] = []

    def addEdge(self, u, v):
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)
        
        
    def addUser(self, username):
        if username in self.adj_list:
            print(f"Username '{username}' is already taken. Please choose another username")
        else:
            self.adj_list[username] = []
            print(f"User '{username}' has been added to the platform.")
    
    
    def removeUser(self, username):
        if username in self.adj_list:
            for w in self.adj_list[username]:
                self.adj_list[w].remove(username)
            del self.adj_list[username]
            print(f"User '{username}' has been removed from the platform with their connections")
        else:
            print(f"Username '{username}' does not exist in the platform. Please make sure of the username.")
            
            
    def DFS(self, v):
        visited = [False] * self.vertices
        stack = [v]

        while False in visited:
            if not stack:
                for i in range(self.vertices):
                    if not visited[i]:
                        stack.append(i)

            else:
                v = stack.pop()
                if not visited[v]:
                    visited[v] = True
                    print(v, end=' ')
                    for w in self.adj_list[v]:
                        if not visited[w]:
                            stack.append(w)