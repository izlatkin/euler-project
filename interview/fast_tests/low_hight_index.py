def find_ow_high_index(a: list[int], val: int):
    def find_low(val):
        low = 0
        high = len(a) - 1
        index = -1

        while (low <= high):
            mid = (low + high) // 2
            if a[mid] == val:
                index = mid
                high = mid - 1
            elif a[mid] < val:
                low = mid + 1
            else:
                high = mid - 1

        return index

    def find_higt(val):
        low = 0
        high = len(a) - 1
        index = -1

        while (low <= high):
            mid = (low + high) // 2
            if a[mid] == val:
                index = mid
                low = mid + 1
            elif a[mid] < val:
                low = mid + 1
            else:
                high = mid - 1

        return index

    low = find_low(val)
    if low == -1:
        return -1
    high = find_higt(val)

    return [low, high]


# Driver code
if __name__ == '__main__':
    for i in range(1, 8):
        print(find_ow_high_index([1, 2, 3, 4, 4, 4, 4, 5, 6, 7, 7, 7, 7], i))