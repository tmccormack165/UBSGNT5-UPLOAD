import sys
infile = open('test.txt', 'r')
txt = infile.read()
txt = txt.split(',')
txt = [elem.strip() for elem in txt]
txt = [f'{elem}: Translation for verb in {elem}' for elem in txt]
for i in range(len(txt)):
    print(txt[i])
