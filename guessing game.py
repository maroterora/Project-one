print('Welcome to my QUIZZ HAHAHAH!!!!')

playing = input('Are you sure you want to play:   ')

if playing.lower() != "yes":
    quit()

print("Alright let's play :)t")
score = 0

answer = input('What does GPU stand for?:   ')
if answer.lower() == "graphics processing unit":
    print('CORRECT!')
    score += 1
else:
    print('INCORRECT!')

answer = input("What's long,yellow and monkeys love eating it?:   ")
if answer.lower() == "banana":
    print('CORRECT!')
    score += 1
else:
    print('INCORRECT!')

answer = input('Is 96512+61 = 96572?:   ')
if answer.lower() == "no":
    print('CORRECT!')
    score += 1
else:
    print("INCORRECT! It's 96573")

answer = input("Do I have to pee right now?:   ")
if answer.lower() == "yes":
    print('CORRECT! I do. BRB')
    score += 1
else:
    print('INCORRECT! I do. BRB')

print(f'You got {((score/4)*100)} % out of 100%')
