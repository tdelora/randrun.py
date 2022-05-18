import rr_constant


def writeWorkLine(line):
    print("{}{}".format(rr_constant.RR_LOG_WORK_PREPEND,line))

def writeErrorLine(line):
    print(line)

def writeOutputLine(line):
    print(line)
