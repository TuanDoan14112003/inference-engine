from propositionalSymbol import PropositionalSymbol

instanceA = PropositionalSymbol("A")
instanceB = PropositionalSymbol("B")
instanceC = PropositionalSymbol("C")
instanceD = PropositionalSymbol("D")


listOfSymbols = [instanceA, instanceB, instanceC, instanceD]
for i in listOfSymbols:
    print(i.getValue())


instanceA.setValue(True)
instanceB.setValue(False)
instanceC.setValue(True)
instanceD.setValue(False)


for i in listOfSymbols:
    print(i.getValue())


