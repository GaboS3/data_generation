import random
import sys

#Se ingresa por linea de comandos los siguientes valores: número de secuencias a generar, archivo con regiones de genes, archivo con secuencias reguladoras a insertar
#Archivo para guardar las secuencias, archivo para guardar la información de las secuencias reguladoras insertadas
#Ejemplo: .\generarDatasetSintetico.py 2000 regions.txt motifs.txt dataset2000.txt motifs2000.txt

def selectSequences(cant, sequences):
    with open(sequences) as fileS:
        seqs=[]
        titles=[]
        while True:
            a = fileS.readline().strip('\n')
            if(a==""):
                break
            titles.append(a)
            b = fileS.readline().strip('\n')
            seqs.append(b)
        
        selectSeqs=[]
        selectTitles=[]

        positions = random.sample(range(len(seqs)-1), int(cant))

        for i in positions:
            selectSeqs.append(seqs[i])
            selectTitles.append(titles[i])

        fileS.close()

    return selectSeqs, selectTitles

def selectMotifs(motifs):
    with open(motifs) as fileM:
        mots=[]
        titles=[]
        while True:
            a = fileM.readline().strip('\n')
            if(a==""):
                break
            titles.append(a)
            b = fileM.readline().strip('\n')
            mots.append(b)

        selectMots=[]
        selectTitles=[]

        positions = random.sample(range(len(mots)-1), 5)

        for i in positions:
            selectMots.append(mots[i])
            selectTitles.append(titles[i])
        
        fileM.close()

    #with open("motifs5000.txt", 'w') as f: #ejemplo
    with open(sys.argv[5], 'w') as f:
        sys.stdout = f
        for i in range(len(selectMots)):
            print(selectTitles[i])
            print(selectMots[i])
        f.close()
    
    return selectMots

def generateDataset(sequences, motifs, seqTitles):

    finalSequences=[]

    for seq in sequences:

        cuts, size = len(seq), len(seq)//5
        subs = [ seq[i:i+size] for i in range(0, cuts, size) ]

        arrs = [0,1,2,3,4]

        if(random.random()>0.1):
            arr = random.choice(arrs)
            pos = random.randrange(len(subs[arr])-1)

            begin = subs[arr][:pos]
            end = subs[arr][pos:]

            lenM = len(motifs[0])

            if(len(begin)>lenM):
                newBegin = begin[:len(begin) - lenM]
                subs[arr] = "".join((newBegin, motifs[0], end))
            else:
                newEnd = end[lenM:]
                subs[arr] = "".join((begin, motifs[0], newEnd))
            arrs.remove(arr)

        if(random.random()>0.2):
            arr = random.choice(arrs)
            pos = random.randrange(len(subs[arr])-1)

            begin = subs[arr][:pos]
            end = subs[arr][pos:]

            lenM = len(motifs[1])

            if(len(begin)>lenM):
                newBegin = begin[:len(begin) - lenM]
                subs[arr] = "".join((newBegin, motifs[1], end))
            else:
                newEnd = end[lenM:]
                subs[arr] = "".join((begin, motifs[1], newEnd))
            arrs.remove(arr)

        if(random.random()>0.3):
            arr = random.choice(arrs)
            pos = random.randrange(len(subs[arr])-1)

            begin = subs[arr][:pos]
            end = subs[arr][pos:]

            lenM = len(motifs[2])

            if(len(begin)>lenM):
                newBegin = begin[:len(begin) - lenM]
                subs[arr] = "".join((newBegin, motifs[2], end))
            else:
                newEnd = end[lenM:]
                subs[arr] = "".join((begin, motifs[2], newEnd))
            arrs.remove(arr)

        if(random.random()>0.4):
            arr = random.choice(arrs)
            pos = random.randrange(len(subs[arr])-1)

            begin = subs[arr][:pos]
            end = subs[arr][pos:]

            lenM = len(motifs[3])

            if(len(begin)>lenM):
                newBegin = begin[:len(begin) - lenM]
                subs[arr] = "".join((newBegin, motifs[3], end))
            else:
                newEnd = end[lenM:]
                subs[arr] = "".join((begin, motifs[3], newEnd))
            arrs.remove(arr)

        arr = random.choice(arrs)
        pos = random.randrange(len(subs[arr])-1)
        
        begin = subs[arr][:pos]
        end = subs[arr][pos:]

        lenM = len(motifs[4])

        if(len(begin)>lenM):
            newBegin = begin[:len(begin) - lenM]
            subs[arr] = "".join((newBegin, motifs[4], end))
        else:
            newEnd = end[lenM:]
            subs[arr] = "".join((begin, motifs[4], newEnd))

        finalSequences.append("".join(subs))

    #with open("dataset5000.txt", 'w') as f: #ejemplo
    with open(sys.argv[4], 'w') as f:
        sys.stdout = f
        for i in range(len(finalSequences)):
            print(seqTitles[i])
            print(finalSequences[i].upper())
        f.close()

sequences, seqTitles = selectSequences(sys.argv[1], sys.argv[2])
#sequences, seqTitles = selectSequences(5000, "regions.txt") #ejemplo

motifs = selectMotifs(sys.argv[3])
#motifs = selectMotifs("motifs.txt") #ejemplo

generateDataset(sequences, motifs, seqTitles)