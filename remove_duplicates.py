def remove_duplicates(arr: list) -> list:
    filtered_arr = []
    for li in arr:
        found = False
        for li2 in filtered_arr:
            if li == li2:
                found = True
                break
        if not found:
            filtered_arr.append(li)
    return filtered_arr
  
