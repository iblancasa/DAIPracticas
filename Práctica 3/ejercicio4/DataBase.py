#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import anydbm

db = anydbm.open('basedatos.db', 'c')

def insertar(nombre,apellidos,correo,dianacimiento,mesnacimiento,anonacimiento,direccion,password,numerovisa,formapago):
	db['nombre'] = nombre
	db['apellidos'] = apellidos
	db['correo'] = correo
	db['dianacimiento'] = dianacimiento
	db['mesnacimiento'] = mesnacimiento
	db['anonacimiento'] = anonacimiento
	db['direccion'] = direccion
	db['password'] = password
	db['numerovisa'] = numerovisa
	db['formapago'] = formapago


def getNombre():
	return db['nombre']

def getApellidos():
	return db['apellidos']

def getCorreo():
	return db['correo']

def getDiaNacimiento():
	return db['dianacimiento']

def getMesNacimiento():
	return db['dianacimiento']

def getPassword():
	return db['password']

def getAnoNacimiento():
	return db['anonacimiento']

def getDireccion():
	return db['direccion']

def getNumeroVisa():
	return db['numerovisa']

def getFormaPago():
	return db['formapago']


def close():
	db.close()