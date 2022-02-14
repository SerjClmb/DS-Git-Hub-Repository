str_list = ['text', 'morning',
            'notepad', 'television',
            'ornament'
            ]
word_dict = {}
for word in str_list:
    word_dict[word] = word.count('t')
print(word_dict)
