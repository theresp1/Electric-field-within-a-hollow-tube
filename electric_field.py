import numpy as np 
import matplotlib.pyplot as plt

plt.rcParams.update({"font.size":14})
plt.rcParams.update({"axes.labelsize":16})
plt.rcParams.update({"xtick.labelsize":13})
plt.rcParams.update({"ytick.labelsize":13})
plt.rcParams.update({"legend.fontsize":15})


N = 100 
M = 100   # we have a sum from n = 0  to m 
L = 1     # lenght og the box
m = 3     # for the first test potential 

x = np.linspace(0,L,N)
y = np.linspace(0,L,N)

## V_0(x)
V_01 = np.sin((m*np.pi * x)/L)
V_02 = 1 - (x/L - 1/2)**4
V_03 = np.heaviside(x-L/2,1/4 ) * np.heaviside(3/4 * L - x, 3/8)

# fourier coeff
def C_n(n,V): 
    return 2/np.sinh(n* np.pi) * np.trapz(np.sin(n*np.pi*x)*V,x)

# potential 
def V(M,V_0): 
    Cn = np.zeros(M) 
    V  = np.zeros((N,N))
    for n in range (M): 
        Cn[n] = C_n(n+1,V_0)
    for i in  range(N):  ## y 
        for j in range(N):  ## x
            n = np.linspace(1,M,M,dtype = np.int16)
            element = np.asarray(np.sin(n* np.pi *x[j] ) *np.sinh(n * np.pi * y[i]))
            V[i][j] = Cn @ element
            
    return V 


def convergance_test(V_0):
    diff = np.zeros(100)
    n    = 100
    X    = np.linspace(1,200,n,dtype= np.int16)
    for i in range (n): 
        pot = V(X[i],V_0) 
        diff[i] = np.amax(np.abs(pot[N-1][1:99] -V_0[1:99]))
        
    return X,diff
    

def E(M,V_0):  
    V1 = V(M,V_0)
    Ex = -np.gradient(V1,axis = 1)     
    Ey = -np.gradient(V1, axis =0)     
    return Ex,Ey


# =============================================================================
#                                PLOTS 
# =============================================================================

## plot fpr V_01 CONTOUR PLOT
#fig, ax = plt.subplots()
#CS = ax.contour(x, y, V(M,V_01))
#ax.clabel(CS, inline=1, fontsize=13)
#plt.xlabel("$\\xi$")
#plt.ylabel("$\\psi$")
#ax.set_title('')

## plot fpr V_02 CONTOUR PLOT
#fig, ax = plt.subplots()
#CS = ax.contour(x, y, V(M,V_02))
#ax.clabel(CS, inline=1, fontsize=14)
#plt.xlabel("$\\xi$")
#plt.ylabel("$\\psi$")
#ax.set_title('')
 
## plot fpr V_03 CONTOUR PLOT 
#fig, ax = plt.subplots()
#CS = ax.contour(x, y, V(M,V_03))
#ax.clabel(CS, inline=1, fontsize=9)
#plt.xlabel("$\\xi$")
#plt.ylabel("$\\psi$")
#ax.set_title('')
        
# Plot of V_01
#plt.plot(x, V(M,V_01)[N-1], color = "b", label ="$V( \\xi )$")
#plt.plot(x,V_01, color = "k", label ="$V_{0}( \\xi )$" )
#plt.xlabel("$\\xi$")
#plt.ylabel("$V( \\xi )/V_{c}$")
#plt.legend()
#plt.show() 

# Plot of V_02
#plt.plot(x, V(M,V_02)[N-1], color = "b", label ="$V( \\xi )$")
#plt.plot(x,V_02, color = "k", label ="$V_{0}( \\xi )$" )
#plt.xlabel("$\\xi$")
#plt.ylabel("$V( \\xi )/V_{c}$")
#plt.legend()
#plt.show() 

# Plot of V_03
#plt.plot(x, V(M,V_03)[N-1], color = "b", label ="$V( \\xi )$")
#plt.plot(x,V_03, color = "k", label ="$V_{0}( \\xi )$" )
#plt.xlabel("$\\xi$")
#plt.ylabel("$V( \\xi )/V_{c}$")
#plt.legend()
#plt.show() 

# convergance plot OF V_01
#X,Y = convergance_test(V_01)
#plt.plot(X,Y,linewidth = 1)
#plt.xlabel("$N$")
#plt.ylabel("$ max|(V(\\xi)-V_{0}(\\xi)|$")
#plt.show() 
    
# convergance plot OF V_02
#X,Y = convergance_test(V_02)
#plt.semilogy(X,Y,linewidth = 1)
#plt.xlabel("$N$")
#plt.ylabel("$ max|(V(\\xi)-V_{0}(\\xi)|$")
#plt.show()

# convergance plot OF V_03
#X,Y = convergance_test(V_03)
#plt.semilogy(X,Y,linewidth = 1)
#plt.xlabel("$N$")
#plt.ylabel("$ max|V(\\xi)-V_{0}(\\xi)|$")
#plt.show()  
    

# plot of E using V_01
#X = x 
#Y = y
#U = E(M,V_01)[0]
#W = E(M,V_01)[1]

#fig, ax = plt.subplots()
#q = ax.quiver(X,Y,U,W,)
#ax.quiverkey(q, X=1, Y=1, U = 0,
#             label='', labelpos='E')

#plt.xlabel("$\\xi$")
#plt.ylabel("$\\psi$")
#plt.show()
    
# plot of E using V_02
#X = x 
#Y = y
#U = E(M,V_02)[0]
#W = E(M,V_02)[1]

#fig, ax = plt.subplots()
#q = ax.quiver(X,Y,U,W,)
#ax.quiverkey(q, X=1, Y=1, U = 0,
#             label='', labelpos='E')
#plt.xlabel("$\\xi$")
#plt.ylabel("$\\psi$")
#plt.show()
    
# plot of E using V_03
#X = x 
#Y = y
#U = E(M,V_03)[0]
#W = E(M,V_03)[1]

#fig, ax = plt.subplots()
#q = ax.quiver(X,Y,U,W,)
#ax.quiverkey(q, X=1, Y=1, U = 0,
#             label='', labelpos='E')
#plt.xlabel("$\\xi$")
#plt.ylabel("$\\psi$")
#plt.show()
