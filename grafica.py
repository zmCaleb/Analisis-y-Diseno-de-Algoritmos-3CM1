import math
from pylab import *
on=arange (10.)
ologn=log(on)
on2=on**2
onlogn=on*log(on)
o2n=2**on
o1=ones_like(on)
plot(on, on, 'b.-', label ='O(n)')
plot(on, ologn, 'g.-', label ='O(log n)')
plot(on, on2, 'r.-', label ='O(n2)')
plot(on, onlogn, 'c.-', label ='O(n log n )')
plot(on, o2n, 'm.-', label ='O(2n)')
plot(on, o1, 'y.-', label ='O(1)')


legend()
show()