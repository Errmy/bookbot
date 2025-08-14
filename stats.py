def get_word_number(text):
    word_list = text.split()
    return len(word_list)

def get_char_dict(text):
    char_set = set(text.lower())
    char_dict = {}
    for char in char_set:
        char_dict[char] = 0
    for char in text.lower():
        if char in char_set:
            char_dict[char] += 1
    return char_dict

def sort_on(items):
    return items["num"]

def get_sorted_list(char_dict):
    char_list = []
    for key in char_dict:
        if key.isalpha():
            char_list.append({"char": key, "num": char_dict[key]})

    
    char_list.sort(reverse=True, key=sort_on)
    return char_list