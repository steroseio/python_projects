secret_number = 7
guess_count = 0
guess_max = 3

while guess_count < guess_max:
   user_guess = int(input("Take a Guess: "))
   guess_count += 1
   #print(guess_count)
   if user_guess == secret_number:
       print(f"Well done, the secret number is {secret_number}.")
       break
else:
    print("Too bad, you ran out of guesses.")