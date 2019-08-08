string=input("give me your string to check if its a pallindrome")
length=len(string)
if length%2==0:
    for i in range(length//2):
        if string.split()[0][i]!=string.split()[0][length-1-i]:
            print("sorry it is not a pallindrome.")
            break
        elif i==(length//2)-1:
            print("yes it is a palindrome.")
elif length%2!=0:
    for j in range((length-1)//2):
        if string.split()[0][j]!=string.split()[0][length-1-j]:
            print("sorry it is not a pallindrome.")
        elif j==((length-1)//2)-1:
            print("yes it is a palindrome.")

