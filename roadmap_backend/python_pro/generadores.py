# OPCION NORMAL
def square_numbers_lista(nums):
    result = []
    for i in nums:
        result.append(i*i)
    return result

my_nums = square_numbers_lista([1,2,3,4,5])

print(f'Imprimiendo "my_nums": {my_nums}')

#GENERADOR 
def square_numbers_generador(nums):
    for i in nums:
        yield (i*i)

my_nums2 = square_numbers_generador([1,2,3,4,5])

for num in my_nums2:
    print(num)
