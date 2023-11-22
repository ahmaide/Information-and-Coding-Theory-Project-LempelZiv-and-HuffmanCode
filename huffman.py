import random
import math

class Symbol:
    def __init__(self, char, probability):
        self.char = char
        self.probability = probability
        self.codeword=''

class Node:
    def __init__(self, probability, elements):
        self.elements=elements
        self.probability = probability

input=open("input.txt", "r")
data = input.read().splitlines()
input.close()
symbols={}
nodes=[]
for i in range(len(data)):
    element=data[i].split()
    sym= Symbol(element[0], float(element[1]))
    symbols[element[0]]=(sym)
    ele=[]
    ele.append(sym)
    node=Node(sym.probability, ele)
    nodes.append(node)

nodes = sorted(nodes, key=lambda x:x.probability, reverse=True)

while len(nodes) > 2:
    ele=nodes[len(nodes)-1].elements.copy()
    ele.extend(nodes[len(nodes)-2].elements)
    prob = nodes[len(nodes)-1].probability + nodes[len(nodes)-2].probability
    for element in nodes[len(nodes)-1].elements:
        element.codeword = '1' + element.codeword

    for element in nodes[len(nodes)-2].elements:
        element.codeword = '0' + element.codeword

    newNode=Node(prob, ele)

    nodes.pop()
    nodes.pop()
    nodes.append(newNode)
    nodes = sorted(nodes, key=lambda x: x.probability, reverse=True)

for element in nodes[0].elements:
    element.codeword = '0' + element.codeword

for element in nodes[1].elements:
    element.codeword = '1' + element.codeword

symbols2={}
for key, value in symbols.items():
    print(key, value.codeword)
    symbols2[key]=value.probability

random_sequence = random.choices(list(symbols2.keys()), list(symbols2.values()), k=100)
random_sequence= ''.join(random_sequence)

print("\nRandom String:")
print(random_sequence)
FinalCodeword=''

for r in random_sequence:
    FinalCodeword = FinalCodeword+symbols[r].codeword
print("\nRandom String Code Word:")
print(FinalCodeword)

Nb=len(FinalCodeword)
print("\nSize of encoded sequence:", Nb)

Ratio=Nb/800
print("\nCompression Ratio:", Ratio)

nOfBits=Nb/100
print("\nNumber of bits per symbol:", Ratio, "b/s")