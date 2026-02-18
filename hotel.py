# pylint: disable=duplicate-code
"""Modulo para la gestion de Hoteles."""
import json
import os


class Hotel:
    """Clase que representa un Hotel y su persistencia."""

    FILE_NAME = "hotels.json"

    def __init__(self, hotel_id, name, location, rooms):
        """Inicializa la instancia de Hotel."""
        self.hotel_id = hotel_id
        self.name = name
        self.location = location
        self.rooms = rooms

    def to_dict(self):
        """Convierte instancia a diccionario."""
        return {
            "hotel_id": self.hotel_id,
            "name": self.name,
            "location": self.location,
            "rooms": self.rooms
        }

    @classmethod
    def _load_data(cls):
        """Carga datos desde JSON."""
        if not os.path.exists(cls.FILE_NAME):
            return []
        try:
            with open(cls.FILE_NAME, 'r', encoding='utf-8') as file:
                return json.load(file)
        except (json.JSONDecodeError, IOError) as error:
            print(f"Error al leer hoteles: {error}")
            return []

    @classmethod
    def _save_data(cls, hotels):
        """Guarda datos en JSON."""
        try:
            with open(cls.FILE_NAME, 'w', encoding='utf-8') as file:
                json.dump(hotels, file, indent=4)
        except IOError as error:
            print(f"Error al guardar hoteles: {error}")

    @classmethod
    def create_hotel(cls, hotel_id, name, location, rooms):
        """Crea un hotel nuevo."""
        hotels = cls._load_data()
        if any(h['hotel_id'] == hotel_id for h in hotels):
            print(f"Error: ID {hotel_id} ya existe.")
            return False
        new_hotel = cls(hotel_id, name, location, rooms)
        hotels.append(new_hotel.to_dict())
        cls._save_data(hotels)
        return True

    @classmethod
    def delete_hotel(cls, hotel_id):
        """Elimina un hotel."""
        hotels = cls._load_data()
        updated = [h for h in hotels if h['hotel_id'] != hotel_id]
        if len(hotels) == len(updated):
            return False
        cls._save_data(updated)
        return True

    @classmethod
    def display_hotel(cls, hotel_id):
        """Muestra info de un hotel."""
        hotels = cls._load_data()
        for hotel in hotels:
            if hotel['hotel_id'] == hotel_id:
                return hotel
        return None

    @classmethod
    def modify_hotel(cls, hotel_id, **kwargs):
        """Modifica info de un hotel."""
        hotels = cls._load_data()
        for hotel in hotels:
            if hotel['hotel_id'] == hotel_id:
                hotel.update(kwargs)
                cls._save_data(hotels)
                return True
        return False
