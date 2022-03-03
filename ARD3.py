#ARD3

#exercice 224

def printASCII(s):
    for c in s:
        print(hex(ord(c))[2:], end = " ")
        

#exercice 225
        
def rot13(s):
    for c in s:
        a = ord(c)
        if a == 32:
            b = 32
        else:
            b = a + 13
            if b>122:
                b = b - 26
        print(chr(b), end = "")
        
        
#exercice 227 

def unicode(s):
    for c in s:
        print(c, ":", ord(c), "|", end = " ")
        