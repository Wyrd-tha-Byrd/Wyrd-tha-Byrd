import math
    #use this function to calculate the ideal output frequency (in kiloHertz) of a colpitts oscillator, 
    #The necessary variables are: the tuning inductance = L, and the capacitors = C1 and C2;
L = raw_input("Please enter the Tuning Inductance Value: ")
C1 = raw_input("Please enter the Collector Capacitor C1 Value: ")
C2 = raw_input("Please enter the Recycling Capacitor C2 Value: ")
print(L)
print(C1)
print(C2)
Tau = math.tau
Cap_Sum = math.fsum(C1,C2)
Cap_Prod = math.prod(C1,C2)
Tau_root = math.pow(Tau),math.sqrt(math.prod(L,Cap_Prod/Cap_Sum))
F0 = 1/Tau_root
print(F0)