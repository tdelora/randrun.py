import rr_random

rr_nats_nouns = ("NATS_CONNECTION", "NATS_PUBLISHER", "NATS_SUBSCRIBER")

def rr_get_randon_nats_noun():
    nounRand = rr_random.rr_rand_lim(len(rr_nats_nouns)-1)
    return rr_nats_nouns[nounRand]