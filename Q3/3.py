# Function:
def SortArray(text: str):
    text = text.replace("[", "")
    text = text.replace("]", "")
    array = text.split(",")
    for i in range(len(array)):
        array[i] = int(array[i])
    swapsCount = 0
    for i in range(len(array)):
        while array[i] != i + 1:
            temp = array[i]
            array[i] = array[array[i] - 1]
            array[temp - 1] = temp
            swapsCount += 1
    return swapsCount


# Input:
inputArray = input()


print(SortArray(inputArray))
