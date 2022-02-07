order_list=["-","-","-","-","-","-","-","-","-"]
user_name=str(input("Please Enter Your Name: "))
print("Hello "+str(user_name+", I Want to Play a Game."))
letters_list=[]
correct_word="metallica"
empty_list=[letters_list.append(j) for j in correct_word]
guess_number=10

for i in order_list:
    print(i)
while (True):
    user_guess=str(input("Please Guess a Letter: "))
    if (user_guess==letters_list[0]):
        order_list.pop(0)
        order_list.insert(0,letters_list[0])
        for i in order_list:
            print(i)
        print("Corect Answer!")
        print("Your Chances: ",guess_number)
    if (user_guess==letters_list[1]):
        order_list.pop(1)
        order_list.insert(1,letters_list[1])
        for i in order_list:
            print(i)
        print("Correct Answer!")
        print("Your Chances: ",guess_number)
    if (user_guess==letters_list[2]):
        order_list.pop(2)
        order_list.insert(2,letters_list[2])
        for i in order_list:
            print(i)
        print("Correct Answer!")
        print("Your Chances: ",guess_number)
    if (user_guess==letters_list[3]):
        order_list.pop(3)
        order_list.insert(3,letters_list[3])
        for i in order_list:
            print(i)
        print("Corect Letter!")
        print("Your Chances: ",guess_number)
    if (user_guess==letters_list[4]):
        order_list.pop(4)
        order_list.insert(4,letters_list[4])
        for i in order_list:
            print(i)
        print("Correct Answer!")
        print("Your Chances: ",guess_number)
    if (user_guess==letters_list[5]):
        order_list.pop(5)
        order_list.insert(5,letters_list[5])
        for i in order_list:
            print(i)
        print("Correct Answer!")
        print("Your Chances: ",guess_number)
    if (user_guess==letters_list[6]):
        order_list.pop(6)
        order_list.insert(6,letters_list[6])
        for i in order_list:
            print(i)
        print("Corect Letter!")
        print("Your Chances: ",guess_number)
    if (user_guess==letters_list[7]):
        order_list.pop(7)
        order_list.insert(7,letters_list[7])
        for i in order_list:
            print(i)
        print("Correct Answer!")
        print("Your Chances: ",guess_number)
    if (user_guess==letters_list[8]):
        order_list.pop(8)
        order_list.insert(8,letters_list[8])
        for i in order_list:
            print(i)
        print("Correct Answer!")
        print("Your Chances: ",guess_number)
    if (order_list==letters_list):
        print("Congratulations, You Won")
        break
    if (user_guess not in letters_list):
        print("Wrong Answer!")
        guess_number-=1
        print("Your Chances: ",guess_number)
        for i in order_list:
            print(i)
    if (guess_number==0):
        print("You Died!")
        break
























