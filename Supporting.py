import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import norm
import scipy as sp
from datetime import datetime, timedelta, date
import warnings
from timeit import default_timer as timer
import seaborn as sns
from scipy.interpolate import interp1d
csfont = {'fontname':'Times New Roman'}

vix = vix[['Date','Adj Close']]

ax = vix.plot('Date','Adj Close',linewidth = 0.4, color = 'b', ms = 20, title = 'Vix Index, 22/09/2003 – 30/07/2020', label = 'Closing Price', figsize=(24,10))

ax.axvline(x = '2008-09-15', color='r', ls='--', lw = 1)
ax.axvline(x = '2010-05-06', color='r', ls='--', lw = 1)
ax.axvline(x = '2020-03-16', color='r', ls='--', lw = 1)
ax.axvline(x = '2020-06-18', color='r', ls='--', lw = 1)
plt.savefig('vix.png')

print(np.mean(vix['Adj Close']))
print(np.std(vix['Adj Close']))
print(np.mean(vix['Adj Close']) + 3*np.std(vix['Adj Close']))

date_1 = vix[vix['Date'] == '2008-09-15'] # Lehmann collapse
date_2 = vix[vix['Date'] == '2010-05-06'] # Flash Crash
date_3 = vix[vix['Date'] == '2020-03-16'] # Corona peak
date_4 = vix[vix['Date'] == '2020-06-18'] # Triple witching
date_5 = vix[vix['Date'] == '2020-07-29'] # normal day

plt.figure(figsize=(22,10))
plt.hist(vix['Adj Close'], 200, density = True)

plt.xlabel('VIX volatility index price level', fontsize=22, **csfont)
plt.ylabel('Relative frequency of price level', fontsize=22, **csfont)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.savefig('vix_hist.png')

plt.figure(figsize=(22,10))
plt.plot('Date', 'Adj Close', data = vix, linewidth = 0.7, label = 'Closing Price')
plt.xlabel('Date', fontsize=22, **csfont)
plt.ylabel('Level of the VIX volatility index', fontsize=22, **csfont)
plt.axvline(pd.to_datetime('2008-09-15'), color='r', ls='--', lw = 1.5)
plt.axvline(pd.to_datetime('2010-05-06'), color='r', ls='--', lw = 1.5)
plt.axvline(pd.to_datetime('2020-03-16'), color='r', ls='--', lw = 1.5)
plt.axvline(pd.to_datetime('2020-06-18'), color='r', ls='--', lw = 1.5)
plt.savefig('vix.png')
