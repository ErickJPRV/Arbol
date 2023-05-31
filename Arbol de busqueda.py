import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf as pdf_backend
iteraciones=[]
ingreso_de_datos=[]
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.der = None
        self.izq = None
def Busqueda(item,a):
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
        print("Item encontrado")
    else:
        print("Objeto no encontrado")    
def Insertar(item, a):
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
    pass
def graficar_arbol(nodo, x, y, dx, dy,item,item2):
    if nodo is None:
        return
    plt.text(x, y, str(nodo.valor), ha='center', va='center', 
             bbox=dict(facecolor='white', edgecolor='black', boxstyle='circle'))
    plt.text(0, 10, 'Las iteraciones para encontrar el 80 fueron ' + "".join(iteraciones)+str(item), ha='center', va='center', bbox=dict(facecolor='white', edgecolor='black', boxstyle='square'))
    plt.text(0, 15, 'Las iteraciones para ingresar el numero fueron ' + "".join(ingreso_de_datos)+str(item), ha='center', va='center', bbox=dict(facecolor='white', edgecolor='black', boxstyle='square'))
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
item = 80
a = A60
encontrado = False
Busqueda(item,a)
Insertar(21,a)
for i in range(0,len(iteraciones)):
    iteraciones[i]=str(iteraciones[i])+'->'
for i in range(0,len(ingreso_de_datos)):
    ingreso_de_datos[i]=str(ingreso_de_datos[i])+'->'
pdf = pdf_backend.PdfPages("arbol.pdf")
fig = plt.figure(figsize=(8, 6))
graficar_arbol(a, 0, 0, 50, 20,item,21)
pdf.savefig(fig)
plt.close(fig)
pdf.close()






