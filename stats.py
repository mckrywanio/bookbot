#Fn that allows you to count the words in the book
def words_in_string(book):
    words = book.split()
    word_count = len(words)
    return word_count

#Fn that counts the individual lower case characters
#list them as {'t' : 2333} in a dict
def count_of_char(book):
    text = book.lower()
    char_counts = {}

    for char in text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    return char_counts

#Returns the count dict after sorting
def sorted_dict_chars(char_counts):
    sorted_list = []

    for char, count in char_counts.items():
        sorted_list.append({"char": char, "num": count})

    sorted_list.sort(key=lambda x: x["num"], reverse=True)
    return sorted_list