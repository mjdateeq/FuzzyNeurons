## This Function takes inputs and weights of input layer
## The output is a matrix m x n 
## Go to ReadME File for more clarification on AND neuron

def AND_Neuron(xy, w):
   func = lambda a, b: ((a+b) - (a*b))

   xShape = np.shape(xy)

   mul = []
   NewFin = []
   for i in range (w1shape[1]):
     for j in range (xShape[0]):
        for k in range (xShape[1]):
          mul.append (func(xy[j][k],w[k][i]))
        NewFin.append(np.prod(mul))
        mul=[]
   NewFin = np.reshape(NewFin, (xShape[0],w1shape[1]), order = 'F');
   return NewFin
