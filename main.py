# programa para gestión emercado 
#  dejestion de mercado 
nombreUsuario=None

#listas 
#productos =[]
#producto={}

print("***APP")
print("1. agregar productos ")
print("2. revisar tulista demercado ")
print("3. modificar la lista del mercado")
print("4. retirar el producto de tulista de metira ")
print ("ingrese con el 5")

opsion=100
while opsion != 5:
    opsion = int(input("digina una opcion del menu "))

    if opsion == 1:
        print("ingresr lista ")
    producto["id"]=5
    producto["nombre "]=(input("ingresa e nombre del producto "))
    producto["presentación"]=(input("Digite la presentacion del producto"))
    producto["cantidad"]=(input("digite la cantidad del producto"))
    producto["precio"]=(input("digite el precio "))

    productos.append(producto)

    if opsion == 2:
      print("mostrar lista  ")
    elif opsion == 3 :
        print("revisar la lista ")
    elif opsion == 4:
      print("modificar lista")
    elif opsion == 5:
      print("retirar producto")
    else:
        print("opciones invalida")
