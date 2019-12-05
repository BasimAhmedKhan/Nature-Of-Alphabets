print(" ")
print("Vowel or Semi-vowel or Consonant")
print(" ")

alph = input("Enter An English Alphabet: ")

if alph == ("a") or alph == ("e") or alph == ("i") or alph == ("o") or alph == ("u"):
    print("Vowel Alphabet")
elif alph == ("y") or alph == ("w"):
    print("Semi-Vowel Alphabet")
elif alph == ('b') or alph == ('c') or alph == ('d') or alph == ('f') or alph == ('g') or alph == ('h') or alph == ('j') or alph == ('k') or alph == ('l') or alph == ('m') or alph == ('n') or alph == ('p') or alph == ('q') or alph == ('r') or alph == ('s') or alph == ('t') or alph == ('v') or alph == ('x') or alph == ('z'):
    print("Consonant Alphabet")
else:
    print("Invalid Input")