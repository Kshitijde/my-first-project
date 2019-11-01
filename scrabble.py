#create scrabble game
from nltk.corpus import words
import random
import string
word_list = words.words()
"""plan is simple use inbuilt to verify if the words exists.Also 8 by 8 square of scrabble will be maintained containing 8 rowd and 8 columns 
initially all will be - placed in empty areas and then the given word must further start or atleast have one of the letters involved.
it must also maintain a score.it should be verified that in such a case the word is not crossing the sq's limits"""
playing_surface=[]
for i in range(8):
    playing_surface.append([])
for i in range(8):
    for j in range(8):
        playing_surface[i].append([])
    for j in range(8):
        playing_surface[i][j].append("-")

def score(a):
    score=0
    if "a" in a:
        score+=1*(a.count("a"))
    if "b" in a:
        score+=3*(a.count("b"))
    if "c" in a:
        score+=3*(a.count("c"))
    if "d" in a:
        score+=2*(a.count("d"))
    if "e" in a:
        score+=1*(a.count("e"))
    if "f" in a:
        score+=4*(a.count("f"))
    if "g" in a:
        score+=2*(a.count("g"))
    if "h" in a:
        score+=4*(a.count("h"))
    if "i" in a:
        score+=1*(a.count("i"))
    if "j" in a:
        score+=8*(a.count("j"))
    if "k" in a:
        score+=5*(a.count("k"))
    if "l" in a:
        score+=1*(a.count("l"))
    if "m" in a:
        score+=3*(a.count("m"))
    if "n" in a:
        score+=1*(a.count("n"))
    if "o" in a:
        score+=1*(a.count("o"))
    if "p" in a:
        score+=3*(a.count("p"))
    if "q" in a:
        score+=10*(a.count("q"))
    if "r" in a:
        score+=1*(a.count("r"))
    if "s" in a:
        score+=1*(a.count("s"))
    if "t" in a:
        score+=1*(a.count("t"))
    if "u" in a:
        score+=1*(a.count("u"))
    if "v" in a:
        score+=4*(a.count("v"))
    if "w" in a:
        score+=4*(a.count("w"))
    if "x" in a:
        score+=8*(a.count("x"))
    if "y" in a:
        score+=4*(a.count("y"))
    if "z" in a:
        score+=10*(a.count("z"))
    return score
def display():
    for i in range(8):
        print(playing_surface[i])
def letter_generator():
    a=""
    for i in range(5):
        a+=random.choice(string.ascii_lowercase)
    print(a)
def game():
    def inputs():
        letter_generator()
        word=input("enter your formed word")
        if word not in word_list:
            print("invalid word")
            return 0
        if word in word_list:
            def position():
                orientation=input("horizontal or vertical?")
                row=int(input("enter your row"))
                column=int(input("enter your column"))
                if orientation=="horizontal":
                    if 8-column-len(word)<0:
                        print("invalid word")
                        return 0
                    else:
                        c=column
                        for i in range(len(word)):
                            if playing_surface[row-1][c-1]==['-']:
                                c+=1
                                pass
                            elif playing_surface[row-1][c-1]==word[i]:
                                c+=1
                                pass
                            else:
                                print("invalid word")
                                return 0
                        else:
                            c_=column
                            for i in range(len(word)):
                                playing_surface[row-1][c_-1] = word[i]
                                c_ += 1
                            else:
                                a=score(word)
                                display()
                                return a
                if orientation=="vertical":
                    if 8-column-len(word)<0:
                        print("invalid word")
                        return 0
                    else:
                        r = row
                        for i in range(len(word)):
                            if playing_surface[r-1][column-1] == ['-']:
                                pass
                            elif playing_surface[r-1][column-1] == word[i]:
                                pass
                            else:
                                print("invalid word")
                                return 0
                        else:
                            r_ = row
                            for i in range(len(word)):
                                playing_surface[r_-1][column-1] = word[i]
                                r_ += 1
                            else:
                                a=score(word)
                                display()
                                return a

            a=position()
            return a

    a=inputs()
    return a
p1=0
p2=0
for i in range(2):
    c=game()
    p1+=c
    d=game()
    p2+=d
if p2>p1:
    print(f"p2 wins by {p2-p1} points")
else:
    print(f"p1 wins by {p1-p2} points")

