def heh(x):
    count = 0
    for i in range(0,len(x)-1):
        if x[i] == x[i+1]:
            count += 1
    return count


inputString = input("Enter: ")


print(heh(inputString))
