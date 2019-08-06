from variaveisGlobais import *

notes = []

def InsertNotes():
    for x in range(0, TURNS):
        notes.append(input('\nInforme a {}º Nota: '.format(x+1)))
        
    