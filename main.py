def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_set = character_count(text)

    print(f"{num_words} words found in the document")
    char_set_print(char_set)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def character_count(text):
    char_set = {}
    for character in text:
        if character.lower() not in char_set:
            char_set[character.lower()] = 1
        else:
            char_set[character.lower()] += 1
    
    return char_set

def char_set_print(dictionary):
    sorted_dict = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))
    for k, v in sorted_dict.items():
        if k.isalpha():
            print(f"The {k} character was found {v} times")


main()
