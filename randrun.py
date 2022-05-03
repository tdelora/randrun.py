import rr_random, rr_nouns_verbs

def  main():

    count = 100
    
    # rr_random.rr_init_rand(10)

    while count:
        natsNoun = rr_nouns_verbs.rr_get_randon_nats_noun()

        print(natsNoun)
        count-=1


if __name__ == '__main__':
    main()