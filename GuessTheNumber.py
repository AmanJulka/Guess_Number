number=9
chances=1
is_guess=True
while is_guess and chances<=3:
    guess=int(input("Guess: "))
    if guess==number:
        print("You Win!")
        is_guess=False
    else:
        chances-=1
if chances==0:
    print("You Lose!")