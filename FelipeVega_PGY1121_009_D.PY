import funciones as fn

while True:
    fn.ver_menu()
    opcion = fn.validar_opcion()
    if opcion ==1:
        fn.comprar_entradas()
    elif opcion ==2:
        fn.ver_escenario()
    elif opcion ==3:
        fn.ver_asistentes()
    elif opcion ==4:
       pass
    else:
      fn.salir()





