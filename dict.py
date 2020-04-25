state_capitals = {
 'Arkansas': 'Little Rock',
 'Colorado': 'Denver',
 'California': 'Sacramento',
 'Georgia': 'Atlanta',
 'Philippines': ['Manila', 'Davao', 'Cebu']
}

state_capitals['Arkansas'] = 'test' # dict are immutable so this line will not take effect


print(state_capitals.keys()) 

# #.format() is just like sprintf
# for k in state_capitals.keys():
# 	print('{} is the capital of {}, btw this is {}'.format(state_capitals[k], k, 'just an extra'))