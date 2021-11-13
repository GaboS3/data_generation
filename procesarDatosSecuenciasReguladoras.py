import sys

def getConsensusFile(file):
    with open(file) as f:
        while True:
            title = f.readline().strip()
            if title == "":
                break
            l1 = f.readline()
            l2 = f.readline()
            l3 = f.readline()
            l4 = f.readline()
            getConsensus(l1, l2, l3, l4, title)

def getConsensus(l1, l2, l3, l4, title):

    arrayA =[int(s) for s in str.split(l1) if s.isdigit()]
    arrayC =[int(s) for s in str.split(l2) if s.isdigit()]
    arrayG =[int(s) for s in str.split(l3) if s.isdigit()]
    arrayT =[int(s) for s in str.split(l4) if s.isdigit()]

    consensus = ""

    for i in range(len(arrayA)):
        value = max(arrayA[i], arrayC[i], arrayG[i], arrayT[i])
        if (value==arrayA[i]):
            consensus += 'A'
        elif (value==arrayC[i]):
            consensus += 'C'
        elif (value==arrayG[i]):
            consensus += 'G'
        elif (value==arrayT[i]):
            consensus += 'T'

    if(len(consensus)<=16):
        print(title)
        print(consensus)

getConsensusFile(sys.argv[1])

            
