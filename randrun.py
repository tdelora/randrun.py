import argparse, sys
import rr_random, rr_nats_nouns_verbs, rr_logging

def  main():

    parser = argparse.ArgumentParser()

    parser.add_argument('--maxSteps',default=100, help = "The maximum number of steps to run.")
    parser.add_argument('--randomSeed',default=0, help = "The value to use for random seed.")
    args = parser.parse_args()

    count = int(args.maxSteps)
    randSeed = int(args.randomSeed)

    if randSeed != 0:
        rr_random.init_rand(randSeed)

    if  not sys.__stdin__.isatty():
        readFromFile()
    else:
        generateRandomly(count)
        
    exit(0)


def readFromFile():
    # Done with file variable in case we decide to add a file open down the line
    inputFile = sys.stdin

    line = inputFile.readline()
    while line:
        rr_nats_nouns_verbs.check_execute_nats_noun_verb_line(line)
        line = inputFile.readline()


def generateRandomly(count):
    steps = count
    while steps:
        natsNoun = rr_nats_nouns_verbs.get_randon_nats_noun()

        rr_logging.writeWorkLine(natsNoun)
        steps-=1


if __name__ == '__main__':
    main()
