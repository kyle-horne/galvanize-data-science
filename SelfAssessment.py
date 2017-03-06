"""
Challenge 1
Write a function that looks at the number of times given letters appear in a 
document. The output should be in a dictionary.
"""
def letter_counter(path_to_file, letters_to_count):
    f = open(path_to_file, 'r').read()
    letters = list(letters_to_count)
    letter_dict = {}
    for i in letters:
        letter_dict[i] = f.count(i)
    return(letter_dict)

print(letter_counter('file.txt', 'aeiou'))

"""
Challenge 2
Write a function that removes one occurrence of a given item from a list. Do 
not use methods .pop() or .remove()! If the item is not present in the list, 
output should be ‘The item is not in the list’.
"""
def remove_item(list_items, item_to_remove):
    if item_to_remove in list_items:
        for i in range(len(list_items)):
            if list_items[i] == item_to_remove:
                del list_items[i]
                return(list_items)
    else:
        return('The item is not in the list')

list_items = [1,3,7,8,0]
remove_item(list_items, 7)
print(list_items)

"""
Challenge 3
The simple substitution cipher basically consists of substituting every 
plaintext character for a di erent ciphertext character. The following is an 
example of one possible cipher:
Plain alphabet : abcdefghijklmnopqrstuvwxyz
cipher alphabet: phqgiumeaylnofdxjkrcvstzwb
"""
def cipher(text, cipher_alphabet, option='encipher'):
    s = list(text)
    if option == 'decipher':
        deciphered_list = []
        for item in s:
            if item == " ":
                    deciphered_list.append(" ")
            else:
                for k,v in cipher_alphabet.items():
                    if item == v:
                        deciphered_list.append(k)
        d_str = "".join(deciphered_list)
        print(d_str)        
    else:
        enciphered_list = []
        for item in s:
            if item in cipher_alphabet:
                enciphered_list.append(cipher_alphabet[item])
            else:
                enciphered_list.append(item)
        e_str = "".join(enciphered_list)
        print(e_str)
    return
        
d = dict(zip('abcdefghijklmnopqrstuvwxyz', 'phqgiumeaylnofdxjkrcvstzwb'))
cipher('defend the east wall of the castle', d)
cipher('giuifg cei iprc tpnn du cei qprcni', d, option='decipher')

"""
Challenge 4
Implement a function that counts the number of isograms in a list of strings.An 
isogram is a word that has no repeating letters, consecutive or non-consecutive.
Assume the empty string is an isogram and that the function should be case 
insensitive.
"""
def count_isograms(list_of_words):
    num_isograms = 0
    for item in list_of_words:
        total = 0
        split_word = list(item)
        for char in split_word:
            if split_word.count(char) > 1:
                total += 1
        if total == 0:
            num_isograms += 1
    print(num_isograms)
    return
    
count_isograms(['conduct', 'letter', 'contract', 'hours', 'interview'])

"""
Challenge 5
Write a function that returns a list of matching items. Items are defined by a 
tuple with a letter and a number and we consider item 1 to match item 2 if:
1. Both their letters are vowels (aeiou), or both are consonnants and, 2. The 
sum of their numbers is a multiple of 3
(1,2) contains the same information as (2,1), the output list should only 
contain one of them.
"""
import itertools
def matching_pairs(data_list):
    vowels = ['a', 'e', 'i', 'o', 'u']
    results=[]
    temp = []
    for a, b in itertools.combinations(data_list, 2):
        if ((a[0] in vowels and b[0] in vowels) or (a[0] not in vowels
            and b[0] not in vowels)) and (a[1]+b[1])%3==0:
            temp = [data_list.index(a), data_list.index(b)]
            results.append(temp)
            temp = temp[:]
    print(results)
    return

data = [('a', 4), ('b', 5), ('c', 1), ('d', 3), ('e', 2), ('f', 6)]    
matching_pairs(data)