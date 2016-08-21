# Code solution to Question 1

def question1(s,t):
    # make the elements in both s and t lowercase.
    s = s.lower()
    t = t.lower()
    
    # if the substring is empty, return True
    if t == '':
        return True
    l = len(t)
    for i in range(len(s)):
        if sorted(s[i:(i+l)]) == sorted(t):
            return True
    
    return False


a = ''
b = ''
c = 'abc'
d = ''
e = 'udacity'
f = 'tic'
g = 'udacity'
h = 'yud'
i = 'caud'
j = 'uat'
k = 'uddddda'

#Should return True
print question1(a,b)
#Should return True
print question1(c,d)
#Should return True
print question1(e,f)
#Should return False
print question1(g,h)
#Should return True
print question1(g,i)
#Should return False
print question1(g,j)
#Should return False
print question1(g,k)




#Code solution for question 2

def question2(s):
    #initialize largest palindrome substring
    lp = ''
    #empty string and one character string cases
    if len(s) < 2:
        return s
    
    for i in range(len(s)):
        for j in range(i+1,len(s)-1):
            #If the string is palindronic and has more characters than
            #the lp, it becomes the lp.
            if s[i:j] == s[i:j][::-1] and len(s[i:j]) > len(lp):
                lp = s[i:j]

    
    return lp

a = ''
b = 'a'
c = 'abcdefg'
d = 'abacccdcd'

#Should return ''
print question2(a)
#Should return a
print question2(b)
#Should return 'a'
print question2(c)
#Should return 'aba'
print question2(d)



#Code solution for question 3
#I had a lot of trouble with this one. Any feedback would be greatly appreciated!


def sortbyweight(graph):
    #Make a list of edges based on weights in ascending order
    edge_list = []
    for node1 in graph:
        for i in range(len(graph[node1])):
            edge = sorted([node1, graph[node1][i][0], graph[node1][i][1]])
            if edge not in edge_list:
                edge_list.append(edge)
    edge_list = sorted(edge_list)

    return edge_list

def cyclic(graph):
    #check to see if the graph with the added edge forms a cycle.
    #Make a dict with keys as nodes and values as sets of the nodes it's connected to.
    nodes = []
    g = {}
    for node in graph:
        nodes.append(node)
        for i in range(len(graph[node])): 
            g[node] = set(graph[node][i][0]) 
    
    def dfs(graph, start):
        visited, stack = set(), [start]
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                stack.extend(graph[vertex] - visited)
        return(len(visited) == len(nodes))
    
    
    dfs(g, nodes[0])
    
def question3(graph):
    #Sort edges by weight
    edge_list = sortbyweight(graph)
    N = len(edge_list)
    edge_count = 0
    #Initialize an empty minimum spanning tree graph
    mst = {}
    for node in graph:
        mst[node] = []
    
    
    #If # of edges in mst == N-1, stop loop        
    while edge_count < N-1:
        #Add the lowest weighted edge and check to see if the graph is cyclical. If so, remove edge.
        for edge in edge_list:
            #Add the edge to the mst
            for node in mst:
                if node == edge[1]:
                    mst[node].append((edge[2], edge[0]))
                if node == edge[2]:
                    mst[node].append((edge[1], edge[0]))
                #Check to see if the graph is cyclical
                if cyclic(mst):
                    #If it is, remove the edge
                    for node in mst:
                        if node == edge[1]:
                            mst[node].remove((edge[2], edge[0]))
                        if node == edge[2]:
                            mst[node].remove((edge[1], edge[0]))
                else:
                    edge_count += 1
        return mst

a = {'A': [('B', 2), ('C', 6), ('B', 100)],
 'B': [('A', 2), ('C', 5)],
 'C': [('B', 5), ('A', 6)]}

question3(a)



#Code for Question 4


class Node:
 
    # Constructor to create a new node
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def initialize(T, node):
    #Initialize a BST
    r = node.value
    for j in range(len(T)):
        value = T[r][j]
        #If the child is greater in value compared to the node, 
        #put it to the left.
        if (value == 1 and j > r):
            node.right = Node(j)
            return initialize(T, node.right)
        #If the child is greater in value compared to the node, 
        #put it to the left.
        if (value == 1 and j < r):
            node.left = Node(j)
            return initialize(T, node.left)

def lca(root, n1, n2):

    # If both n1 and n2 are smaller than root, then LCA
    # lies in left
    if(root.value > n1 and root.value > n2):
        return lca(root.left, n1, n2)
 
    # If both n1 and n2 are greater than root, then LCA
    # lies in right 
    if(root.value < n1 and root.value < n2):
        return lca(root.right, n1, n2)
 
    return root 

def question4(T, r, n1, n2):
    root = Node(r)
    
    #Initialize the BST
    initialize(T,root)
    
    #Use lca to find the least common ancestor
    lca(root, n1, n2)
 
    return root.value
    print root.value, root.right.value, root.right.right.value
    
    #Test cases

a = [[0,0],
    [1,0]]
b = [[0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0]]
c = [[0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
    [0, 0, 0, 0]]

#Should return 1 
print question4(a, 1, 0, 1)
#Should return 3
print question4(b, 3, 1, 4)
#Should return 1
print question4(c, 0, 1, 2)



#Code for Question 5
# Node class 
class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None
 
class LinkedList:
 
    # Initialize the head of the linkedlist
    def __init__(self):
        self.head = None
 
    # Function to insert a new node at the beginning
    def add_a_node(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def question5(self, ll, m):
        #If the linkedlist is empty, return None
        if ll == None:
            return None
        #Verify the first node is the head
        if ll != self.head.data:
            return 'Node is not the head of the linked list'
        
        #Get the number of linked nodes
        temp = self.head
        count = 0

        while (temp):
            count += 1
            temp = temp.next
        return count
        
        #Create a main and reference pointer
        main = self.head
        ref = self.head 
        n = count - m
        
        
     
        count  = 0
        if(self.head is not None):
            while(count < n ):
                ref = ref.next
                count += 1
 
        while(ref is not None):
            main = main.next
            ref = ref.next
 
        return main.data
 
 
a = LinkedList()
b = LinkedList()
b.add_a_node(0)
c = LinkedList()
c.add_a_node(20)
c.add_a_node(4)
c.add_a_node(15)
c.add_a_node(35)

#Should return None
print a.question5(None, 0)
#Should return 1
print b.question5(0, 1)
#Should return 4
print c.question5(35, 3)



            

