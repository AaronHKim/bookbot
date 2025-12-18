from stats import get_num_words,count_letters
def get_book_text(fpath):
    with open(fpath) as f:
        file_contents = f.read()
    return file_contents

def main():
    words = get_book_text("books/frankenstein.txt")
    word_count = get_num_words(words)
    
    #print(f"Found {word_count} total words")
    print(count_letters(words))

main()
