source_text = input('Input Source Text... ')
fh = open(source_text)
dct = {}
for l in fh:
    for chr in l:
        dct[chr] = dct.get(chr, 0) + 1
#print(dct)
fh.close()

fh = open('histogram.csv','w')
fw = open('histogram.txt','w')

num = [[fh.write(f'{v},{k[0]}\n'), fw.write(f'{v},{k[0]}\n')] for k,v in sorted(map(lambda a: (a[1:],a[0]),list(dct.items())),reverse = True)]

fh.close()


#Get and Print
#Sorted Desc
fh = open('histogram.csv')
l = map(lambda a: (a[2:],a[0]),[i for i in fh])

#print(list(l))
[ print(f'{k} -> {v}') for v,k in l if not k=='\n']

fh.close()
fw.close()
