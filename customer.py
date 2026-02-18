# pylint: disable=duplicate-code
"""Modulo para la gestion de Clientes."""
import json
import os


class Customer:
    """Clase que representa un Cliente."""

    FILE_NAME = "customers.json"

    def __init__(self, customer_id, name, email):
        """Inicializa cliente."""
        self.customer_id = customer_id
        self.name = name
        self.email = email

    def to_dict(self):
        """Convierte a diccionario."""
        return {
            "customer_id": self.customer_id,
            "name": self.name,
            "email": self.email
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
            print(f"Error al leer clientes: {error}")
            return []

    @classmethod
    def _save_data(cls, customers):
        """Guarda datos JSON."""
        try:
            with open(cls.FILE_NAME, 'w', encoding='utf-8') as file:
                json.dump(customers, file, indent=4)
        except IOError as error:
            print(f"Error al guardar clientes: {error}")

    @classmethod
    def create_customer(cls, customer_id, name, email):
        """Crea un cliente."""
        data = cls._load_data()
        if any(c['customer_id'] == customer_id for c in data):
            return False
        new_c = cls(customer_id, name, email)
        data.append(new_c.to_dict())
        cls._save_data(data)
        return True

    @classmethod
    def delete_customer(cls, customer_id):
        """Elimina un cliente."""
        data = cls._load_data()
        updated = [c for c in data if c['customer_id'] != customer_id]
        if len(data) == len(updated):
            return False
        cls._save_data(updated)
        return True

    @classmethod
    def display_customer(cls, customer_id):
        """Muestra cliente."""
        data = cls._load_data()
        for c in data:
            if c['customer_id'] == customer_id:
                return c
        return None

    @classmethod
    def modify_customer(cls, customer_id, **kwargs):
        """Modifica cliente."""
        data = cls._load_data()
        for c in data:
            if c['customer_id'] == customer_id:
                c.update(kwargs)
                cls._save_data(data)
                return True
        return False
