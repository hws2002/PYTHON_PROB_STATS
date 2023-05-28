
def sum_list(lst):
    total = 0
    for i in lst:
        total += i
    return total

def expectation(lst):
    length = len(lst)
    total = sum_list(lst)
    return total / length

#样本方差
def sample_variance(lst):
    length = len(lst)
    mean = expectation(lst)
    total = sum((x - mean)**2 for x in lst)
    return total / (length - 1)


