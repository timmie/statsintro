'''Show the origin of ROC-curves

'''

'''
Author: thomas haslwanter
Date:   23-march 2013
Ver:    0.1
'''

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Calculate the PDF-curves
x = np.linspace(-10, 15, 201)
nd1 = stats.norm(1,2)
nd2 = stats.norm(6,2)
y1 = nd1.pdf(x)
y2 = nd2.pdf(x)

# Axes locations
ROC = {'left': 0.3,
       'width': 0.45,
       'bottom': 0.1,
       'height': 0.45}

PDF = {'left': 0.1,
       'width': 0.8,
       'bottom': 0.65,
       'height': 0.3}
       
rect_ROC = [ROC['left'], ROC['bottom'], ROC['width'], ROC['height']]
rect_PDF = [PDF['left'], PDF['bottom'], PDF['width'], PDF['height']]

fig = plt.figure()

ax1 = plt.axes(rect_PDF)
ax2 = plt.axes(rect_ROC)

# Plot and label the PDF-curves
ax1.plot(x,y1)
ax1.hold(True)
ax1.fill_between(x,0,y1, where=x<3, facecolor='blue', alpha=0.5)
ax1.annotate('Sensitivity',
             xy=(x[50], y1[50]),
             xytext=(x[20], y1[50]*1.2), 
             fontsize=14,
             horizontalalignment='center',
             arrowprops=dict(facecolor='blue'))

ax1.plot(x,y2,'r')
ax1.fill_between(x,0,y2, where=x<3, facecolor='red', alpha=0.5)
ax1.annotate('1-Specificity',
             xy=(3, 0.03),
             xytext=(4,0.05), 
             fontsize=14,
             horizontalalignment='center',
             arrowprops=dict(facecolor='red'))

ax1.set_ylabel('PDF')

# Plot the ROC-curve
ax2.plot(nd2.cdf(x), nd1.cdf(x), 'k')
ax2.hold(True)
ax2.plot(np.array([0,1]), np.array([0,1]), 'k--')

# Format the ROC-curve
ax2.set_xlim([0, 1])
ax2.set_ylim([0, 1])
#ax2.axis('equal')
ax2.set_title('ROC-Curve')
ax2.set_xlabel('1-specificity')
ax2.set_ylabel('sensitivity')

# Show the plot, and create a figure
outFile = r'C:\Temp\ROC.png'
plt.savefig(outFile, dpi=200)
print 'ROC-figure saved to {0}.'.format(outFile)

plt.show()
