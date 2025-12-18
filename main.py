def get_book_text(fpath):
    with open(fpath) as f:
        file_contents = f.read()
    return file_contents

def main():
    words = get_book_text("books/frankenstein.txt")
    words_array = words.split()
    word_count = len(words_array)
    
    print(f"Found {word_count} total words")

main()
