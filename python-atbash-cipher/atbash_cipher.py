import string

plain = "abcdefghijklmnopqrstuvwxyz1234567890"
cipher = "zyxwvutsrqponmlkjihgfedcba1234567890"

def encode(word):
    word = list(''.join([i for i in word if i not in string.punctuation]).replace(" ", "").lower().strip())
    for i in range (len(word)):
        word[i] = cipher[plain.index(word[i])]
    word = ''.join(word)
    return ' '.join([word[k*5:(k+1)*5] for k in range((len(word)//5) + 5)]).strip()
    

def decode(word):
    word = list(word.replace(' ', ''))
    for i in range (len(word)):
        word[i] = plain[cipher.index(word[i])]
    return ''.join(word)