from bruteforce import bruteforce

print("Welcome to Brute Force Attack program!")
password = input("Enter the password to crack (only lowercase alphabets): ")
print("Our program will now attempt to crack the password..")
decision = input("Are you ready for the show? (y/n): ")

if decision == 'y':
    bruteforce(password)
else:
    print("Program cancelled!")