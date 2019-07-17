announce = '''If you guess the answer 
you will get the cash price. you will be given only 3 guesses'''
print (announce)
begin = input("do you want to start playing? Yes/No: ")
if begin == "Yes":
    print(" Here is the question:")
    print("What is always coming, but never arrives?")
    guess_count = 3
    guess_made = 0
    while guess_made < guess_count:
        guess= input("Guess: ")
        if guess == "tomorrow":
            print(" You Win!!!")
            print(" you are good in guessing riddle")
            print (" you have got $3, Congratz")
            break
        guess_made += 1
    else :
        print(" Sorry")
        print(" You have Failed")
else:
    print(" Have a good Day")
    print(" GoodBye")        






