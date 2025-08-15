"""
OPCION NORMAL

def square_numbers(nums):
    result = []
    for i in nums:
        result.append(i*i)
    return result

my_nums = square_numbers([1,2,3,4,5])

print(my_nums)
"""
#imprime la lista: [1,4,9,16,25] 
"""
#GENERADOR 
def square_numbers(nums):
    for i in nums:
        yield (i*i)

my_nums = square_numbers([1,2,3,4,5])

for num in my_nums:
    print(num)
"""    
"""
imprime:
1
4
9
16
25
"""




