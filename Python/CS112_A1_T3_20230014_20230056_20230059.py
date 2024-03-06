# Program: The user is allowed to use six programs: 
# the first is a program that converts grades into grades, 
# the second is a program that checks whether the number is Armstrong, 
# the third is a program that calculates the approximate value of pi, 
# the fourth is a program that helps encrypt in a way Caesar Cipher, 
# the fifth is a program that compares two lists and sees whether they are equal or not, 
# the sixth is a program, and the last gives you the factors of the integer number that His intervention

# Authors: Islam Hassan Galabi Salem_20230059 Solved Problem 1,2
#          Ahmed Hassan Abdel Hamed_20230014 Solved Problem 3,4
#          Islam Ahmed Salah Dawood_20230056 Solved Problem 5,6

# Version: 1.0
# Date: 26/2/2024

def main():
    while True:    
        #Menu_1
        print("\n==============**Wlecome in the our program**===============\n")
        print("A) Enter a Program")
        print("B) Exit a program\n")
        
        #Check Valid choice
        while True:
            num_choice = input("Enter your choice (A/B) : ").upper()
            if num_choice == 'A' or num_choice == 'B':
                break
            else:
                print("Please enter a valid chioce.")

        #Start a program
        if num_choice == 'A':
        
            print("===========================================================")
            #Menu_2
            print("\nA) Grade Conversion Program")
            print("B) Check Number Armstrong")
            print("C) Calculate Approximation of π")
            print("D) Encrypted Version Cesar Cipher")
            print("E) Compare Between Two Lists Whether They are Equal or Not")
            print("F) Find Factors For Integer Number\n")

            #Check Valid choice
            while True:
                number_choice = input("Enter your choice (A/B/C/D/E/F) : ").upper()
                if number_choice == 'A' or number_choice == 'B' or number_choice == 'C' or number_choice == 'D' or number_choice == 'E' or number_choice == 'F':
                    break
                else:
                    print("Please enter a valid chioce.")
                
            if number_choice == 'A':
                convert_grade()
                print("\nThanks you for trying our program")
            elif number_choice == 'B':
                is_armstrong()
                print("\nThanks you for trying our program")
            elif number_choice == 'C':
                calculate_approximation_of_π()
                print("\nThanks you for trying our program")
            elif number_choice == 'D':
                encrypt_text()
                print("\nThanks you for trying our program") 
            elif number_choice == 'E':
                are_lists_equal()
                print("\nThanks you for trying our program")
            elif number_choice == 'F':
                find_factors()
                print("\nThanks you for trying our program")   
        
        #Exiting program
        else:
            print("\nExiting Program !")
            break
        
def convert_grade():
    print("===========================================================\n")
    while True:
        try:
            mark = int(input("Enter the mark : "))

            if mark >= 90:
                grade = "A+"
            elif mark >= 85:
                grade = "A"
            elif mark >= 80:
                grade = "A-"
            elif mark >= 75:
                grade = "B+"
            elif mark >= 70:
                grade = "B"
            elif mark >= 65:
                grade = "B-"
            elif mark >= 60:
                grade = "C+"
            elif mark >= 55:
                grade = "C"
            elif mark >= 50:
                grade = "C-"
            else:
               grade = "F"

            print(f"Grade: {grade}")
            break

        except ValueError:
            print("Please enter the correct number.")

def is_armstrong():
   print("===========================================================\n")
   while True:
       try:
           num = int(input("Enter a number: "))
           
           # Count the number of digits
           num_str = str(num)
           num_digits = len(num_str)

           # Calculate the sum of each digit raised to the power of the number of digits
           armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
           
           # Check if the sum is equal to the original number
           
           
           if armstrong_sum == num:
               print(num, "is an Armstrong number\n")
           else:
               print(num, "is not an Armstrong number\n")
           break  # Exit the loop if input is valid
       except ValueError:
           print("Please enter the correct numbers")
     
def calculate_approximation_of_π():
    print("===========================================================\n")
    total_sum = 0
    while True:
        try:
           terms = int(input("Enter the number of terms to consider: "))
           for i in range(terms):
              term = (-1) ** i / (2 * i + 1)
              total_sum += term
           pi_approximation = total_sum * 4
           print(f"Approximation of π using {terms} terms: {pi_approximation:.15f}")
           break
        except ValueError:
              print("Invalid input. Please enter a positive integer.")
                 
def encrypt_text():
    print("===========================================================\n")
    n = 1
    text_before_encrypt = input("Enter what you want to encrypt: ")
    answar = ""

    # iterate over the given text
    for i in range(len(text_before_encrypt)):
        char = text_before_encrypt[i]
        
        # check if space is there then simply add space
        if char==" ":
            answar+=" "
            
        # check if a character is uppercase then encrypt it accordingly 
        elif (char.isupper()):
            answar += chr((ord(char) + n-65) % 26 + 65)
            
        # check if a character is lowercase then encrypt it accordingly
        else:
            answar += chr((ord(char) + n-97) % 26 + 97)
            
    print(f"Cipher Text is : {answar}")

def are_lists_equal():
    print("===========================================================\n")
    print("Note !! That Space are calculated with the list\n") 
    
    # Check ValueError
    while True:
        try:
            list1 = input('Enter elements of a list1 separated by space:\n')
            
            # Check Enter number and space only
            if  all(c in "0123456789 " for c in list1) == True:  
                break
            else:
                print("Please Enter number not thing other!\n")
        except ValueError:
            break
    
    # Check ValueError
    while True:
        try:           
            list2 = input('Enter elements of a list2 separated by space:\n')
            
            # Check Enter number and space only
            if  all(c in "0123456789 " for c in list2) == True:  
                break
            else:
                print("Please Enter number not thing other!\n")
        except ValueError:
            break
    
    user_list1 = list1.split()
    user_list2 = list2.split()
    
    for i in range(len(user_list1)):
     
        # convert each item to int type
        user_list1[i] = int(user_list1[i])
    
    for i in range(len(user_list2)):
     
        # convert each item to int type
        user_list2[i] = int(user_list2[i])
        
    


    # Create a copy of list2 to avoid modifying the original list
    temp_list2 = list(list2)

    
    # Iterate over each element in list1
    for item in list1:
        
        # Check if the lengths of the lists are different
        if len(list1) != len(list2):
           print(f"\nList are equal = {False}")
           break
        
        # Check if the element is in temp_list2
        if item in temp_list2:
            
            # If all elements in list1 are found in list2, and both lists are of the same length,
            # then the lists have the same elements
            print(f"\nList are equal = {True}")            
            break
        else:
            
            # If an element from list1 is not in temp_list2, the lists are not equal
            print(f"\nList are equal = {False}")
            break

def find_factors():
    print("===========================================================\n")
    #Check ValueError
    while True:
        try:
            num1 = int(input("Please Enter The Integer Number You Want To Factor: "))
            int(num1)
            break
        except ValueError:
            print("\nPlease Enter Integer Number!")
    
    # Initialize an empty list to store factors       
    factors = []  
    
    # negtive integer number
    if num1 < 0:
        # Iterate from 1 to num1 (inclusive)
        for i in range(1, (-num1) + 1):
            
            # Check if i divides num1 evenly
            if num1 % i == 0: 
                
                # If it does, add i to the factors list
                factors.append(i)  
    
    # negtive integer number
    if num1 > 0:
        # Iterate from 1 to num1 (inclusive)
        for i in range(1, num1 + 1):

            # Check if i divides num1 evenly
            if num1 % i == 0:  
                
                # If it does, add i to the factors list
                factors.append(i)  
    print(f"The factors of {num1} are: {factors}")

main()