# CaesarCipher

	Author: Edgard Diaz
	Date: 17th march 2020	
	
	In this project I develop a plaintext file encryption using shift encryption or César encryption, 
	this project was implemented in   the Python programming language.

	To perform the Caesar cipher, the alphabet can be represented by modular arithmetic 
	by first transforming the letters into numbers, as shown below, A → 0, B → 1, ..., Z → 25. 
	Based on this, you can perform encryption of a letter x using an n-letter offset, 
	and such encryption can be described mathematically as (1):

						E_n(x)  = (x + n) % 61					(1)

	The decryption process is performed in a similar way using (2)

						D_n(x) = (x - n) % 61					(2)
						
	It is worth mentioning that the cipher considers the use of an alphabet of letters 
	from A to Z lowercase and uppercase, as well as the numbers from zero to nine.
