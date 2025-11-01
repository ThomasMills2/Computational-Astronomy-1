# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 20:07:41 2023

@author: Tom
"""

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('galaxy_data.csv')

ra = data['RA']
dec = data['DEC']

galaxy_a = (184.14566666666664, 0.44455555555555426)
galaxy_b = (141.30974999999998, 59.41844444444445)

highlight_a = ((ra == galaxy_a[0]) & (dec == galaxy_a[1]))
highlight_b = ((ra == galaxy_b[0]) & (dec == galaxy_b[1]))


plt.scatter(ra, dec, s=1, color='blue')

plt.scatter(ra[highlight_a], dec[highlight_a], s=30, color='violet', label='Galaxy A')
plt.scatter(ra[highlight_b], dec[highlight_b], s=30, color='red', label='Galaxy B')


plt.xlabel('Right Ascension, RA, (deg)')
plt.ylabel('Declination, DEC, (deg)')
plt.title('Declination Vursus Right Ascension for All Galaxies')
plt.grid()
plt.legend(loc='upper left')


plt.show()