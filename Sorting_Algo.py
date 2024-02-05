def bubble_sort(input_list):
    swap_status = True
    for j in range(len(input_list)-1, 0, -1):
        if not swap_status:
            break
        swap_status = False
        for i in range(0, j):
            if input_list[i] > input_list[i+1]:
                input_list[i], input_list[i+1] = input_list[i+1], input_list[i]
                swap_status = True
    return input_list

def merge_sorted(list1, list2):
    sorted_list = []
    i, j = 0, 0
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            sorted_list.append(list1[i])
            i += 1
        else:
            sorted_list.append(list2[j])
            j += 1

    if i < len(list1):
        sorted_list += list1[i:]

    if j < len(list2):
        sorted_list += list2[j:]

    return sorted_list

def merge_sort(input_list):
    if len(input_list) < 2:
        return input_list[:]
    else:
        middle = len(input_list)//2
        left = merge_sort(input_list[:middle])
        right = merge_sort(input_list[middle:])
        return merge_sorted(left, right)

def insertion_sort(input_list):
    for key in range(1, len(input_list)):
        if input_list[key] < input_list[key-1]:
            j = key
            while j > 0 and input_list[j] < input_list[j-1]:
                input_list[j], input_list[j-1] = input_list[j-1], input_list[j]
                j -= 1
    return input_list

def selection_sort(input_list):
    for i in range(len(input_list)):
        for j in range(i, len(input_list)):
            if input_list[i] > input_list[j]:
                input_list[i], input_list[j] = input_list[j], input_list[i]
    return input_list

def quicksort(input_list):
    if len(input_list) < 2:
        return input_list
    else:
        pivot = input_list[-1]
        smaller, equal, larger = [], [], []
        for num in input_list:
            if num < pivot:
                smaller.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                larger.append(num)
        return quicksort(smaller) + equal + quicksort(larger)

print("All Modified Algorithms Loaded")
