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




# Code solution for question 2

def question2(s):
    
    # initialize largest palindrome substring
    lp = ''
    # empty string and one character string cases
    if len(s) < 2:
        return s
    
    for i in range(len(s)):
        for j in range(i+1,len(s)-1):
            # If the string is palindronic and has more characters than the lp, it becomes the lp.
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



# Code solution for question 3


parent = dict()
rank = dict()

def sortbyweight(graph):
    # Make a list of edges based on weights in ascending order
    edges = []
    for node1 in graph:
        for i in range(len(graph[node1])):
            edge = sorted((node1, graph[node1][i][0], graph[node1][i][1]))
            edge = tuple(edge)
            if edge not in edges:
                edges.append(edge)
    edges = sorted(edges)

    return edges

def make_set(v):
    parent[v] = v
    rank[v] = 0

def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]

def union(v1, v2):
    root1 = find(v1)
    root2 = find(v2)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]: rank[root2] += 1

def adjacency(graph, edges):
    for edge in edges:
        weight, v1, v2 = edge
        for v in graph:
            if v1 == v:
                graph[v].append((v2, weight))
            if v2 == v:
                graph[v].append((v1, weight))
    return graph

def question3(graph):
    # Initiate a mst dict
    mst_dict = {}
    
    # Setup parent and rank dicts
    for v in graph:
        mst_dict[v] = []
        make_set(v)
    
    # Create a minimum spanning tree
    mst = set()
    
    # Create a list of edges
    edges = sortbyweight(graph)
    
    for edge in edges:
        weight, v1, v2 = edge
        if find(v1) != find(v2):
            union(v1, v2)
            mst.add(edge)
    
    #Create an adjacency matrix
    return adjacency(mst_dict, mst)


a = {'A': [('B', 2), ('C', 6), ('B', 100)],
 'B': [('A', 2), ('C', 5)],
 'C': [('B', 5), ('A', 6)]}

b = {'A': [('B', 2)],
 'B': [('A', 2)]}

c = {}



print question3(a)
print question3(b)
print question3(c)



#Code for Question 4


class Node:
 
    # Constructor to create a new node
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def initialize(T, n):
    for i in range(len(T)):
        # If the child is smaller in value compared to the node, 
        # put it to the right.
        if (T[n.value][i] == 1 and i > n.value):
            n.right = i
            initialize(T, Node(i))
        
        # If the child is greater in value compared to the node, 
        # put it to the left.
        if (T[n.value][i] == 1 and i < n.value):
            n.left = i
            initialize(T, Node(i))

def lca(root, n1, n2):
    
    # If both n1 and n2 are smaller than root, then LCA
    # lies in left
    if(root.value > n1 and root.value > n2):
        return lca(root.left, n1, n2)
 
    # If both n1 and n2 are greater than root, then LCA
    # lies in right 
    if(root.value < n1 and root.value < n2):
        return lca(root.right, n1, n2)
 
    return root.value 

def question4(T, r, n1, n2):
    root = Node(r)
    # Initialize the BST
    initialize(T, root)
    
    # Use lca to find the least common ancestor
    return lca(root, n1, n2)
    
    
    
# Test cases

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

# Should return 1 
print question4(a, 1, 0, 1)
# Should return 3
print question4(b, 3, 1, 4)
# Should return 1
print question4(c, 1, 1, 3)




# Code for Question 5
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
        # If the linkedlist is empty, return None
        if ll == None:
            return None
        # Verify the first node is the head
        if ll != self.head.data:
            return 'Node is not the head of the linked list'
        
        # Get the number of linked nodes
        temp = self.head
        total = 0

        while (temp):
            total += 1
            temp = temp.next

        ref = self.head
        
        #Find the position of the node from the head
        n = total - m
        
        count = 0
        
        while(count < n ):
            ref = ref.next
            count += 1
 
        return ref.data
 
 
a = LinkedList()
b = LinkedList()
b.add_a_node(0)
c = LinkedList()
c.add_a_node(20)
c.add_a_node(4)
c.add_a_node(15)
c.add_a_node(35)

# Should return None
print a.question5(None, 0)
# Should return 1
print b.question5(0, 1)
# Should return 4
print c.question5(35, 3)



            

