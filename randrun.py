import rr_random

def  main():

    count = 100
    
    # rr_random.rr_init_rand(10)

    while count:
        rNum = rr_random.rr_rand_lim(9)

        print(rNum)
        count-=1


if __name__ == '__main__':
    main()