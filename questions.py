#Code solution for question 1

def question1(s,t):
    #make the elements in both s and t lowercase.
    s = s.lower()
    t = t.lower()
    #Initialize counter and Boolean variable r
    counter = 0
    r = False
    
    for i in range(len(t)):
        for j in range(len(s)):
            if s[j] == t[i]:
                r = True
        if r:
        #If r is True, add one to our counter.
            counter += 1
        #Reset r
        r = False
        
    #If the number of characters of t is equal to our counter, return True.
    return(counter == len(t))

a = 'I go on and on'
b = 'igo'
c = ''
d = ''
e = 'Cant Understand'
f = 'how'

#Should return True
print question1(a,b)
#Should return True
print question1(c,d)
#Should return False
print question1(e,f)

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


#Code solution for question 2
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
