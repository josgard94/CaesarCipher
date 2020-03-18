"""
	Author: Edgard Diaz
	Date: 17th march 2020	
	This code performs the encryption of a text file using Cesar encryption.


"""

from files import files
from CesarEncryption import Encryption
from os import system, name
import sys
    


# define our clear function 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')


if __name__ == '__main__':

	#create objects from class
	obj_File = files()
	obj_Encryption = Encryption()
	state = True
	flag = True
	#print options menu
	print("\n\nEncrypt and decrypt text files using Caesar encryption.")
	while state:
		print("\nSelect an option:\n\n\t1).- Encript text \n\t2).- Encrypt text \n\t3).-Exit")
		
		opt = int(input("Enter option: "))
		if opt == 1: 
			try:
				clear();
				fileName = input("File name: ")
				Text = obj_File.UploadTextFile(fileName)
				shift = int(input("Number of letters to move the text:  "))
				TextEncryp = obj_Encryption.EncrypText(Text,shift)
				print(obj_File.WriteFile(TextEncryp,fileName,'e'))
				
				state = False
			except ValueError:
				clear();
				print('\n\nError: must be a numeric value\n\n')
				state = True
			except FileNotFoundError:
				clear();
				print('Error: file no fund')
		elif opt == 2: 
			try:
				clear();
				fileName = input("File name: ")
				Text = obj_File.UploadTextFile(fileName)
				shift = int(input("Number of letters to move the text:  "))
				TextDecryp = obj_Encryption.DecrypText(Text,shift)
				obj_File.WriteFile(TextDecryp,fileName,'d')
				state = False
			except ValueError:
				clear();
				print('\n\nError: must be a numeric value\n\n')
				state = True
			except FileNotFoundError:
				clear();
				print('Error: file no fund')
		elif opt == 3:
			state = False
			flag = False
			print('The program has finished executing, because the exit option has been chosen.')
			sys.exit()
		else:
			clear();
			print("\n\nError: Invalid option\n\n")