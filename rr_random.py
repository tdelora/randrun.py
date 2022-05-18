import random

def init_rand(seed):
    random.seed(seed)

def rand_lim(upperLimit):
    return(random.randint(0,upperLimit))