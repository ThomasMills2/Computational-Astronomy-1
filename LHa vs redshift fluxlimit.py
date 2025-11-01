import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np
from astropy.cosmology import FlatLambdaCDM

cosmo = FlatLambdaCDM(H0=70, Om0=0.3, Tcmb0=2.725)
df = pd.read_csv('galaxy_data.csv')
lumDist = np.array(cosmo.luminosity_distance(df['redshift']))

lumDist_cm = lumDist*(3.086*10**24)

fig, ax = plt.subplots()

data = pd.read_csv('galaxy_data.csv')

redshift = data['redshift']
F_HAlpha = (data['HAlpha_flux'])*10**-17

L_HAlpha = 4*np.pi*(lumDist_cm**2)*F_HAlpha

galaxy_a = (0.0728652, 3.199353103*10**40)
galaxy_b = (0.09639389, 1.490969734*10**40)
plt.scatter(redshift, L_HAlpha, s=1)
plt.scatter(galaxy_a[0], galaxy_a[1], s=20, c='black', label='Galaxy A')
plt.scatter(galaxy_b[0], galaxy_b[1], s=20, c='orange', label='Galaxy B')

plt.xlabel('redshift')
plt.ylabel('Luminosity, L_HAlpha, (ergs^-1)')
plt.title('Luminosity Versus Redshift')
plt.legend()
plt.yscale('log')
plt.grid()

plt.show()
