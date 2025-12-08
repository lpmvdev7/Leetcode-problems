# Caso 1
#ransomNote = "a"
#magazine = "b"
# FALSE

# Caso 2
#ransomNote = "aa"
#magazine = "ab"
# FALSE

# Caso 3
#ransomNote = "aa"
#magazine = "aab"
#TRUE

def reconstructWord(ransomNote, magazine):
    construct = []

    for l in magazine:
        if l in ransomNote:
            construct.append(l)
    delimeter = ""
    map_string = map(str, construct)
    word = delimeter.join(map_string)

    print(ransomNote)
    print(word)

    if word == ransomNote:
        return True
    else:
        return False

call = reconstructWord("aa", "aab")
print(call)







