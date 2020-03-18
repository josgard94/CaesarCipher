"""
	Author: Edgard Diaz
	Date: 18th March 2020

	In this class, the methods of encrypting and decrypting the plain 
	text file using modular arithmetic are implemented to move the original 
	message n times and thus make it unreadable in the case of encryption, 
	the same process is performed for decryption using the file containing the 
	encrypted text and scrolled n times to retrieve the original text.

	In the alphabet the use of lowercase and capital letters is considered as 
	well as the numbers from zero to nine.
	
"""


import string
class Encryption:

	
	def EncrypText(self, PlaneText, n):
		EncrypT = "";
		EncrypTxt = self.TextToNumber(PlaneText)
		i = 0;
		
		while i < len(EncrypTxt):
			aux = EncrypTxt[i]
	
			try:
				x = int(EncrypTxt[i])
				if x >= 0 or x <= 60:
					E_n = ((x - n) % 61)
					#print(E_n)
					letter = self.NumberToText(E_n)
					EncrypT += letter
				i += 1;
			except ValueError:
				#i += 1;
				EncrypT += aux
				i += 1;
		return EncrypT

	def DecrypText(self, EncrypTxt, n):
		Text = ""
		StringNumber = self.TextToNumber(EncrypTxt)

		i = 0;
		
		while i < len(StringNumber):
			aux = StringNumber[i]
	
			try:
				x = int(StringNumber[i])
				if x >= 0 or x <= 60:
					D_n = ((x + n) % 61)
					letter = self.NumberToText(D_n)
					Text += letter
				i += 1;
			except ValueError:
				#i += 1;
				Text += aux
				i += 1;
		return Text



	def NumberToText(self,Number):

		letter = 'abcdefghijklmnopqrstuvwxyzABCDFGHIJKLMNOPQRSTUVWXYZ0123456789'

		return letter[Number]


	def TextToNumber(self,Text):
		NumberString = []
		letter = 'abcdefghijklmnopqrstuvwxyzABCDFGHIJKLMNOPQRSTUVWXYZ0123456789'
		i = 0
		for c in Text:
			#c = Text[i]
			if c in letter:
				#NumberString[i] = str(letter.index(c))
				NumberString.append(str(letter.index(c)))
			else:
				NumberString.append(c);
			i += 1;
		return NumberString

