def userip():
    a = int(input("Enter number of vectors:"))
    b = int(input("Enter number of elements"))

    v = []
    i = 0
    while i<a :
        e = []
        j = 0
        while j<b:
            e.append(int(input("Enter the element ")))
            j = j+1
        v.append(e)
        i=i+1
    return v