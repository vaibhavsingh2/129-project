import csv
import pandas as pd

file1 = 'bright_stars.csv'
file2 = 'dwarf_stars.csv'

a1 = []
a2 = []
with open(file1,'r',encoding='utf8') as f:
    csv_reader =csv.reader(f)
    
    for i in csv_reader:
        a1.append(i)
        
with open(file2,'r',encoding='utf8') as f:
    csv_reader = csv.reader(f)
    
    for i in csv_reader:
        a2.append(i)

h1 = a1[0]
h2 = a2[0]

p_d1 = a1[1:]
p_d2 = a2[1:]

h = h1+h2

p =[]

for i in p_d1:
    p.append(i)
for j in p_d2:
    p.append(j)
with open("total_stars.csv",'w',encoding='utf8') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(h)   
    csvwriter.writerows(p)
    
df = pd.read_csv('total_stars.csv')
df.tail(8)
