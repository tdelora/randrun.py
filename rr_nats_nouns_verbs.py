import rr_constant, rr_logging, rr_random


rr_nats_nouns = ("NATS_INIT", "NATS_CONNECTION", "NATS_PUBLISHER", "NATS_SUBSCRIBER")

def get_randon_nats_noun():
    nounRand = rr_random.rand_lim(len(rr_nats_nouns)-1)
    return rr_nats_nouns[nounRand]

def genex_random_nats_noun_verb():
    natsNoun = get_randon_nats_noun()
    execute_nats_noun_verb_line(natsNoun)

def check_execute_nats_noun_verb_line(line):
    if line.find(rr_constant.RR_LOG_WORK_PREPEND,0) != -1:
        start = len(rr_constant.RR_LOG_WORK_PREPEND)
        execute_nats_noun_verb_line(line[start::])
        
def execute_nats_noun_verb_line(line):

    rr_logging.writeWorkLine(line) 
    print("exec: {}".format(line))
