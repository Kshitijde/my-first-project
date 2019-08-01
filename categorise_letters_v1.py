response=0
dictionary={}
while True:
    response=int(input(print("press 1 to enter a new word and press 2 to stop and see your dictionary")))
    if response==2:
        break
    word=input(print("enter your word"))
    first_letter=word[0]
    if first_letter in dictionary.keys():
        dictionary[first_letter].append(word)
    else:
        dictionary[first_letter]=[]
        dictionary[first_letter].append(word)
print(dictionary)
