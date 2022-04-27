import random

def rr_init_rand(seed):
    random.seed(seed)

def rr_rand_lim(upperLimit):
    return(random.randint(1,upperLimit))