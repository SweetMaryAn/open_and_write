import os


docs = {}
with open(os.path.join(os.getcwd(), '1.txt'), encoding='utf8') as file_1:
    counter_1 = len(file_1.readlines())
    docs[1]= counter_1
with open(os.path.join(os.getcwd(), '2.txt'), encoding='utf8') as file_2:
    counter_2 = len(file_2.readlines())
    docs[2]= counter_2
with open(os.path.join(os.getcwd(), '3.txt'), encoding='utf8') as file_3:
    counter_3 = len(file_3.readlines())
    docs[3]= counter_3

lengts = sorted(docs.values())

for lengt in lengts:
    if lengt == docs[1]:
        with open(os.path.join(os.getcwd(), '1.txt'), encoding='utf8') as file_1:
            content_1 = file_1.read()
        with open(os.path.join(os.getcwd(), 'Itog.txt'), 'a', encoding='utf8') as file:
            file.write(f'1.txt\n')
            file.write(f'{counter_1}\n')
            file.write(f'{content_1}\n')
    elif lengt == docs[2]:
        with open(os.path.join(os.getcwd(), '2.txt'), encoding='utf8') as file_2:
            content_2 = file_2.read()
        with open(os.path.join(os.getcwd(), 'Itog.txt'), 'a', encoding='utf8') as file:
            file.write(f'2.txt\n')
            file.write(f'{counter_2}\n')
            file.write(f'{content_2}\n')
    elif lengt == docs[3]:
        with open(os.path.join(os.getcwd(), '3.txt'), encoding='utf8') as file_3:
            content_3 = file_3.read()
        with open(os.path.join(os.getcwd(), 'Itog.txt'), 'a', encoding='utf8') as file:
            file.write(f'3.txt\n')
            file.write(f'{counter_3}\n')
            file.write(f'{content_3}\n')