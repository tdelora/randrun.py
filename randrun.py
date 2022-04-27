import rr_random

def  main():

    count = 100

    while count:
        rNum = rr_random.rr_rand_lim(9)

        print(rNum)
        count-=1


if __name__ == '__main__':
    main()