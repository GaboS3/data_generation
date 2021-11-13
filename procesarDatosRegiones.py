import sys

def organize(file):
    count = 1
    with open(file) as f:

        first = True

        while True:  
            a = f.readline().strip('\n').strip('n')
            if(a==""):
                print(sequence)
                break
            elif(a[0]=='>'):
                if(not first):
                    print(sequence)
                    sequence=""
                else:
                    first = False
                    sequence=""
                print(">Sequence" + str(count))
                count = count + 1
            else:
                sequence=sequence+a

organize(sys.argv[1])