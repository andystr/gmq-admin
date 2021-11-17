# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from sqlalchemy.orm import relationship, session
from apps import db

class vehiculo(db.Model):

    __tablename__ = 'vehiculos'

    id = db.Column(db.Integer, primary_key=True)
    placa = db.Column(db.String)
    chassis = db.Column(db.String)
    motor = db.Column(db.String)
    marca = db.Column(db.String)
    modelo = db.Column(db.String)
    anio = db.Column(db.String)
    clase = db.Column(db.String)
    color = db.Column(db.String)
    cilindraje = db.Column(db.Integer)
    transmision = db.Column(db.String)
    combustible = db.Column(db.String)
    paisOrigen = db.Column(db.String)
    kilometraje = db.Column(db.Integer)
    precio = db.Column(db.Float)
    pasajeros = db.Column(db.Integer)
    capacidadCarga = db.Column(db.Integer)
    estado = db.Column(db.String)
    equipamiento = db.Column(db.String)
    costo = db.Column(db.Float)
    idPropietario = db.Column(db.String)
    telefonoPropietario = db.Column(db.Integer)
    
    
    def __init__(self):
        self.id = id
        #self.nombresPropietario = db.session.query(vehiculo, persona).filter(persona.id == vehiculo.idPropietario).filter(persona.id == 1).all()                        

class persona(db.Model):

    __tablename__ = 'personas'

    id = db.Column(db.Integer, primary_key=True)
    ccruc = db.Column(db.Integer)
    nombres = db.Column(db.String)
    apellidos = db.Column(db.String)
    telefono = db.Column(db.String)
    direccion = db.Column(db.String)
    email = db.Column(db.String)
    estado = db.Column(db.String)

    def __init__(self, id=None, ccruc=None):
        self.id = id

class transaccion(db.Model):

    __tablename__ = 'transacciones'

    id = db.Column(db.Integer, primary_key=True)
    idProveedor = db.Column(db.String)
    idConsumidor = db.Column(db.String)
    idProductoServicio = db.Column(db.String)
    idValorMonetario = db.Column(db.String)


class stats():
    vehiculosActivos = vehiculo
    numVehiculosActivos = db.Integer
    vehiculosReservados = vehiculo
    numVehiculosReservados = db.Integer
    vehiculosProspectos = vehiculo
    numVehiculosProspectos = db.Integer
    vehiculosVendidos = vehiculo
    numVehiculosVendidos = db.Integer

    def __init__(self):
        self.vehiculosActivos = db.session.query(vehiculo).filter_by(estado="Disponible")
        self.numVehiculosActivos = db.session.query(vehiculo).filter_by(estado="Disponible").count()
        self.vehiculosReservados = db.session.query(vehiculo).filter_by(estado="Reservado")
        self.numVehiculosReservados = db.session.query(vehiculo).filter_by(estado="Reservado").count()
        self.vehiculosProspectos = db.session.query(vehiculo).filter_by(estado="Prospecto")
        self.numVehiculosProspectos = db.session.query(vehiculo).filter_by(estado="Prospecto").count()
        self.vehiculosVendidos = db.session.query(vehiculo).filter_by(estado="Vendido")
        self.numVehiculosVendidos = db.session.query(vehiculo).filter_by(estado="Vendido").count()

    
