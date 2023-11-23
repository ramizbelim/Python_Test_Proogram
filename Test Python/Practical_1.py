user_string = " Tom, Tony, tony@Stark, alfred254, Tony stark, Edward, tom$323, Nigam, frank, Francis, nigam Gupta "
# user_string = input("Enter a sentence : ")
def practical_1(sentence):
    sentence_strip = sentence.strip()
    punc = 'aeiou,'
    result = []
    for ele in sentence_strip.split():
        if ele.isalpha():
            pass
        elif ele not in punc:
            result.append(ele)
        elif ele.isdigit():
            pass
    return result
print(practical_1(user_string))



