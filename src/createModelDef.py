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

THOMP = {
  "ZTRG":[1,5],
  "ZTR2":[6,13],
  "ZTR3":[14,40]
}

TRENCHGUN = {
  "ZSGG":[1,7],
  "ZSGS":[8,22],
  "ZSGP":[23,34],
  "ZSGR":[35,46]
}

M1911A1 = {
  "Z19G":[1,7],
  "Z19S":[8,15],
  "Z1R1":[16,35],
  "Z1R2":[36,59]
}

GARAND = {
  "M1GG":[1,10],
  "M1GS":[11,18],
  "M1GR":[19,35]
}

FMW41 = {
  "FLMG":[1,1],
  "IFLS":[2,8],
  "FLMF":[9,14]
}

KAR98 = {
  "ZK9G":[1,6],
  "ZK9R":[7,11],
  "ZKR2":[12,27],
  "ZKR1":[28,34],
  "ZK9S":[35,43]
}

def generateFrames(strips):
  for strip in strips:
    j = 65
    for i in range(strips[strip][0], strips[strip][1] + 1):
      print("\tFrameIndex\t{0}\t{1}\t0\t{2}".format(strip, chr(j), i))
      j += 1
    print("")

generateFrames(KAR98)
