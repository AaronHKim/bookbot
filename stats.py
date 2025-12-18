def get_num_words(words):
    words_array = words.split()
    word_count = len(words_array)
    return word_count
def count_letters(words):
    # ord('a') = 97
    # ord('z') = 122
    # chr(97) = 'a'
    # chr(122) = 'z'
    
    # initializing character counter
    letter_count_dict = {}
    for letter in range(0,2**16):
        letter_count_dict[chr(letter)] = 0
    
    # counting letters
    for word in words:
        letter_count_dict[word.lower()] +=1
    # subset containing only required letters
    letters_only_dict = {letter: letter_count_dict[letter] for letter in 
                         [chr(k) for k in range(97,123)]}
    return letters_only_dict
    