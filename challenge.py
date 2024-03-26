import re
regex = re.compile('[^a-zA-Z]')

def add_prefix_un(word):
    result = "un"+word
    return result

def make_word_groups(vocab_words):
    wordString = f"{vocab_words[0]}"
    for x in range(1,len(vocab_words)):
        wordString = wordString + f" :: {vocab_words[0] + vocab_words[x]}"
    return wordString

def remove_suffix_ness(word):
    result = word[0:-4]
    if result[-1] == "i":
        result = result[0:-1] + "y"
        return result
    else:
        return result
    
def adjective_to_verb(sentence, index):
    word_array = sentence.split(" ")
    result = regex.sub('', word_array[index]) + "en"
    return result

