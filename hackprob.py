in_is = input("enter string")
list_1 = in_is.split()
till_what_number = int(list_1[1])
word = sorted(str(list_1[0]))
for j in range(0,till_what_number):
    for l in range(0,len(word)-j+1):
        a = ""
        new = []
        for k in range(0,j):
            new.append(word[k+l])
        a = a.join(new)
        for i in range(j, len(word)):
            print(a, end=(""))
            print(word[i])
        if j==0 and l==0:
            break
#fakta ata HH type probelm hotoy jyala if a[-1]==word[i] then break lau shakto but jevha first case madhe string form honar nai tevha issue hoil tevha.tyala mag maybe akkha separte loop lau shakto for a c h k separate print ani mag 2 have astil tar tyasathi mi mhanlo tasa.



