import os
    
def word_mod(word, mod):
    if mod > 26 or mod < 0:
        print("You must use a number within the inclusive range of 0-26")
        return
    
    cleaned_word = ""
    mod_word = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    mod_alphabet = {}

    for letter in word:
        if letter in alphabet:
            cleaned_word += letter

    i = mod + 1
    for letter in alphabet:
        if i > len(alphabet):
            i = 1
            mod_alphabet[letter] = i
            i += 1
        else:
            mod_alphabet[letter] = i
            i += 1
    
    for letter in cleaned_word:
        letter_index = mod_alphabet[letter]
        keys = list(mod_alphabet.keys())
        mod_word += keys[letter_index - 1]

    return mod_word

def analyze_words(file):
    words = []
    words_dict = {}
    final_word_dict = {}
    with open (file, 'r') as reader:
        for line in reader.readlines():
            word = line.rstrip('\n').lower()
            words.append(word)
            words_dict[word] = []
    for word in words:
        i = 1
        while i <= 25:
            mod_word = word_mod(word, i)
            print(mod_word)
            if mod_word in words_dict:
                words_dict[word].append([mod_word, i])
            i += 1

    for entry in words_dict.copy():
        if len(words_dict[entry]) > 0 and len(entry) > 2:
            final_word_dict[entry] = words_dict[entry]
    
    
    with open("word_list.txt", "w") as f:
        f.write(str(final_word_dict))
    
    print(len(final_word_dict))
        







    






