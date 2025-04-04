from stats import get_word_count

def main():

    #Where is the book located
    book_path = "books/frankenstein.txt"

    #Functions of the report
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    char_dict = get_char_dict(text)
    sorted_dict = get_sorted_dict(char_dict)

    #Printing the report
    print(f"Report for {book_path} is here!")
    print(f"There were {word_count} words found in the document! WOW...\n")
    
    for x in sorted_dict:
        print(f"'{x['char']}' was found '{x['freq']}' times...")

    print(f"\nThanks for reading this report on {book_path} :)")

#---------FUNCTIONS---------#

def get_sorted_dict(char_dict):
    char_freq = []
    for c in char_dict:
        if c.isalpha() == True:
            char_freq.append({"char": c, "freq": char_dict[c]})
    char_freq.sort(reverse=True, key=lambda x: x["freq"])
    return char_freq


def get_char_dict(text):
    dict = {}
    lowercase = text.lower()
    for letter in lowercase:
        if letter in dict:
            dict[letter] += 1
        else:
            dict[letter] = 1
    return dict


def get_book_text(book_path):
    with open(book_path) as t:
        return t.read()

main()