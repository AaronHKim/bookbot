def get_num_words(words):
    words_array = words.split()
    word_count = len(words_array)
    return word_count
def count_letters(words):
    # ord('a') = 97
    # ord('z') = 122
    # chr(97) = 'a'
    # chr(122) = 'z'
    num_ascii_chars = 2**16
    
    # initializing character counter
    letter_count_dict = {}
    
    for letter in range(0,num_ascii_chars):
        letter_count_dict[chr(letter)] = 0
    
    # counting letters
    for word in words:
        letter_count_dict[word.lower()] +=1
        
    # subset containing only required letters
    letters_only_dict = {letter: letter_count_dict[letter] for letter in 
                         [chr(k) for k in range(97,123)]}
    
    return letters_only_dict


def sorted_count(words):
    def sort_on(items):
        return items['num']
    
    letter_dict= count_letters(words)
    nums=[]
    
    for key in letter_dict:
        nums.append({"letter":key, "num": letter_dict[key]})
    
    nums.sort(reverse=True,key=sort_on)
    
    for letter_count in nums:
        print(f"{letter_count['letter']}: {letter_count['num']}")
    
    return nums


    