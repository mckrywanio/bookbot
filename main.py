import sys

#Fn that opens a book and prints it to a string
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()
    

    
#basic pull of a book and then runs the get_book_text
#uses whats defined in file_path
#prints the text of book to console/terminal.
def main():
    #Book Pull
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]

    book_text = get_book_text(path)
    #Fn's to stats
    num_words = words_in_string(book_text)
    char_count = count_of_char(book_text)
    sorted_chars = sorted_dict_chars(char_count)

    
#Outputs to console
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/Frankenstein.txt...")
    print("----------- Word Count -----------")
    print("Found", num_words, "total words")
    print("--------- Character Count ---------")

    for entry in sorted_chars:
        char = entry["char"]
        num = entry["num"]
        if char.isalpha():
            print(f"{char}: {num}")
    
    print("============= END =============")



#imports from stats.py
from stats import words_in_string
from stats import count_of_char
from stats import sorted_dict_chars

main()

