from array import array
from time import sleep

from os import system


Numberfiles = int(input("digite a quantidade de arquivos"))

vetor = []

for i in range(1,Numberfiles+1):
    system(f"mkdir oi")
    sleep(1)
    system(f"rmdir oi")
