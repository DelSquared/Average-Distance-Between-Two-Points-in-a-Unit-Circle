import numpy as np

s=0

while s==0:
	x1,x2,y1,y2=np.random.uniform(-1,1,(4,))

	if (x1*x1+y1*y1<=1 and x2*x2+y2*y2<=1):
		s=np.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))


for i in range(100000000):
	x1,x2,y1,y2=np.random.uniform(-1,1,(4,))

	if (x1*x1+y1*y1<=1 and x2*x2+y2*y2<=1):
		s=((i+1)*s+np.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)))/(i+2)

print(s)
