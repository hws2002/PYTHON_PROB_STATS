import numpy as np

# @PARAM: mean, std (default = 0,1)
# @RETURN: a random number from normal distribution
def normal_random_number_generator(mean = 0,std = 1):
    numbers = np.random.uniform(0,1,size=12)
    y = np.sum(numbers) - 6
    z = mean + y * std
    return z