#declare an array
array_1 = ['1','2','3','4'] 
#append to the last index
array_1.append('1')
array_1.append('1')
#insert somewhere in the array
array_1.insert(4,'0')
#get the length of the array
array_len = len(array_1)
#remove first occurence 
array_1.remove("1")
#get the index in the list
index_of_0 = array_1.index("0")
#count instances of 1 in the list
how_many_1s = array_1.count('1') 
#reverse the list using list.reverse() or list[::-1]
reversed_array = array_1[::-1]
#remove the last 

array_1.pop() 

print(array_1)


# just a simple loop through the list
for element in array_1:
 print (element)

