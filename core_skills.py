import random
# rand_list =

# list_comprehension_below_10 =

# list_comprehension_below_10 =

# random list of numbers
rand_nums = [random.randint(1, 100) for x in range(10)]
print(rand_nums)

#Filter Numbers Below 10 (List Comprehension)
print([num for num in rand_nums if num<10])
