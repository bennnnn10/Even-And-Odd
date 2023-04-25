#Vargas, Ruben A.
#BSCPE 1-4
#Object-Oriented Programming

import pyfiglet

def process():
#Open the "numbers.txt" for reading, and "even.txt" and "odd.text" for appending
    with open("numbers.txt") as numbers_txt_file, open("even.txt", "a") as even_txt_file, open("odd.txt", "a") as odd_txt_file:
        #Repeat the input file's lines
        for line in numbers_txt_file:
            numbers = int(line.strip())
            #Check if even
            if numbers % 2 == 0:
                #If even, write it to the even.txt file
                even_txt_file.write(f"{numbers}\n")
            else:
                #If odd, write it to the odd.txt file
                odd_txt_file.write(f"{numbers}\n")
process()

print("*" * 63)
print(pyfiglet.figlet_format("SUCCESSFUL!"))
print("*" * 63)

