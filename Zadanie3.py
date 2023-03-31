def cypher(data, offset, alphabet=None):
    if alphabet is None:
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                    'u', 'v', 'w', 'x', 'y', 'z']
    offset = offset % len(alphabet)
    data=data.lower()
    result = ""
    for i in range(len(data)):
        if alphabet.__contains__(data[i]):
            for j in alphabet:
                if data[i] == j:
                    if alphabet.index(j) + offset > len(alphabet) - 1:
                        result += alphabet[alphabet.index(j) + offset - len(alphabet)]
                    else:
                        result += alphabet[alphabet.index(j) + offset]
        else:
            result += data[i]
    return result

tekstDoZaszyfrowania = "The Project Gutenberg eBook of Alice’s Adventures in Wonderland, by Lewis Carroll"
zaszyfrowanie=cypher(tekstDoZaszyfrowania,5)
print(zaszyfrowanie)
#Zamiana a na B
enc = cypher(tekstDoZaszyfrowania,3,["a","B"])
print(enc)