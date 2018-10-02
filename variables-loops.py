import numpy as np #we use numpy for lots o' things

def main():
	i = 0		#declare i equal to 0
	n = 10		#declare n equal to 10
	x = 119.0	#declare x equal to 119.0
	
	# we can use numpy to quickly make arrays
	
	y = np.zeros(n,dtype=float)	#declares 10 zeros as floats using np
	
	# we can use for loops to iterate with a variable
	
	for i in range(n):			#i in range [0,n-1]
		y[i] = 2.0 * float(i) + 1.0	#set y = 2i+1 as floats
		
	# we can also simply iterate through a variable
	for y_element in y:
		print(y_element)
		
#execute the main function
if __name__ == "__main__":
	main()