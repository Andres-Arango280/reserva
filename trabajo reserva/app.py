from nodos import *



try:
    opcion = 0
    lista_salas = ListaSimplementeEnlazada()
    while True:
        print("\n--- SISTEMA DE GESTIÓN DE SALAS ---")
        print("1. Agregar sala")
        print("2. Eliminar sala")
        print("3. Listar salas disponibles")
        print("4. Listar salas reservadas")
        print("5. Reservar sala")
        print("6. Cancelar reserva")
        print("7. Cambiar reserva")
        print("8. Buscar sala por tipo")
        print("9. Buscar sala por capacidad")
        print("10. Mostrar salas reservadas por tipo")
        print("11. Calcular dinero total")
        print("12. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_sala = int(input("Ingrese el ID de la sala: "))
            tipo = input("Ingrese el tipo de sala (Pequeña, Mediana, Grande): ")
            capacidad_maxima = int(input("Ingrese la capacidad máxima de la sala: "))
            nombre = input("Ingrese el nombre de la sala: ")
            tarifa_por_hora = float(input("Ingrese la tarifa por hora: "))
            estado = input("Ingrese el estado de la sala (Disponible/Reservada): ")
            sala = Sala(id_sala, tipo, capacidad_maxima, nombre, tarifa_por_hora, estado)
            lista_salas.agregar_ultimo(sala)
            
        elif opcion == "2":
            id_sala = int(input("Ingrese el ID de la sala a eliminar: "))
            lista_salas.eliminar_sala_especifica(id_sala)
        elif opcion == "3":
            lista_salas.listar_salas_disponibles()
        elif opcion == "4":
            lista_salas.listar_salas_reservadas()
        elif opcion == "5":
            lista_salas.reservar_sala()
        elif opcion == "6":
            lista_salas.Cancelar_reservada()
        elif opcion == "7":
            lista_salas.cambiar_reserva()
        elif opcion == "8":
            tipo = input("Ingrese el tipo de sala a buscar: ")
            lista_salas.buscar_por_tipo(tipo)
        elif opcion == "9":
            capacidad = int(input("Ingrese la capacidad de sala a buscar: "))
            lista_salas.buscar_por_capacidad(capacidad)
        elif opcion == "10":
            tipo = input("Ingrese el tipo de sala reservada a mostrar: ")
            lista_salas.mostrar_sala_reservada_por_tipo(tipo)
        elif opcion == "11":
            total = lista_salas.dinero_total()
            print(f"El dinero total de las salas reservadas es: ${total:.2f}")
        elif opcion == "12":
            print("Gracias por usar el sistema de gestión de salas. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")
            
except ValueError:
    print("Error: Entrada inválida. Asegúrate de ingresar los valores correctos.")
except Exception as e:
    print(f"Error inesperado: {e}")