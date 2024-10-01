# modulo de salas 


class Sala:
    def __init__(self, id_sala, tipo, capacidad_maxima, nombre, tarifa_por_hora, estado="Disponible"):
        self.id_sala = id_sala               # Identificador único de la sala
        self.tipo = tipo                     # Tipo de sala (Pequeña, Mediana, Grande)
        self.capacidad_maxima = capacidad_maxima  # Capacidad máxima de personas
        self.nombre = nombre                 # Nombre de la sala
        self.tarifa_por_hora = tarifa_por_hora   # Tarifa por hora de uso
        self.estado =estado                 # Estado de la sala (Disponible/Reservada)

    def __str__(self):
        return (f"Información de la salas:\n"
                f"Sala ID: {self.id_sala}\n"
                f"Nombre: {self.nombre}\n"
                f"Tipo: {self.tipo}\n"
                f"Capacidad: {self.capacidad_maxima}\n"
                f"Tarifa por hora: ${self.tarifa_por_hora}\n"
                f"Estado: {self.estado}\n")
    
    # Método para marcar la sala como disponible
    def hacer_disponible(self):
        self.estado = "disponible"
        print(f"La sala {self.id_sala} ahora está disponible para reservar.")

    # Método para marcar la sala como reservada
    def hacer_reservada(self):
        self.estado = "reservada"
        print(f"La sala {self.id_sala} ahora está reservada.")
