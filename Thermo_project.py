import numpy as np
import matplotlib
import matplotlib.pyplot as plt

T = np.linspace(300,1500,100)

deltag0_1 = -259600 + 62.55*T  # for reaction of Fe and O2 to give FeO
deltag0_2 = -1091000 + 312.8*T  # for reaction of Fe and O2 to give Fe304
deltag0_3 = -247300 + 55.9*T  # for reaction of H2 and O2 to give H2O

# for reaction of FeO and H2 to give Fe and H2O
# deltag0_a = deltag0_1 + deltag0_3
deltag0_a = 12300 - 6.65*T
# x1 = 1/(1+(exp(-deltag0_a/(R*T))))
x1 = 1/(1+np.exp(0.8 - (1479.43/T)))
plt.plot(T,x1)

# for reaction of Fe3O4 and H2 to give Fe and H2O
# deltag0_b = deltag0_2 + 4*deltag0_3
deltag0_b = 101800 - 89.2*T
# x2 = 1/(1+((exp(-deltag0_b/(R*T)))/4))
x2 = 1/(1+np.exp(2.68 - (3061.1/T)))
plt.plot(T,x2)

# for reaction of Fe3O4 and H2 to give FeO and H2O
# deltag0_c = deltag0_b - 3*deltag0_a
deltag0_c = 64900 - 69.25*T
# x3 = 1/(1+(exp(-deltag0_c/(R*T))))
x3 = 1/(1+np.exp(8.33 - (7806.11/T)))
plt.plot(T,x3)

plt.xlabel("Temperature")
plt.ylabel("PH2/(PH2+PH20)")
plt.legend(('FeO to Fe','Fe3O4 to Fe','Fe3O4 to FeO'))
plt.title(" Fe-O-H stability diagram ")
plt.show()

T_invariant = (64900 - 12300)/(69.25 - 6.65) # from deltag0_c - deltag0_a = 0 that is △G = 0 for reaction Fe3O4 + Fe = 4FeO
print('Invarient temperature is',T_invariant)


T2 = np.linspace(T_invariant,1500,100)
plt.plot(T2, 1/(1+np.exp(0.8-(1479.43/T2))))

T1 = np.linspace(300,T_invariant,100)
plt.plot(T1, 1/(1+np.exp(2.68-(3061.1/T1))))

T2 = np.linspace(T_invariant,1500,100)
plt.plot(T2, 1/(1+np.exp(8.33-(7806.11/T2))))

plt.text(500, 0.5, 'Fe3O4', horizontalalignment='center', verticalalignment='center')
plt.text(1000, 0.9, 'Fe', horizontalalignment='center', verticalalignment='top')
plt.text(1200, 0.4, 'FeO', horizontalalignment='center', verticalalignment='bottom')
plt.xlabel("Temperature")
plt.ylabel("PH2/(PH2+PH20)")
plt.legend(('FeO to Fe','Fe3O4 to Fe','Fe3O4 to FeO'))
plt.title(" Fe-O-H stability diagram ")
plt.show()