import itertools
import time

def bruteforce(password):
    possible = 'abcdefghijklmnopqrstuvwxyz'
    attempts = 0
    found = False
    start_time = time.time()

    for combination in itertools.product(possible, repeat=len(password)):
        guessed_password = ''.join(combination)
        print(f"Cracking.. {guessed_password}")
        attempts += 1

        if guessed_password == password:
            found = True
            end_time = time.time()
            time_taken = end_time - start_time
            print()
            print(f"PASSWORD FOUND!: {guessed_password}")
            print(f"Total attempts: {attempts}")
            print(f"Time taken: {round(time_taken, 2)} seconds")
            break
    
    if not found:
        print("Password not found")