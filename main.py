from stats import get_num_words,count_letters,sorted_count
import sys

def get_book_text(fpath):
    with open(fpath) as f:
        file_contents = f.read()
    return file_contents

def main():
    # print(sys.argv[0])

    try:
        f_path = sys.argv[1]
        # f_path = "books/frankenstein.txt"
        print("============ BOOKBOT ============")
        words = get_book_text(f_path)
        print(f"Analyzing book found at {f_path}...")
        
        print("----------- Word Count ----------")
        word_count = get_num_words(words)
        print(f"Found {word_count} total words")
        
        print("--------- Character Count -------")
        sorted_count(words)
        #print(sorted_count(words))
    except Exception as e:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    

main()
