from stats import get_word_number, get_char_dict, get_sorted_list
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents



def main():
    args = sys.argv
    if len(args) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    num_words = get_word_number(get_book_text(filepath))
    #print(f"{num_words} words found in the document")
    #print(get_char_dict(get_book_text("books/frankenstein.txt")))
    char_list = get_sorted_list(get_char_dict(get_book_text(filepath)))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in char_list:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()