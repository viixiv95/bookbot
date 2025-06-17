from stats import count_characters
from stats import get_num_words
from stats import sort_list
import sys

def get_book_text ():
    with open(sys.argv[1]) as f :
        content = f.read()
    return content

def main():

    if len(sys.argv) != 2:
        print(f"<Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book = get_book_text()
    book_lower =  book.lower()
    num_words = get_num_words (book)
    char_dict = count_characters(book_lower)
    sorted_list = sort_list(char_dict)



    #print ("============ BOOKBOT ============\n " \
    #"Analyzing book found at books/frankenstein.txt...\n" \
    #"----------- Word Count ----------\n"
    #f"Found {num_words} total words\n"
    #"--------- Character Count -------")#

    for key in range(len(sorted_list)):
        character = sorted_list[key]["character"]
        if character.isalpha():
            print (f"{sorted_list[key]["character"]}: {sorted_list[key]["num"]}")
    #print ("============= END ===============")


if __name__ == "__main__":
    main() 

