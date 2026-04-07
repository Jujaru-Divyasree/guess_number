import random
print ('welcome to guess number game !\nyou have 5 chances to guess the  number')

num = random.randint(1, 50)
chance = 5
gc = 0
i=0
while chance > gc:
    gc +=1
    guess = int(input('guess the number between 1 and 50 : '))
    if guess == num :
        print ('congratulation you win! ,at attempt number : ',gc)
        break
    elif chance == gc and guess !=num :
        print ('sorry you lose ! the number is : ',num)       
    elif guess < num :
        print ('too low ')
    elif guess > num :
        print ('too high ')
        """ elif chance == gc and guess !=num :
        print ('sorry you lose ! the number is : ',num)       """
for (i) in range(1, chance + 1) :
    print(i)


'''add print statement for advising for playing different python games'''
print("hello have interest to play python program games")
print("hangman game ")

