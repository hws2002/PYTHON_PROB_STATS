# ideal coin toss
import random

def toss_coin(num_tosses):
    num_heads = 0
    for _ in range(num_tosses):
        result = random.choice(["Heads", "Tails"])
        if result == "Heads":
            num_heads += 1
    return num_heads


def calculate_probability_ideal(num_tosses, num_experiments):
    delta = 0
    total_heads = 0
    for _ in range(num_experiments):
        num_heads = toss_coin(num_tosses)
        total_heads += num_heads
        print(f"Number of heads in {num_tosses} tosses: {num_heads} | Probability : {num_heads/num_tosses}")
        if (delta < abs(num_heads/num_tosses - 0.5)):
            delta = abs(num_heads/num_tosses - 0.5)
    probability = total_heads / (num_tosses * num_experiments)
    return probability,delta


# realistic coin toss
import numpy as np


def simulate_coin_tosses(num_tosses):
    outcomes = np.random.choice(['H', 'T'], size=num_tosses)
    num_heads = np.count_nonzero(outcomes == 'H')
    num_tails = np.count_nonzero(outcomes == 'T')
    return num_heads, num_tails


def calculate_probability(num_tosses,num_experiment):
    total_heads = 0
    for i in range(num_experiment):
        num_heads, _ = simulate_coin_tosses(num_tosses)
        total_heads += num_heads
        print(f"Number of heads in {num_tosses} tosses: {num_heads} | Probability : {num_heads/num_tosses}")
    probability = total_heads / (num_experiment*num_tosses)
    return probability

def collect_data(number_toss,number_experiment,eps = 0.01, p = 0.5):
    total_excess  = 0
    for _ in range(number_experiment):
        num_heads,_ = simulate_coin_tosses(number_toss)
        if(num_heads/number_toss > p+eps or num_heads/number_toss < p-eps): # has a 25% of happening
            total_excess += 1
    return total_excess

def calculate_prob_supremum(number_toss,esp = 0.01, p = 0.5):
    return (p * (1-p) / (number_toss * esp**2))
