def length_of_last_word(s: str) -> int:
    arr_txt = s.split()
    if len(arr_txt) == 0:
        return 0
    return len(arr_txt[-1])