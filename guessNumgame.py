import random
secret_num = random.randint(1, 10)
max_attemp = 3

def welcom_massage():
    print("welcome to the game!")
    print(f"you have {max_attemp} attemp to guess!")

def guess_recursive(attemp_left):
    guess = int(input("guess a number between 1 - 10"))

    if guess == secret_num:
        print("congratulations! u have guessed correct no.")
    else:
        print("wrong guess! try again!")
        print(f"attempts left: {attemp_left -1}")
        if attemp_left > 1:
            guess_recursive(attemp_left -1)
        else:
            print(f"sorry out of attempts! correct answer is {secret_num}.")

welcom_massage()
guess_recursive(max_attemp)

print(f"memory address {secret_num}is : {id(secret_num)}")
