import numpy as np
from matplotlib import pyplot as plt
import constants
fig = plt.figure()
ax = fig.add_subplot(111)
fig.set_size_inches(10, 10)
# ax.set_aspect(aspect=1)
# ax.set_title('miscarea pe x in functie de timp')
# ax.set_xlabel('timp')
# ax.set_ylabel('x')
t = np.linspace(0, 2 * np.pi, 1024, endpoint=True) #axa timpului; t_initial=0s, t_final=2*PI s; 2024 cadre
# plt.plot(t-np.pi, [0 for i in t], '--', linewidth=1, color='gray') #linii punctate centru x
# plt.plot([0 for i in t], t-np.pi, '--', linewidth=1, color='gray') #linii punctate centru y
 
x = np.sin(t)*(-1) #Deplasarea pe x in functie de timp
y = np.append(x, x)
y = y[::2] #Deplasarea pe y in functie de timp
x *= 5
liftCoeff = []
dragCoeff = []
finete = []
power = []
for i in y:
    l = 1.05 + i/20
    d = 0.15 + i/33
    liftCoeff.append(l)
    dragCoeff.append(d)
    f = l**3 / d**2
    finete.append(f)
    p = f * (constants.CONST*constants.PRESIUNE_AER*constants.ARIE_ARIPA*constants.VITEZA_VANT_CUB)
    power.append(f)

plt.plot(t, power)

plt.show()

