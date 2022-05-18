import rr_random

rr_nats_nouns = ("NATS_INIT", "NATS_CONNECTION", "NATS_PUBLISHER", "NATS_SUBSCRIBER")

def get_randon_nats_noun():
    nounRand = rr_random.rand_lim(len(rr_nats_nouns)-1)
    return rr_nats_nouns[nounRand]

def check_execute_nats_noun_verb_line(line):
    print(line,end="")



