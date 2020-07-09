# def my_hash(s):
#     sb = s.encode()

#     sum = 0
#     for b in sb:
#         sum += b

#     return sum % 8


# i = my_hash('steve')


# hash_table = [None]*8

# hash_table[i] = '8 months'


# def get_length_of_time_at_lambda(e):
#     curr_hash = my_hash(e)
#     return hash_table[curr_hash]


# length_steve = get_length_of_time_at_lambda('steve')

# print('Steve has been attending Lambda school for ' + length_steve)


# first we hash value -> constant
# index into the list based on the hash -> constant


# dances = ['Waltz', 'Tango', 'Viennese Waltz', 'Foxtrot',
#           'Cha Cha', 'Samba', 'Rumba', 'Paso Doble', 'Jive']

# for d in sorted(dances):
#     print(d)


# Fib
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
# Recursive

import math
cache = {}


def fib(n):
    if n <= 1:
        return n

    if n in cache:
        return cache[n]

    else:
        cache[n] = fib(n-1) + fib(n-2)

    return cache[n]


# print(fib(50))

# ^^^^^memoization
# dynamic programming
# top-down dynamic programming


# Look-up Table

lookup_table = {}


def inverse_root(n):
    return 1 / math.sqrt(n)


def build_lookup_table():

    for i in range(1, 1000):
        lookup_table[i] = inverse_root(i)


build_lookup_table()

# print(lookup_table[556])
# print(lookup_table[99])
# print(lookup_table[999])


# Sorting
my_list = []

my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)

# why are dictionaries not in order? i.e., order is not guaranteed
# everything hashes differently
# don't know what index the hash function will return

my_list = [5, 3, 4, 2, 6, 7, 8, 1, 9]

d = {
    'Austin': 12,
    'Michael': 24,
    'Troy': 35,
    'Jorge': 99,
    'David': 42
}

# how can we sort our dictionary?

# turn into a list
for pair in d.items():
    print(pair)

# d.items().sort()

print(sorted(d.items()))

sorted_list_of_items = list(d.items())


def named_function(pair):
    return pair[1]


# sorted_list_of_items.sort(reverse=True, key=named_function)
sorted_list_of_items.sort(reverse=True, key=lambda pair: pair[1])

print(sorted_list_of_items)

# List comprehension to sort dict sorted([(v, k) for k, v in d.items()])


# Letter count

# given a string
# return every letter and how many times they occur in a string
# sorted by frequency of occurence

# iterate through our string
# tally the count using a dictionary
# sort our dictionary by the value (i.e. count of each letter)

# upper to lower case everything

def print_letter_count(s):
    count = {}

    s = s.lower()
    for character in s:
        if character >= 'a' and character <= 'z':
            if character not in count:
                count[character] = 1
            else:
                count[character] += 1

    count_list = list(count.items())
    count_list.sort(key=lambda x: x[1], reverse=True)

    for pair in count_list:
        print(f'Count: {pair[1]}, letter: {pair[0]}')


print_letter_count('bunny hop')
