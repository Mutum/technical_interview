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

