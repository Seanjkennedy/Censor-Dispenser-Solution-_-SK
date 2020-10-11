# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]
negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]
punctuation = [",", "!", "?", ".", "%", "/", "(", ")"]


def censor_length(word):
    word = full_word(word)
    word = "##" + (len(word) * "#") + "#"
    return word

def full_word(word):
    temp = word
    count = -2

    if (word[-1] != " "):
        if (word[-1] in punctuation):
            while count < len(word) -1 :
                count = count + 1
                temp = temp.replace(word[count], "#")
    return temp

def censor_2(terms, source):
    temp = source

    for i in range(len(terms)):
        if terms[i] in source:
            temp = temp.replace(terms[i], censor_length(terms[i]))
        if terms[i] in source.lower():
            temp = temp.replace(terms[i].title(), censor_length(full_word(terms[i])))
        if terms[i] in source.lower():
            temp = temp.replace(terms[i].upper(), censor_length(full_word(terms[i])))

    return temp

def censor_combine(terms1, terms2, source):
    a = censor_2(terms1, source)
    a = censor_2(terms2, a)

    return a

def censor_main(terms1, terms2, source):

    copy_a = source.split(" ")
    censored_doc = censor_combine(terms1, terms2, source)
    copy_b = censored_doc.split(" ")

    count = 0
    for i in copy_a:
        if count > 0 and count < len((copy_a)):
            try:
                if "#" in copy_b[count]:

                    try:
                        if ((copy_b[count-1] + " " + copy_b[count] + " "+ copy_b[count+1])) in censored_doc:
                            censored_doc = censored_doc.replace((copy_b[count-1] + " " + copy_b[count] + " " + copy_b[count+1]), (censor_length(copy_b[count-1]) + " " + censor_length(copy_b[count]) + " "+ censor_length(copy_b[count+1])))
                    except IndexError:
                        continue
            except IndexError:
                continue
        count = count + 1


    return censored_doc

#print(censor_main(negative_words,proprietary_terms,email_one))

#print(censor_main(negative_words,proprietary_terms,email_two))

#print(censor_main(negative_words,proprietary_terms,email_three))

#print(censor_main(negative_words,proprietary_terms,email_four))
