import itertools

'''
_ _ _ _ _
'''

mylist = list(itertools.product("0123456789", repeat=4))
print(mylist)
print(len(mylist))


