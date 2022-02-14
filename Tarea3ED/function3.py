

def valx(x):
#if X
    if (x > 0):
        a = "positive"
        return (a)
    elif (x < 0):
        a = "negative"
        return (a)
    else:
        a = "no es ni negativo ni positivo"
        return (a)
def valy(y):
#if Y
    if (y > 0):
        b = "positive"
        return (b)  
    elif (y < 0):
        b = "negative"
        return (b)
    else:
        b = ("no es ni negativo ni positivo")
        return (b)

def findCua (a,b):

    #if cuadrante
    if (a > 0 and b > 0):
        c = 1
        return(c)
    elif(a<0 and b>0):
        c = 2
        return(c)
    elif(a<0 and b<0):
        c = 3
        return(c)        
    elif(a>0 and b<0):
        c = 4
        return(c)
    elif(a == "no es ni negativo ni positivo" or b == "no es ni negativo ni positivo"):
        c = 0
        return(c)


