def userInput() : 
    n = int(input("Enter the row of the matrix : "))
    m = int(input("Enter the col of the matrix : "))

    vi = []
    i = 0
    while i < n :
        vx = []
        j = 0
        while j < m:
            vx.append(int(input("Enter the element ")))
            j = j + 1
        vi.append(vx)
        i = i + 1
    return vi