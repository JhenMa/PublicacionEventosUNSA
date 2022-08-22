from abc import ABC, abstractmethod
from Evento import Evento

class Lista_Evento(ABC):
    @abstractmethod
    def agregar_evento(self,nuevoIdEvento):
        pass
    @abstractmethod
    def mostrarEventos(self):
        pass