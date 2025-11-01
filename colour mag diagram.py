import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np
from astropy.cosmology import FlatLambdaCDM

cosmo = FlatLambdaCDM(H0=70, Om0=0.3, Tcmb0=2.725)
df = pd.read_csv('galaxy_data.csv')
lumDist = np.array(cosmo.luminosity_distance(df['redshift']))

fig, ax = plt.subplots()

data = pd.read_csv('galaxy_data.csv')

g = data['g']
r = data['r']

grcolour = g-r
M_r = r - 5*np.log10((lumDist*10**6)/10)

galaxy_a = (M_r == -20.23892799, grcolour == 0.792)
galaxy_a = (M_r == -20.30130799, grcolour == 0.93224)

highlight_a = ((ra == galaxy_a[0]) & (dec == galaxy_a[1]))
highlight_b = ((ra == galaxy_b[0]) & (dec == galaxy_b[1]))

def red_blue_line(M_r):
    return -0.0571*(M_r+24)+0.9

x_line = np.linspace(-25.5,-13.9, 100)
y_line = red_blue_line(x_line)
ax.plot(x_line, y_line, 'g', label='Red sequeance / Blue cloud seperation')

plt.scatter(M_r, grcolour, s=1)
plt.scatter(M_r[highlight_a], grcolour[highlight_a], s=20, color='black', label='Galaxy A')
plt.scatter(M_r[highlight_b], grcolour[highlight_b], s=20, color='orange', label='Galaxy B')

plt.xlabel('r band absolute magnitude, M_r')
plt.ylabel('g-r colour, g-r')
plt.title('Colour-Magnitude diagram for All Galaxies')
plt.legend()
plt.annotate('Red Cloud', (-20,0.9), fontsize=13, color='red')
plt.annotate('Blue Sequence', (-24,0.5), fontsize=14, color='navy')


plt.show()
