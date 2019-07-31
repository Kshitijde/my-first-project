data=("Being able to effectively perform mathematical operations in programming is an important skill to develop because of how"
      " frequently you’ll be working with numbers. Though a high-level understanding of mathematics can certainly help you become"
      " a better programmer, it is not a prerequisite. If you don’t have a background in mathematics, try to think of math as a tool"
      " to accomplish what you would like to achieve, and as a way to improve your logical thinking.")
count=0
last_word=data.split()[-1]
last_word_number=data.split().index(last_word)
for i in 'abcdefghijklmnopqrstuvwxyz':
    for j in range(last_word_number):
        count+=data.split()[j][0].count(i)
    print(f"number of words starting with {i} are {count}")
    count=0