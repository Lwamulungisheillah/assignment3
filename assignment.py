import numpy as np
# 2 .sum of list
#let the list be b
b=(8,2,3,0,7)
print(sum(b))

# 3. multiply the numbers in the list
sample_list=(8,2,3,-1,7)
multiplication_of_sample_list=(8*2*3*-1*7)
print(multiplication_of_sample_list)

# 4.reverse the string below
the_list="1234abcd" [::-1]
print(the_list)

# 8. function that takes a list and returns a new list with distinct elements from the first list.
first_list=[1,2,3,3,3,3,4,5]
def my_function(s):
    return list(dict.fromkeys(s))

first_list = my_function([1,2,3,3,3,3,4,5])

print(first_list)
