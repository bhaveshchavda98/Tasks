pyg = 'ay'
original = input("Enter the word:")

if len(original)>0 and original.isalpha():
    word = original.lower()
    first = word[0]
    new_word = first + pyg
    new_word = word[1:] + new_word

    print('Result:', new_word)
else:
    print("empty")