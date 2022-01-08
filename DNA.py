from csv import reader, DictReader #imports python library with the dictreader function
from sys import argv

if len(argv) < 3:
    print("usage error, dna.py sequence.txt database.csv")
    exit()

# read the dna sequence from the file
with open(argv[2]) as dnafile:
    dnareader = reader(dnafile)
    for row in dnareader:
        dnalist = row

# stores into a string
dna = dnalist[0]
sequences = {}


with open(argv[1]) as peoplefile: # extract the sequences from the database into a list
    people = reader(peoplefile)
    for row in people:
        dnaSequences = row
        dnaSequences.pop(0)
        break

for item in dnaSequences:
    sequences[item] = 1

for key in sequences:
    l = len(key)
    tempMax = 0
    temp = 0
    for i in range(len(dna)):
        while temp > 0:
            temp -= 1
            continue

        if dna[i: i + l] == key:
            while dna[i - l: i] == dna[i: i + l]:
                temp += 1
                i += l

            if temp > tempMax:
                tempMax = temp

    sequences[key] += tempMax

with open(argv[1], newline='') as peoplefile:
    people = DictReader(peoplefile)
    for person in people:
        match = 0
        for dna in sequences:  #checks the sequences to every person and determines whether there is a match
            if sequences[dna] == int(person[dna]):
                match += 1
        if match == len(sequences):
            print(person['name'])
            exit()

    print("No match")
