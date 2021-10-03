def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        print('high=', high, ' low=', low)
        mid = int((low + high) / 2)
        guess = list[mid]
        print('mid=', mid, ' guess=', guess, ' item=', item)
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 3))
