def find_missing_number(arr: list) -> int:
    arr.sort()
    start = arr[0]
    end = arr[-1]
    index = 0
    while start < end:
        if start != arr[index]:
            return start
        start += 1
        index += 1