def isSubsequence(s, t):
    x,y= 0,0
    while x < len(s) and y < len(t):
        if s[x]== t[y]:
            x+=1
        y+=1
    if x==len(s):
        return True
        print("true")
    else:
        print("false")
        return False

isSubsequence("abc",'ahbgdc')


