def mean(nums):
    return sum(nums) / len(nums) if nums else 0.0

def is_prime(n: int) -> bool:
    if n < 2: return False
    for d in range(2, int(n**0.5)+1):
        if n % d == 0: return 
    return True

def median(nums):
    n = len(nums)

    if len(nums) % 2 == 0:
        i = n // 2
        avg = (nums[i - 1] + nums[i]) / 2
        return avg
    else:
        med = nums[n // 2]
        return med