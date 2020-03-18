"""
	Author: Edgard Diaz
	Date: 17th March 2020

	This class implements the methods used to read and write the 
	plaintext files that are processed by the encryption algorithm.

"""
import os
class files:

	def UploadTextFile(self, path):
		File = ""
		PlaneText = ""
		try:
			File = open(path)
			PlaneText = (File.read().rstrip())
			File.close()
			return PlaneText
		except ValueError:
			print ("File or path not found.")
	def WriteFile(self, Text,OriginalFileName,opt):

		if opt == 'e':
			OriginalFileName = OriginalFileName.replace(".txt","_")
			FileName = OriginalFileName + "Encrypted.txt"
			
			try:
				FileToWrite = open(FileName, 'w+')
				FileToWrite.write(Text)
			except ValueError:
				print(ValueError)

			return 'file encryption completed successfully'
		elif opt == 'd':

			FileName = "Text_decrypted.txt"
			
			try:
				FileToWrite = open(FileName, 'w+')
				FileToWrite.write(Text)
			except ValueError:
				print(ValueError)

			return 'file decryption completed successfully'
