meccsek=[]
f=open("focieredmenyek.txt","r",encoding="utf-8")
for sor in f:
    kislista=sor[:-1].split(";")
    meccsek.append(kislista)
f.close()

