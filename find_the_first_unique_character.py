def find_the_first_unique_char(s: str) -> str:
    s = s.strip()
    if not s:
        return None
        
    for char in s:
        count = 0
        for char2 in s:
            if char == char2:
                count += 1
        if count == 1:
            return char
    return None     
