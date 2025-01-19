def count_character_frequency(text: str) -> dict:
    text_trimmed = text.replace(' ', '')
    char_freq = {}
    for char in text_trimmed:
        count = 0
        for inner_char in text_trimmed:
            if inner_char == char:
                count += 1
        char_freq[char] = count
    return char_freq