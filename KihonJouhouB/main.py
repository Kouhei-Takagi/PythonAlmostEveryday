def fee(age):
    ret = 0
    if age < 4:
        ret = 100
    elif age < 10:
        ret = 300
    else:
        ret = 500
    return ret

result = fee(3)
print(result)

array = [1, 2, 3, 4, 5]
right = 0
left = 0
tmp = 0

def inverse(array):
    for left in range(1, len(array) // 2):
        right = len(array) - left + 1
        tmp = array[right]
        array[right] = array[left]
        array[left] = tmp
    return array

print(inverse(array))

array = [1, 2, 3, 4, 5]

def inverse(array):
    length = len(array)
    for i in range(length // 2):
        tmp = array[i]
        array[i] = array[length - 1 - i]
        array[length - 1 - i] = tmp
    return array

print(inverse(array))

