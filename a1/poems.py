import codecs
import random

poems = ['01', '02', '03']
current_poem = poems[2]

with open(current_poem + '.txt','r') as poem:
    content = poem.read()
    words_array = content.split()
    # print(words_array[4])

new_poem = ''
counter = 0
line_length = random.randint(1, 7)
for i in range(0, len(words_array)):
    element_index = random.randint(0, len(words_array)-1)
    new_poem += words_array[element_index]
    counter += 1
    if counter == line_length:
        counter = 0
        line_length = random.randint(1, 7)
        new_poem += '\n'
        # print("New line")
    else:
        new_poem += ' '
    # print(words_array[element_index])

    del words_array[element_index]

with open(current_poem + "_modified.txt", 'w') as f:
    f.write(new_poem)

print(new_poem)