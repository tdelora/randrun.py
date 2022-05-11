import rr_constant


def rr_writeWorkLine(line):
    print("{}{}".format(rr_constant.RR_LOG_WORK_PREPEND,line))

def rr_writeErrorLine(line):
    print(line)

def rr_writeOutputLine(line):
    print(line)
