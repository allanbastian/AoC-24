def check_level_difference(arr: list[int]):
    for i in range(len(arr) - 1):
        diff = abs(arr[i] - arr[i+1])
        if diff < 1 or diff > 3:
            return False
    return True

def check_ascending_elements(arr: list[int]):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            return False
    return True

def check_descending_elements(arr: list[int]):
    for i in range(len(arr) - 1):
        if arr[i] < arr[i+1]:
            return False
    return True

with open('day2/day2_input.txt', 'r') as file:
    count = 0
    for line in file:
        arr = []
        strlst = line.split()
        for i in strlst:
            arr.append(int(i))
        is_asc = check_ascending_elements(arr)
        is_desc = check_descending_elements(arr)
        ans = is_asc or is_desc
        is_safe = ans and check_level_difference(arr)
        if is_safe:
            count += 1
    print(count)
    #ans is 490