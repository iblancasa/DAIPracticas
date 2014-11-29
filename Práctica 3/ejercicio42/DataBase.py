#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import pymongo
from pymongo import MongoClient

connection = MongoClient()
db = connection.usuarios.usuarios

def insertar(nombre,apellidos,correo,dianacimiento,mesnacimiento,anonacimiento,direccion,password,numerovisa,formapago):
	usuario = {'nombre':nombre,
		'apellidos':apellidos,
		'correo':correo,
		'dianacimiento':dianacimiento,
		'mesnacimiento':mesnacimiento,
		'anonacimiento':anonacimiento,
		'direccion':direccion,
		'password':password,
		'numerovisa':numerovisa,
		'formapago':formapago
	}
	db.insert(usuario)

def getNombre(nombre):
	results = db.find({'nombre':nombre})
	for record in results:
		return record['nombre']

def getApellidos(nombre):
	results = db.find({'nombre':nombre})
	for record in results:
		return record['apellidos']

def getCorreo(nombre):
	results = db.find({'nombre':nombre})
	for record in results:
		return record['correo']

def getDiaNacimiento(nombre):
	results = db.find({'nombre':nombre})
	for record in results:
		return record['dianacimiento']

def getMesNacimiento(nombre):
	results = db.find({'nombre':nombre})
	for record in results:
		return record['mesnacimiento']

def getPassword(nombre):
	results = db.find({'nombre':nombre})
	for record in results:
		return record['password']

def getAnoNacimiento(nombre):
	results = db.find({'nombre':nombre})
	for record in results:
		return record['anonacimiento']

def getDireccion(nombre):
	results = db.find({'nombre':nombre})
	for record in results:
		return record['direccion']

def getNumeroVisa(nombre):
	results = db.find({'nombre':nombre})
	for record in results:
		return record['numerovisa']

def getFormaPago(nombre):
	results = db.find({'nombre':nombre})
	for record in results:
		return record['formapago']


def close():
	connection.close()
