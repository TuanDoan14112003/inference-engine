from propositionalSymbol import PropositionalSymbol
from clause import Clause
instanceA = PropositionalSymbol("A")
instanceB = PropositionalSymbol("B")
instanceC = PropositionalSymbol("C")
instanceD = PropositionalSymbol("D")

clauseAandB = Clause(instanceA, "&", instanceB)
clauseAandBandC = Clause(clauseAandB, "&", instanceC)
clauseAandBandCimplyD = Clause(clauseAandBandC, "=>", instanceD)
# print(clauseAandBandCimplyD.getValue())
clauseAandBandCimplyD.setPropositionalSymbol({"A":True, "B":True, "C":True, 'D':False})
print(clauseAandBandCimplyD.getValue())

