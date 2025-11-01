import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv('galaxy_data.csv')


data = data[(data['OIII_5007_flux']/data['OIII_5007_flux_err'] > 5) & (data['HBeta_flux']/data['HBeta_flux_err'] > 5) & (data['NII_6584_flux']/data['NII_6584_flux_err'] > 5) & (data['HAlpha_flux']/data['HAlpha_flux_err'] > 5)] 
 
NII_6584_flux = data['NII_6584_flux']
HAlpha_flux = data['HAlpha_flux']
OIII_5007_flux = data['OIII_5007_flux']
HBeta_flux = data['HBeta_flux']

NII_HAlpha = np.log10(NII_6584_flux/HAlpha_flux)
OIII_HBeta = np.log10(OIII_5007_flux/HBeta_flux)

x = np.linspace(-2, 1, 10000)

def kewley_line(x):
    return 0.61/(x-0.47)+1.19

def kauffmann_line(x):
    return 0.61/(x-0.05)+1.3

x = np.linspace(-2, 0.05, 10000)

fig, ax = plt.subplots(figsize=(8,6))
ax.scatter(NII_HAlpha, OIII_HBeta, s=3, c='blue')

plt.plot(x,kewley_line(x), '--', c='red')
plt.plot(x,kauffmann_line(x), '--', c='orange')

plt.tick_params(axis='x', which='both', length=0)

ax.set_xlabel(r'$\log_{10}([\rm{N\ II}]/HAlpha)$')
ax.set_ylabel(r'$\log_{10}([\rm{O\ III}]/HBeta)$')
plt.title('BPT Diagram for all Galaxies that have Flux/Flux_error>5')
plt.xlim(-2,1)
plt.ylim(-1.5, 1.5)
plt.annotate('AGN', (0.1,1), fontsize=15, color='red')
plt.annotate('Star-Forming Galaxies', (-1.4,-0.5), fontsize=14, color='orange')
plt.show()

            
