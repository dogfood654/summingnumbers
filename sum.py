array = [7, 13, 11, 1]
target = 8

array.sort(reverse=True)
original_array = []

def main():

    reset_array()
"""
    # Compare 1:1
    for i in original_array:
        answer = compare(i, target)
        if answer == 1:
            continue
        else:
            break

    check_status(answer)
    reset_array()

    # Compare 2:1
    for a in range(1, len(original_array)+1):
        temp_array = []
        temp_array.insert(0, original_array[0])
        original_array.pop(0)
        for b in range(1, len(original_array)+1):
            temp_array.insert(1, original_array[b-1])
            if len(temp_array) > 2:
                temp_array.pop(2)
            sum = sum_array(temp_array)
            answer = compare(sum, target)
            if answer == 1:
                continue
            else:
                break
        if answer == 0:
            print("The array is: " + str(temp_array))
            break
        else:
            continue

    check_status(answer)
    reset_array()
"""


def compare(x, y):
    if x == y:
        return 0
    elif x > y:
        return 1
    else:
        return 2

def sum_array(z):
    temp_sum = 0
    for i in z:
        temp_sum += i
    return temp_sum

def check_status(p):
    if p == 0:
        print("Found it")
    else:
        print("No luck, try another one")
    return

def reset_array():
    original_array.clear()
    original_array.extend(array)
    return

main()