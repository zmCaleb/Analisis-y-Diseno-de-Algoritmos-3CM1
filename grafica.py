import math
from pylab import *
on=arange (10.)
ologn=log(on)
on2=on**2
onlogn=on*log(on)
o2n=2**on
plot(on, on, 'b.-', on, ologn, 'g.-', on, on2, 'r.-', on, onlogn, 'c.-', on, o2n, 'm.-')

show()