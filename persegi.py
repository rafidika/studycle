### Mengecek apakah beberapa set angka yang dimasukkan membentuk sebuah persegi

import math

### Syarat persegi:
### 1. Seluruh sisi harus memiliki panjang yang sama
### 2. Seluruh sudut harus memiliki besar 90 derajat

# isTupleValid mengecek apakah tuple valid
def isTupleValid(tup):
    if (len(tup) == 2):
        if (isinstance(tup[0],int) or isinstance(tup[0],float)):
            if(isinstance(tup[1],int) or isinstance(tup[1],float)):
                return True
    return False

# isTupleSame mengecek apakah tuple a dan b (titik koordinat) sama
def isTupleSame(a,b):
    if (a[0] == b[0] and a[1] == b[1]):
        return True
    return False

# countDistance menghitung jarak titik A dan titik B menggunakan euclidean distance
def countDistance(a, b):
    if (isTupleValid(a) and isTupleValid(b)):
        return math.sqrt(math.pow(a[0]-b[0],2) + math.pow(a[1]-b[1],2))
    else:
        return False

# is90Degree mengecek apakah 2 garis yang dibentuk 3 titik bersudut 90 derajat
def is90Degree(a,b,c):
    distanceAB = countDistance(a,b)
    distanceAC = countDistance(a,c)
    distanceBC = countDistance(b,c)

    if (distanceAB == distanceAC):
        if (distanceBC == distanceAB * math.sqrt(2)):
            return ((a,b), (a,c))
    elif (distanceAB == distanceBC):
        if (distanceAC == distanceAB * math.sqrt(2)):
            return ((a,b), (b,c))
    elif (distanceAC == distanceBC):
        if (distanceAB == distanceAC * math.sqrt(2)):
            return ((a,c), (b,c))
    else:
        return False

# searchPerpendicular mencari perpotongan 2 garis yang dikembalikan oleh is90Degree
def searchPerpendicular(tup):
    for i in range(2):    
        for j in range(2):
            if (isTupleSame(tup[0][i],tup[1][j])):
                return tup[0][i]

# isUnique mengecek apakah suatu list berisi tuple-tuple yang unik
def isUnique(listOfElement):
    for i in range(len(listOfElement)-1):
        for j in range(i+1,len(listOfElement)):
            if (isTupleSame(listOfElement[i],listOfElement[j])):
                return False
    return True

# isSquare mengecek apakah seluruh titik yang diberikan membentuk suatu persegi. Masukannya adalah sebuah list of tuple
def isSquare(a,b,c,d):
    point90Degree = []
    ninetyDegree = []
    for i in range(4):
        if (i == 0):
            ninetyDegree = is90Degree(a,b,c)
        elif (i == 1):
            ninetyDegree = is90Degree(a,b,d)
        elif (i == 2):
            ninetyDegree = is90Degree(a,c,d)
        else:
            ninetyDegree = is90Degree(b,c,d)
        if (not ninetyDegree):
            return False
        else:
            point90Degree.append(searchPerpendicular(ninetyDegree))
    if (isUnique(point90Degree)):
        return True
    else:
        return False

# tupleToString mengubah tuple int atau float menjadi string
def tupleToString(tup):
    return "(" + str(tup[0]) + "," + str(tup[1]) + ")"

# isThereSquare mengecek apakah ada persegi yang bisa dibentuk dari kumpulan titik-titik yang diberikan
def isThereSquare(listofTuples):
    atLeastOneSquare = False
    if (len(listofTuples) < 4):
        print("Jumlah titik yang dimasukkan kurang untuk membentuk persegi: " + str(len(listofTuples)))
    else:
        for a in range(len(listofTuples)-3):
            for b in range(a+1,len(listofTuples)-2):
                for c in range(b+1,len(listofTuples)-1):
                    for d in range(c+1,len(listofTuples)):
                        if (isSquare(listofTuples[a],listofTuples[b],listofTuples[c],listofTuples[d])):
                            atLeastOneSquare = True
                            print("Terdapat persegi dengan koordinat " + tupleToString(listofTuples[a]) + " " + tupleToString(listofTuples[b]) + " " + tupleToString(listofTuples[c]) + " " + tupleToString(listofTuples[d]))
        if (not atLeastOneSquare):
            print("Tidak terdapat persegi yang bisa dibentuk dari input-input koordinat")

# Main program
listOfTuples = []
while (True):
    x = float(input("Masukkan koordinat titik di sumbu x: "))
    y = float(input("Masukkan koordinat titik di sumbu y: "))
    newTuple = (x,y)
    listOfTuples.append(newTuple)
    lanjutkan = input("Lanjutkan? (y/n): ")
    while (lanjutkan != "y" and lanjutkan != "n"):
        lanjutkan = input("Lanjutkan? (y/n): ")
    if (lanjutkan == "n"):
        break
isThereSquare(listOfTuples)