from pylab import *

def linestyle(ls):
    size = 512,16
    dpi = 72.0
    figsize= size[0]/float(dpi),size[1]/float(dpi)
    fig = figure(figsize=figsize, dpi=dpi)
    fig.patch.set_alpha(0)
    axes([0.2,0,.8,.8],frameon=False)
    X = np.arange(25)
    Y = np.ones(25)
    plot(X,Y,ls,color=(.0,.0,1,1), lw=3, ms=10, mfc=(.75,.75,1,1), mec=(0,0,1,1))
    xlim(0,24)
    xticks([]), yticks([])
    savefig('../figures/linestyle-%s.png' % ls, dpi=dpi)

for ls in ['-','--','-.',':','.',',','o','^','v','<','>','s',
           '+','x','D','d','1','2','3','4','h','H','p','|','_']:
    linestyle(ls)
