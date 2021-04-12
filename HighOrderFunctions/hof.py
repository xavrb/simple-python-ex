# High order functions
from functools import reduce

#filter


my_list = list(range(1, 1000))
odd = list(filter(lambda x: x%2 !=0, my_list))
print(odd)


# map 
map_list = {1,2,3,4,5}

#using list comprehension
pow2list_lc = [i**2 for i in map_list]
print(pow2list_lc)

# map hof
squares_map = list(map(lambda x: x**2, map_list))
print(squares_map)

#reduce

to_reduce_list = [2]*50

# using a for loop
multip_accum = 1 
for x in to_reduce_list:
    multip_accum = multip_accum * x
print(multip_accum)

#using reduce
multip_accum2 = reduce(lambda a,b: a*b, to_reduce_list)
print(multip_accum2)



