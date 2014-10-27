from datetime import datetime
import time

#Count words
array = ["apple", "banana", "apple", "pie"]

def count_words(arr):
    words = {}
    for word in arr:
        print (word)
        if words.get(word) == None:
            words[word] = 1
        else:
            words[word] = words[word] + 1
    return words


#print (count_words(array))



#Unique words
def unique_words_count(arr):
    return len(set(arr))

#print (unique_words_count(array))




#print (groupby(lambda x: x % 2, [0,1,2,3,4,5,6,7]))


#Spam and Eggs
def prepare_meal(number):
    num = number
    result = ""
    if not (number % 3 == 0):
        return result
    else:
        while (number % 3 == 0):
            number = number / 3
            result = result + "spam "
    if num % 5 == 0:
        result = result + "and eggs"
    return result

#print (prepare_meal(45))


#Reduce file path
str = '/srv/www/./htdocs//wtf/..'
def reduce_file_path(path):
    path = str.split('/')
    i = 0
    result = ""
    for n in path:
        if path[i] == '':
            path.remove(path[i])
        elif path[0] == '..' or path[1] == '.':
            return '/'
        elif path[i] == '..' and i != 0:
            path.remove(path[i])
            path.remove(path[i-1])
        elif path[i] == '.':
            path.remove(path[i])
        i = i + 1

    str_return = ''
    for directory in path:
        str_return = str_return + '/' + directory


    return str_return

#print (reduce_file_path(str))

#Word from a^nb^n


def is_an_bn(word):
    myword = list(word)
    if len(myword) % 2 != 0:
        return False
    else:
        middle = len(myword) / 2
        i = 0
        while i < middle:
            if myword[i] != 'a' or myword[len(myword)-i-1] != 'b':
                return False

            i = i + 1
        return True


#print(is_an_bn("aabbaabb"))


#Simplify fractions

class Fraction():
    def __init__(self, numerator, denumerator):
        self.numerator = numerator
        self.denumerator = denumerator
    def __str__(self):
        return "{} / {}".format(self.numerator, self.denumerator)


def simplify_fraction(fraction):
    nominator = fraction.numerator
    denominator = fraction.denumerator
    r = 0
    mcd = 0
    while denominator != 0:
        r = nominator % denominator;
        nominator = denominator;
        denominator = r;
    mcd = nominator
    return Fraction(fraction.numerator / mcd,fraction.denumerator / mcd)

f = Fraction(3,9)
#print (simplify_fraction(f))


def test():
    # time tuple to string
    t = 88

    m = 0
    s = 0
    print(t//60)
    print(t%60)

test()