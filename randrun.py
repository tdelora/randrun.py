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
        rr_random.rr_init_rand(randSeed)

    if  not sys.__stdin__.isatty():
        print("\nFile read not implemented")
        exit(1)
    else:
        while count:
            natsNoun = rr_nats_nouns_verbs.rr_get_randon_nats_noun()

            rr_logging.rr_writeWorkLine(natsNoun)
            count-=1


if __name__ == '__main__':
    main()