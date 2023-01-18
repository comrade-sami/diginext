# Function:
def Pull(x, y):
    while len(x) < y:
        x += x
    msg = (x[:y])
    aCount = 0
    for i in msg:
        if i.lower() == 'a':
            aCount += 1
    return aCount


# Input:
inputString = input("Enter String: ")
inputNum = int(input("Enter Number: "))

# Call Function:
print(Pull(inputString, inputNum))
