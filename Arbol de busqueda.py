import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf as pdf_backend
iteraciones=[]
ingreso_de_datos=[]
global encontrado
global p
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.der = None
        self.izq = None
def Busqueda(item,a):
    global encontrado
    while a is not None:
        if item > a.valor:
            iteraciones.append(a.valor)
            a = a.der
        elif item < a.valor:
            iteraciones.append(a.valor)
            a = a.izq
        else:
            encontrado = True
            break
    if encontrado:
        pass
    else:
        encontrado=False    
def Insertar(item, a):
    global p
    while True:
        ingreso_de_datos.append(a.valor)
        if item > a.valor:
            if a.der is None:
                a.der = Nodo(item)
                break
            else:
                a = a.der
        elif item < a.valor:
            if a.izq is None:
                a.izq = Nodo(item)
                break
            else:
                a = a.izq
        elif item==a.valor:
            p=True
            break
    pass
def graficar_arbol(nodo, x, y, dx, dy,item,item2):
    global encontrado
    if nodo is None:
        return
    plt.text(x, y, str(nodo.valor), ha='center', va='center', 
             bbox=dict(facecolor='white', edgecolor='black', boxstyle='circle'))
    if(encontrado==False):
        plt.text(0, 10, 'No se pudo encontrar el numero seleccionado', ha='center', va='center', bbox=dict(facecolor='white', edgecolor='black', boxstyle='square'))
    elif(encontrado==True):
        plt.text(0, 10, 'Las iteraciones para encontrar el n fueron ' + "".join(iteraciones)+str(item), ha='center', va='center', bbox=dict(facecolor='white', edgecolor='black', boxstyle='square'))
    if(p==True):
        plt.text(0, 15, 'El numero que quiere insertar ya existe', ha='center', va='center', bbox=dict(facecolor='white', edgecolor='black', boxstyle='square'))    
    elif(p==False):
        plt.text(0, 15, 'Las iteraciones para ingresar el numero fueron ' + "".join(ingreso_de_datos)+str(item2), ha='center', va='center', bbox=dict(facecolor='white', edgecolor='black', boxstyle='square'))
    x_izq = x - dx
    x_der = x + dx
    y_nivel = y - dy
    if nodo.izq is not None:
        plt.plot([x, x_izq], [y, y_nivel], color='black')
    if nodo.der is not None:
        plt.plot([x, x_der], [y, y_nivel], color='black')
    graficar_arbol(nodo.izq, x_izq, y_nivel, dx/2, dy,item,item2)
    graficar_arbol(nodo.der, x_der, y_nivel, dx/2, dy,item,item2)
A60 = Nodo(60)
B30 = Nodo(30)
C70 = Nodo(70)
D20 = Nodo(20)
E55 = Nodo(55)
F90 = Nodo(90)
G35 = Nodo(35)
H80 = Nodo(80)
I95 = Nodo(95)
J40 = Nodo(40)
K40 = Nodo(40)
L50 = Nodo(50)
A60.izq = B30
A60.der = C70
B30.izq = D20
B30.der = E55
C70.der=F90
E55.izq=G35
G35.der=J40
J40.der=L50
J40.izq=K40
F90.der=I95
F90.izq=H80
item = 50  ######Numero que desea Buscar
item2= 70 ####Numero que desea ingresar
a = A60
encontrado = False
Busqueda(item,a)
Insertar(item2,a)
for i in range(0,len(iteraciones)):
    iteraciones[i]=str(iteraciones[i])+'->'
for i in range(0,len(ingreso_de_datos)):
    ingreso_de_datos[i]=str(ingreso_de_datos[i])+'->'
pdf = pdf_backend.PdfPages("arbol.pdf")
fig = plt.figure(figsize=(8, 6))
graficar_arbol(a, 0, 0, 50, 20,item,item2)
pdf.savefig(fig)
plt.close(fig)
pdf.close()