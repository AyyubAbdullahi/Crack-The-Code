# Code
# This program will be used to decipher encrypted text
def remove_chars(word, char_list):
# this function is used to remove unwanted elements from the encrypted text
# parameters: word(list), char_list(list)
    # i use a while loop with i to keep count of iterations. If a certain element matches with an element from char_list it is removed
    i = 0
    while i < len(word):
        for char in char_list:
            if word[i] == char:
                del word[i]
        i+=1       
        
def rev_string(word):
# this function is used to reverse the encrypted text
# parameters: word(list)
    # i make a copy of the encrypted text and replace each elemnt of the orignal list with an element from the copied list an equal distance from the back as the original is from the front
    word_copy = word.copy()
    i = 0
    while i < len(word):
        word[i] = word_copy[len(word)-(i+1)]
        i+=1
        
def sub_alt_num(word):
# in this function i subtract 2 from every other digit
# parameters: word(List)
    # I use a while loop with counter i. If i come across an element that is a digit I subtract 2 from that digit and increment i by 2. Otherwise I increment i by 1
    i = 0
    while i < len(word):
        if word[i].isdigit():
            word[i] = str(int(word[i])-2)
            i+=2
        else:
            i+=1
            
def swap_cases(word):
# this function swaps the cases of each letter in the encrypted text
# parameters: word(list)
    # I use another for loop witha counter i. If a letter is uppercase I replace that element with an lowercase version of it. Vice versa for lowercase letter
    i = 0
    for letter in word:
        if letter.islower():
            word[i] = word[i].upper()
        elif letter.isupper():
            word[i] = word[i].lower()
        i+=1
        
def display(ecode,dcode):
# I call this function to display the encrypeted text, and the finished decrypted text
# parameters: ecode(str), dcode(str)
    # print the results
    print('Encrypted Code:  ' + ecode)
    print('Decrypted Code:  ' + dcode)

def read_file():
# this function reads the encrypted text from a file and returns it
    infile = open('encrypted2.txt')
    content = infile.read()
    infile.close()
    return content

def main(): 
# main function
    # read the encrypted text from a file and run the required functions to decrypt it and display the decrypted text
    ecode = read_file()
    word = list(ecode)
    char_list = ['&', '+', '#', '%', '/', '$', '@', '!']
    remove_chars(word, char_list)
    rev_string(word)
    sub_alt_num(word)
    swap_cases(word)
    dcode = "".join(word)
    display(ecode, dcode)
main()