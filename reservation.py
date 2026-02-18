# pylint: disable=duplicate-code
"""Modulo para la gestion de Reservas."""
import json
import os


class Reservation:
    """Clase que representa una Reserva."""

    FILE_NAME = "reservations.json"

    def __init__(self, res_id, customer_id, hotel_id):
        """Inicializa reserva."""
        self.res_id = res_id
        self.customer_id = customer_id
        self.hotel_id = hotel_id

    def to_dict(self):
        """Convierte a diccionario."""
        return {
            "res_id": self.res_id,
            "customer_id": self.customer_id,
            "hotel_id": self.hotel_id
        }

    @classmethod
    def _load_data(cls):
        """Carga datos JSON."""
        if not os.path.exists(cls.FILE_NAME):
            return []
        try:
            with open(cls.FILE_NAME, 'r', encoding='utf-8') as file:
                return json.load(file)
        except (json.JSONDecodeError, IOError) as error:
            print(f"Error al leer reservas: {error}")
            return []

    @classmethod
    def _save_data(cls, data):
        """Guarda datos JSON."""
        try:
            with open(cls.FILE_NAME, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4)
        except IOError as error:
            print(f"Error al guardar reservas: {error}")

    @classmethod
    def create_reservation(cls, res_id, customer_id, hotel_id):
        """Crea reserva."""
        data = cls._load_data()
        new_res = cls(res_id, customer_id, hotel_id)
        data.append(new_res.to_dict())
        cls._save_data(data)
        return True

    @classmethod
    def cancel_reservation(cls, res_id):
        """Cancela reserva."""
        data = cls._load_data()
        updated = [r for r in data if r['res_id'] != res_id]
        if len(data) == len(updated):
            return False
        cls._save_data(updated)
        return True
