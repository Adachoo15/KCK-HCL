import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import aseegg as ag
dane = pd.read_csv(r"sub-007_trial-07.csv", delimiter=',', engine='python')
baza=pd.DataFrame(dane)
sygnal=baza["b"]
liczba=baza["f"]
t=np.linspace(0,37.84, 200*37.84)
sygnalprzef=ag.pasmowozaporowy(sygnal,200,49,51)
sygnalprzefiltrowany=ag.pasmowoprzepustowy(sygnalprzef,200,1,50)
plt.plot(t,sygnal)
plt.ylabel("Amplituda [-]")
plt.xlabel("Czas [s]")
plt.show()
plt.plot(t,sygnalprzef)
plt.ylabel("Amplituda [-]")
plt.xlabel("Czas [s]")
plt.show()
plt.plot(t,sygnalprzefiltrowany)
plt.ylabel("Amplituda [-]")
plt.xlabel("Czas [s]")
plt.show()
print(sygnal.mean())
print(sygnal.max())
print((1.5847468537697242+3.719023605585575)/2)
mrug=[]
mrug2=[]
j=1
for i in range(len(sygnal)):
    if sygnal[i]>1.8:
        mrug.append(liczba[i])
for i in range(len(sygnal)):
    if sygnal[i]>2.6518852296776494:
        mrug2.append(liczba[i])
print(mrug)
print(mrug2)
