#Gowri's calculator
#hackbright day 3
#Exercise 03 from GIT

import arithmetic

#repeat forever:
while True:
	request=raw_input("-->")  #       read input
 
 #       tokenize input
 	calc_string=request.split(" ")
 	calc_string[1] = int(calc_string[1])

 	if len(calc_string) ==3:
 		calc_string[2] = int(calc_string[2])

 #       if the first token is 'q', quit
 	if calc_string[0]=="q":
 		quit
	elif calc_string[0]=="+": #       if the first token is '+', add
		print arithmetic.add(calc_string[1], calc_string[2])

	elif calc_string[0]=="-": #       if the first token is '-', subtract
		print arithmetic.subtract(calc_string[1], calc_string[2])


	elif calc_string[0]=="*": #       if the first token is '*', multiply
		print arithmetic.multiply(calc_string[1], calc_string[2])

	elif calc_string[0]=="/": #       if the first token is '/', divide
		print arithmetic.divide(calc_string[1], calc_string[2])

	elif calc_string[0]=="square": #       if the first token is 'square', square
		print arithmetic.square(calc_string[1])

	elif calc_string[0]=="cube": #       if the first token is 'cube' 
		print arithmetic.cube(calc_string[1])

	elif calc_string[0]=="pow":#       if the first token is 'pow'
		print arithmetic.power(calc_string[1], calc_string[2])

	elif calc_string[0]=="mod":#       if the first token is 'mod',
		print arithmetic.mod(calc_string[1], calc_string[2])

	else:
		print "I do not understand"



	

	


 