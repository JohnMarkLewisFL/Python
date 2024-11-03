# This script prompts the user to enter a range of numbers and generates a random number within that range

# Import selection
import random
import time

# Welcome message
print("This script will generate one random number between the two numbers you specify")
time.sleep(3)

# Defines the function to generate a random number
def random_number_generator():
    while True:
        # Asks the user to input the bottom end and top end of the range
        bottom_number = int(input("\nPlease enter the bottom number of the range: "))
        top_number = int(input("Please enter the top number of the range: "))

        # Generate random number
        random_number = random.randint(bottom_number, top_number)

        # Prints the random number after sleeping for 3 seconds (to add a small level of suspense)
        time.sleep(3)
        print(f"\nThe random number between {bottom_number} and {top_number} is: {random_number}")

        # Prompt the user to run through the script again or exit
        another = input("\nWould you like to generate another random number? (yes/no): ").strip().lower()
        if another not in ('yes', 'y'):
            print("\nThis script will exit shortly")
            time.sleep(3)
            break

if __name__ == "__main__":
    random_number_generator()