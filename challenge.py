import re
regex = re.compile('[^a-zA-Z]')

# function to add prefix- un
def add_prefix_un(word):
    result = "un"+word
    return result

# function to transform array of vocab words into array of vocab words
def make_word_groups(vocab_words):
    wordString = f"{vocab_words[0]}"
    for x in range(1,len(vocab_words)):
        wordString = wordString + f" :: {vocab_words[0] + vocab_words[x]}"
    return wordString

# function to remove suffix
def remove_suffix_ness(word):
    result = word[0:-4]
    if result[-1] == "i":
        result = result[0:-1] + "y"
        return result
    else:
        return result

# function to convert adjective in sentence to a verb
def adjective_to_verb(sentence, index):
    word_array = sentence.split(" ")
    result = regex.sub('', word_array[index]) + "en"
    return result

menu = "HEY SISTER\n"
menu += "Select one of the following options below:\n"
menu += "1 - add_prefix_un\n"
menu += "2 - make_word_groups\n"
menu += "3 - remove_suffix_ness\n"
menu += "4 - adjective_to_verb\n"
menu += ":"

option = input(menu)
if option == "1":
    word = input("Please enter a word for the prefix -un:")
    print(add_prefix_un(word))
elif option == "2":
    prefix = input("Please enter the prefix of the vocab_words array:")
    words = input("Please enter the words of the vocab_words array seperated by a space:")
    vocab_words = []
    vocab_words.append(prefix)
    words_array = words.split(" ")
    for w in words_array:
        vocab_words.append(w)
    print(make_word_groups(vocab_words))
elif option == "3":
    word = input("Please enter a word with the suffix -ness:")
    print(remove_suffix_ness(word))
elif option == "4":
    sentence = input("Please enter a sentence that contains an adjective:")
    index = input("Please enter the index of the adjective in sentence:")
    print(adjective_to_verb(sentence, int(index)))
else:
    print(f"{option} is not a menu option")