#97 = a ; 122 = z

import random
plain_text = str(input("Write your text to be encrypted: \n"))

plain_text = plain_text.lower()                         # converts all text in lowercase

plain_text_list = list(plain_text)                      # converts lowercase string in list object

print(plain_text_list)

for j in range(1, plain_text_list.count(' ')+1):        # removes spaces
    plain_text_list.remove(' ')

print(plain_text_list)

num_letter = len(plain_text_list)                       # takes length of list

# print(num_letter)

key1 = [];  key2 = []; key3 = []

for i in range(1, len(plain_text_list)+1):              # creates random keys equal to the length of text
    key1.append(chr(random.randrange(97, 123)))
    key2.append(chr(random.randrange(97, 123)))
    key3.append(chr(random.randrange(97, 123)))

print(key1, ' => Key 1'); print(key2, ' => Key 2'); print(key3, ' => Key 3')

count = 1

for i in range(num_letter):                    # replacing elements in list with monoalphabetic keys a/c to algorithm
    if count == 1:
        plain_text_list[i] = key1[i]
        count += 1

        if num_letter == i:
            break

    elif count == 2:
        plain_text_list[i] = key2[i]
        count += 1

        if num_letter == i:
            break

    elif count == 3:
        plain_text_list[i] = key3[i]
        count = 1

        if num_letter == i:
            break

print(plain_text_list)

cipher_text = ''.join(plain_text_list)                  # converting the list into string, without spaces

print(cipher_text, ' =>Cipher Text')