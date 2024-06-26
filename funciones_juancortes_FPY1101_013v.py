


libras = ["python \n sku 212121122022", "python2 \n sku 1000000222000", "python3 \n sku  051514412541", "python4 \n sku 0541215452154"]
libros = []
def r_libros():
        nombre = input("ingrese titulo del libro que desea agregar \n: ")
        autor = input("ingrese autor del libro \n: ")
        ano = int(input("ingrese año de publicacion del libro \n: "))
        sku0 = input("ingrese sku SKU es las 6 primeras letras del título del libro  \n: ")
        sku2 = input("ingrese las tres primeras letras del nombre del autor ")
        sku = sku0, sku2, ano

        if nombre and autor and ano and sku0 and sku2:
            libro = {
                "nombre": nombre,
                "autor": autor,
                "ano": ano,
                "sku0": sku0,
                "sku2": sku2,
                "sku": sku
                }
            libros.append(libro)
            print("\3"*18 ,"todo bien ingresado", "\3"*18) 
        
def prestar_libro(libros):
     persona = input("porfavor ingrese su nombre: ")
     escri_sku = input(" por favor ingrese el sku del libro que desea solicitar : ")
     sku_disponible = [libro for libro in libros if libro ["sku"] == escri_sku]
     libros.append(persona)
     if sku_disponible:
        print("\3 libro encontrado \3")
            
     else:
      print("\1 libro no encontrado \1")
      return

def lista_de_libros():
     with open("lista_libros.txt" , "w") as listalibros:
        listalibros.write(" nombre del autor   año de publicacion     sku1          sku2\n")

    

        





def imprimir_prestamos():
     




                        














 def menu():
     while True:
        try:
            print("\3"*18, "menu" , "\3"*18)
            op = int(input(" 1.registrar libro  \n 2  prestar libro \n 3 lista de todos los libros \n 4 Imprimir reporte de préstamos  \n 5 salir del programa  \n----------- " ))
            if op == 1:
             r_libros(libros)
            elif op == 2:
               prestar_libro(libros)
            elif op == 3:
              lista_de_libros()
            elif op == 4:    
              imprimir_prestamos()
              print(imprimir_prestamos)
            elif op == 5:
                print("programa finalizado \n desarrollado por juan cortes \n run : 19.312.169-1 ")    

            else:
                print("ingrese una opcion valida")

        except ValueError:
            print("hay un error ")                