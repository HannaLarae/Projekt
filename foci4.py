meccsek=[]
f=open("focieredmenyek.txt","r",encoding="utf-8")
for sor in f:
    kislista=sor[:-1].split(";")
    meccsek.append(kislista)
f.close()

#összes hazai csapat nevét írjuk ki egymás alá

for i in range(0,len(meccsek)):
    print(meccsek[i][0])

print("---------------------------------------")
#ön. vendég csapat

for i in range(0,len(meccsek)):
    print(meccsek[i][1])
print("---------------------------------")
#hazai rúgott gól

for i in range(0,len(meccsek)):
     print(meccsek[i][2])
