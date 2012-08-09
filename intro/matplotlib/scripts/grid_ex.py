from pylab import *

axes = gca()

axes.set_xlim(0,4)
axes.set_ylim(0,3)
axes.xaxis.set_major_locator(MultipleLocator(1.0))
axes.xaxis.set_minor_locator(MultipleLocator(0.1))
axes.yaxis.set_major_locator(MultipleLocator(1.0))
axes.yaxis.set_minor_locator(MultipleLocator(0.1))
axes.grid(which='major', axis='x', linewidth=0.75, linestyle='-', color='0.75')
axes.grid(which='minor', axis='x', linewidth=0.25, linestyle='-', color='0.75')
axes.grid(which='major', axis='y', linewidth=0.75, linestyle='-', color='0.75')
axes.grid(which='minor', axis='y', linewidth=0.25, linestyle='-', color='0.75')

axes.set_xticklabels([])
axes.set_yticklabels([])

# savefig('../figures/grid_ex.png',dpi=64)
show()
