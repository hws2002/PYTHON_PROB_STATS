import numpy as np

def normal_random_number_generator(mean = 0,std = 1):
    numbers = np.random.uniform(0,1,size=12)
    y = np.sum(numbers) - 6
    z = mean + y * std
    return z