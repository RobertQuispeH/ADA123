import sys
INF = sys.maxsize
def rec(n):
    a=[]
    for i in range(n):
        m = []
        for j in range(n):
            m.append(j+1)
        a.append(m)
    return a

def printdf(array):
    print('--------------Recorrido------------')
    for i in range(len(array)):
        for j in range(len(array)):
            if array[i][j] == 1:
                print("%7s" % "Argentina", end = ' ')
            elif array[i][j] == 2:
                print("%7s" % "Bolivia  ", end = ' ')
            elif array[i][j] == 3:
                print("%7s" % "Brazil   ", end = ' ')
            elif array[i][j] == 4:
                print("%7s" % "Chile    ", end = ' ')
            elif array[i][j] == 5:
                print("%7s" % "Colombia ", end = ' ')
            elif array[i][j] == 6:
                print("%7s" % "Ecuador  ", end = ' ')
            elif array[i][j] == 7:
                print("%7s" % "Guyana   ", end = ' ')
            elif array[i][j] == 8:
                print("%7s" % "Guyana F.", end = ' ')
            elif array[i][j] == 9:
                print("%7s" % "Paraguay ", end = ' ')
            elif array[i][j] == 10:
                print("%7s" % "Perú     ", end = ' ')
            elif array[i][j] == 11:
                print("%7s" % "Suriname ", end = ' ')
            elif array[i][j] == 12:
                print("%7s" % "Uruguay  ", end = ' ')
            else:
                print("%7s" % "Venezuela", end = ' ')   
        print() 
def printdis(array):
    n = len(array)
    print('------Distancia más corta entre paises de sudamerica-----')
    for i in range(n):
        for j in range(n):
            if array[i][j] == INF:
                print("%7s" % ("INF"), end = ' ')
            else:
                print("%7s" % (array[i][j]), end = ' ')
        print()
            
        

        