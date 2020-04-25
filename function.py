# import sys

# global_list= ["kevin", "thea"]


# def function_kevin(n):
 
#  if n==global_list[0]:
#  	# print("The name of the script being executed is : " + sys.argv[0])
#  	print ("The argument passed in this function is " + n)
#  	local_list = ['1','2']
#  	return local_list
#  return False


# function_return_variable = function_kevin("kevin")	

# print("The function returned ")


def separateFunction(b):
	for i in b:
		print (i)
		if i == 1:
			print ('saw a match')
		# return False
	print ('im outside the loop')	
separateFunction([2,3,5,6,1])