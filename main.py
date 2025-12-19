import sys
from stats import number_of_words, list_characters, sorted_dict

def main():
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
       
    location = sys.argv[1]
    text = get_book_text(location)
    words_num = number_of_words(text)
    num_words = f"Found {words_num} total words"
    characters = list_characters(text)
#    print(num_words)
#    print(characters)
    sorted_list = sorted_dict(characters)
    
    print (f"""============ BOOKBOT ============
Analyzing book found at {location}...
----------- Word Count ----------
Found 75767 total words
--------- Character Count -------""")

    for item in sorted_list:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
    print ("============= END ===============")


def get_book_text(file_path):
    with open(file_path) as file:
        file_contents = file.read()
    return file_contents

main()