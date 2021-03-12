import random


print("Hello")
with open('photo.jpg','rb') as image_file:
    content = image_file.read()
    # print(content)
    modified = ''.join(content[c] for c in range(0, 3000))
    for c in range(3000, len(content)):
        modified = modified + ' ' if random.randint(0, 10) > 7 else modified + content[c]

with open("photo_edited.jpg", 'wb') as f:
    f.write(modified)

print("Done.")