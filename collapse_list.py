from functools import reduce

def collapse_list(numbers, reverse=False):
    original_length = len(numbers)
    if reverse:
        # Can't reverse a numpy array
        numbers = list(numbers)
        numbers.reverse()
    numbers = reduce(collapse_list_helper, numbers, [])
    numbers.extend([0] * (original_length - len(numbers)))
    if reverse:
        numbers.reverse()
    return numbers

def collapse_list_helper(acc, x):
    if x == 0:
        return acc
    elif not acc and x != 0:
        acc.append(x) 
        return acc
    elif x == acc[-1]:
        acc[-1] += x
        return acc
    else:
        acc.append(x) 
        return acc
