STG44 = {
    "ZSTS":[1,12],
    "ZSTG":[13,18],
    "ZSTR":[19,24],
    "ZSR2":[25,28],
    "ZSR3":[29,41],
    "ZSR4":[42,50]
}

MG42 = {
    "ZMGS":[1,12],
    "ZMGG":[13,18],
    "ZMGR":[19,30],
    "ZGR0":[31,47],
    "ZGR1":[48,73],
    "ZGR2":[74,97]
}

def generateFrames(strips):
    for strip in strips:
        j = 65
        for i in range(strips[strip][0], strips[strip][1] + 1):
            print("\tFrameIndex\t{0}\t{1}\t0\t{2}".format(strip, chr(j), i))
            j += 1
        print("")

generateFrames(MG42)
