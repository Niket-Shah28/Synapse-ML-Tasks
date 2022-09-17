modern_family = ['CLaiRe_DunPhY', 'PHiL_dUnpHY', 'GLoRiA_PriTCheTt', 'CaMErOn_TuCKEr','StELLa']
l=len(modern_family)
indices=[]
characters=[]
for a,b in enumerate(modern_family):
    indices.append(a)
    characters.append(b)
for i in range(0,l):
    characters[i]=characters[i].lower()
    characters[i]=characters[i].replace('_','-')
temp=list(map(lambda x:len(x),characters))
indices=list(zip(indices,temp))
for i in range (0,l):
    indices[i]=sum(indices[i])
indices.sort(reverse=True)
Phew_finally={}
for i in range (0,l):
  Phew_finally.update({indices[i]:characters[i]})
print(Phew_finally)

