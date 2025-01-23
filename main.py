def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    char_dic = get_char_dict(text)

    print(book_path)



def get_char_dict(text):
    dict = {}
    lowercase = text.lower()
    for letter in lowercase:
        if letter in dict:
            dict[letter] += 1
        else:
            dict[letter] = 1
    return dict


def get_word_count(text):
    words = len(text.split())
    return words



def get_book_text(book_path):
    with open(book_path) as t:
        return t.read()


main()