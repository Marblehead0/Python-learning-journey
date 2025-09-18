from util_math import mean, is_prime,median
import statistics

data = [3,5,7,10]
print("mean: ",mean(data))
print("primes in data: ", [x for x in data if is_prime(x)])
print("median: ", median(data))
