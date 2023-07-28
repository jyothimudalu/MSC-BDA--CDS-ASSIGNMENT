import timeit
def print_square(x):
    return x ** 2

#start
t0 = timeit.default_timer()

#call_function
result = print_square(11111111)

#end
t1 = timeit.default_timer()

# calculate elapsed time and print
elapsed_time = round((t1 - t0) * 10 ** 6, 3)
print(f"Elapsed time: {elapsed_time} µs")
