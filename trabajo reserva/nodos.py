# modulo de listatas enlazadas 

from Salas_P_M_G import *


class Nodo:
    def __init__(self, sala):
        self.sala = sala
        self.siguiente = None

class ListaSimplementeEnlazada:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def vacia(self):
        return self.primero == None

    def agregar_ultimo(self, sala):
                if self.vacia():
                    self.primero = self.ultimo = Nodo(sala)
                else:
                    aux = self.ultimo
                    self.ultimo = aux.siguiente = Nodo(sala) 

    def recorrido(self):
        aux = self.primero
        while aux != None:
            print(aux.sala)  # Esto imprime la información de la sala usando el método __str__ de Sala
            aux = aux.siguiente

    def eliminar_ultimo(self):
        if self.vacia():
            print("La lista está vacía.")
            return
        aux = self.primero
        while aux.siguiente != self.ultimo:
            aux = aux.siguiente
        aux.siguiente = None
        self.ultimo = aux

    def agregar_inicio(self, sala):
        if self.vacia():
            self.primero = self.ultimo = Nodo(sala)
        else:
            aux = Nodo(sala)
            aux.siguiente = self.primero
            self.primero = aux

    def eliminar_inicio(self):
                if self.vacia():
                    print("La lista está vacía.")
                    return
                self.primero = self.primero.siguiente
                if self.primero is None:
                    self.ultimo = None

    def buscar_por_tipo(self, tipo):
        aux = self.primero
        resultado = []
        while aux is not None:
            if aux.sala.tipo == tipo:
                resultado.append(aux.sala)
            aux = aux.siguiente
        if resultado:
            for sala in resultado:
                print(sala)
        else:
            print(f"No se encontraron salas del tipo '{tipo}'.")

    def buscar_por_capacidad(self, capacidad):
        aux = self.primero
        resultado = []
        while aux is not None:
            if aux.sala.capacidad_maxima == capacidad:
                resultado.append(aux.sala)
            aux = aux.siguiente
        if resultado:
            for sala in resultado:
                print(sala)
        else:
            print(f"No se encontraron salas con capacidad mínima de {capacidad} personas.")


    def eliminar_sala_especifica(self, id_sala):
        if self.vacia():
            print("No hay ninguna sala registrada")
            return

        # si la sala a eliminar es la primera
        if self.primero.sala.id_sala == id_sala:
            self.primero = self.primero.siguiente
            if self.primero is None:
                self.ultimo = None
            print(f"Sala con ID {id_sala} eliminada")
            return

        # Recorrer la lista para encontrar el nodo con el id_sala
        actual = self.primero
        anterior = None

        while actual is not None:
            if actual.sala.id_sala == id_sala:
                
                anterior.siguiente = actual.siguiente
                
                if actual == self.ultimo:
                    self.ultimo = anterior
                print(f"Sala con ID {id_sala} eliminada")
                return
            anterior = actual
            actual = actual.siguiente

        # Si no se encontró la sala
        print(f"Sala con ID {id_sala} no encontrada")

    def listar_salas_disponibles(self):
        print("Salas disponibles para reserva:")
        aux = self.primero
        encontradas = False
        while aux is not None:
            if aux.sala.estado.lower() == "disponible":
                print(f"ID: {aux.sala.id_sala}")
                print(f"Nombre: {aux.sala.nombre}")
                print(f"Tipo: {aux.sala.tipo}")
                print(f"Capacidad máxima: {aux.sala.capacidad_maxima}")
                print(f"Tarifa por hora: ${aux.sala.tarifa_por_hora:.2f}")
                print("--------------------")
                encontradas = True
            aux = aux.siguiente
        
        if not encontradas:
            print("No hay salas disponibles en este momento.")
        
    def listar_salas_reservadas(self):
        print("Salas actualmente reservadas:")
        aux = self.primero
        encontradas = False  # Bandera para verificar si hay salas reservadas
        while aux is not None:
            if aux.sala.estado.lower() == "reservada":  # Verificar si la sala está reservada
                print(f"ID: {aux.sala.id_sala}")
                print(f"Nombre: {aux.sala.nombre}")
                print(f"Tipo: {aux.sala.tipo}")
                print(f"Capacidad máxima: {aux.sala.capacidad_maxima}")
                print(f"Tarifa por hora: ${aux.sala.tarifa_por_hora:.2f}")
                print("--------------------")
                encontradas = True
            aux = aux.siguiente  # Avanzar al siguiente nodo

        if not encontradas:
            print("No hay salas reservadas en este momento.")


    def Cancelar_reservada(self):
        if self.vacia():
            print("No hay salas registradas.")
            return

        # Mostrar las salas reservadas
        aux = self.primero
        encontradas = False
        reservadas = []

        while aux is not None:
            if aux.sala.estado.lower() == "reservada":  # Verificar si la sala está reservada
                reservadas.append(aux.sala)
                encontradas = True
            aux = aux.siguiente

        if not encontradas:
            print("No hay salas reservadas en este momento.")
            return

        # Mostrar las salas reservadas
        print("Salas actualmente reservadas:")
        for sala in reservadas:
            print(f"ID: {sala.id_sala}, Nombre: {sala.nombre}")

        # Solicitar al usuario que elija una sala para cancelar
        id_sala = int(input("Ingrese el ID de la sala que desea cancelar: "))
        
        # Cambiar el estado de la sala a disponible si está reservada
        aux = self.primero
        while aux is not None:
            if aux.sala.id_sala == id_sala:
                if aux.sala.estado.lower() == "reservada":
                    aux.sala.estado = "disponible"  # Cambiar a disponible
                    print(f"Reserva de la sala '{aux.sala.nombre}' (ID: {id_sala}) cancelada y ahora está disponible.")
                else:
                    print(f"La sala '{aux.sala.nombre}' (ID: {id_sala}) ya está disponible.")
                return
            aux = aux.siguiente
        
        print(f"Sala con ID {id_sala} no encontrada.")

    def cambiar_reserva(self):
        if self.vacia():
            print("No hay salas registradas.")
            return

        # Mostrar salas reservadas
        aux = self.primero
        reservadas = []
        while aux is not None:
            if aux.sala.estado.lower() == "reservada":
                reservadas.append(aux.sala)
            aux = aux.siguiente

        if not reservadas:
            print("No hay salas reservadas en este momento.")
            return

        print("Salas actualmente reservadas:")
        for sala in reservadas:
            print(f"ID: {sala.id_sala}, Nombre: {sala.nombre}")

        # Solicitar al usuario que elija una sala reservada
        id_sala_reservada = int(input("Ingrese el ID de la sala reservada que desea cambiar: "))

        # Buscar la sala reservada
        sala_reservada = None
        aux = self.primero
        while aux is not None:
            if aux.sala.id_sala == id_sala_reservada:
                sala_reservada = aux.sala
                break
            aux = aux.siguiente

        if sala_reservada is None:
            print(f"Sala con ID {id_sala_reservada} no encontrada.")
            return

        # Mostrar salas disponibles
        aux = self.primero
        disponibles = []
        while aux is not None:
            if aux.sala.estado.lower() == "disponible":
                disponibles.append(aux.sala)
            aux = aux.siguiente

        if not disponibles:
            print("No hay salas disponibles en este momento.")
            return

        print("Salas disponibles para reservar:")
        for sala in disponibles:
            print(f"ID: {sala.id_sala}, Nombre: {sala.nombre}")

        # Solicitar al usuario que elija una sala disponible
        id_sala_disponible = int(input("Ingrese el ID de la sala disponible que desea reservar: "))

        # Buscar la sala disponible
        sala_disponible = None
        aux = self.primero
        while aux is not None:
            if aux.sala.id_sala == id_sala_disponible:
                sala_disponible = aux.sala
                break
            aux = aux.siguiente

        if sala_disponible is None:
            print(f"Sala con ID {id_sala_disponible} no encontrada.")
            return

        # Solicitar horas para la nueva reserva
        horas_reservar = int(input(f"Ingrese la cantidad de horas que desea reservar para la sala '{sala_disponible.nombre}': "))

        # Calcular el costo total de la nueva reserva
        costo_total = sala_disponible.tarifa_por_hora * horas_reservar

        # Aplicar descuento si es necesario
        if horas_reservar > 8:
            descuento = costo_total * 0.15  # 15% de descuento
            costo_total -= descuento
            print(f"Se aplicó un descuento del 15%. Total después de descuento: ${costo_total:.2f}")

        # Cambiar los estados de ambas salas y actualizar el costo de la nueva sala reservada
        sala_reservada.estado = "disponible"
        sala_disponible.estado = "reservada"
        sala_disponible.costo_total = costo_total  # Guardar el costo total de la nueva reserva

        print(f"La sala '{sala_reservada.nombre}' (ID: {id_sala_reservada}) ahora está disponible.")
        print(f"La sala '{sala_disponible.nombre}' (ID: {id_sala_disponible}) ha sido reservada por {horas_reservar} horas.")
        print(f"Costo total de la reserva: ${costo_total:.2f}")


    def reservar_sala(self):
        if self.vacia():
            print("No hay salas registradas.")
            return

        aux = self.primero
        sala_disponible = []

        print("Salas disponibles para reserva:")
        while aux is not None:
            if aux.sala.estado.lower() == "disponible":
                # Mostrar detalles de la sala
                print(f"ID: {aux.sala.id_sala}")
                print(f"Nombre: {aux.sala.nombre}")
                print(f"Tipo: {aux.sala.tipo}")
                print(f"Capacidad máxima: {aux.sala.capacidad_maxima}")
                print(f"Tarifa por hora: ${aux.sala.tarifa_por_hora:.2f}")
                print("--------------------")
                sala_disponible.append(aux.sala)  # Agregar sala a la lista de disponibles
            aux = aux.siguiente  # Avanzar al siguiente nodo

        if not sala_disponible:
            print("No hay salas disponibles en este momento.")
            return

        # Solicitar al usuario que elija una sala para reservar
        id_sala_reservar = int(input("Ingrese el ID de la sala que desea reservar: "))
        sala_a_reservar = None

        for sala in sala_disponible:
            if sala.id_sala == id_sala_reservar:
                sala_a_reservar = sala
                break

        if sala_a_reservar is None:
            print("El ID de la sala ingresado no es válido.")
            return

        # Solicitar horas a reservar
        horas_reservar = int(input("Ingrese la cantidad de horas que desea reservar: "))
        
        # Calcular el costo total
        costo_total = sala_a_reservar.tarifa_por_hora * horas_reservar

        # Aplicar descuento si las horas son mayores a 8
        if horas_reservar > 8:
            descuento = costo_total * 0.15  # 15% de descuento
            costo_total -= descuento
            print(f"Se aplicó un descuento del 15%. Total después de descuento: ${costo_total:.2f}")

        # Cambiar el estado de la sala a "reservada" y guardar el costo total en el objeto Sala
        sala_a_reservar.estado = "reservada"
        sala_a_reservar.costo_total = costo_total  # Guardar el costo total
        print(f"La sala '{sala_a_reservar.nombre}' (ID: {sala_a_reservar.id_sala}) ha sido reservada por {horas_reservar} horas.")
        print(f"Costo total de la reserva: ${costo_total:.2f}")


    def dinero_total(self):
        aux = self.primero
        total = 0  # Inicializa el total en 0

        while aux is not None:
            if aux.sala.estado.lower() == "reservada":  # Solo sumar las salas reservadas
                total += aux.sala.costo_total  # Sumar el costo total de cada sala reservada
            aux = aux.siguiente  # Avanzar al siguiente nodo

        print(f"Dinero total acumulado por las reservas: ${total:.2f}")
        return total  # Retornar el total acumulado


    
    def mostrar_sala_reservada_por_tipo(self, tipo):
        aux = self.primero
        resultado = []

        while aux is not None:
            if aux.sala.tipo.lower() == tipo.lower() and aux.sala.estado.lower() == "reservada":
                resultado.append(aux.sala)
            aux = aux.siguiente  # Avanzar al siguiente nodo

        if resultado:
            print(f"Salas reservadas del tipo '{tipo}':")
            for sala in resultado:
                print(sala)
        else:
            print(f"No se encontraron salas reservadas del tipo '{tipo}'.")













