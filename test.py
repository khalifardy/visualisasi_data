def odd_sum(min, max):
    total = 0
    for i in range(min,max+1):
        if i%2 != 0:
            total += i
    
    return total

print(odd_sum(4,15))