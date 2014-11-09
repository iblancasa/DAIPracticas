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
	return ""

def getApellidos():
	return ""

def getCorreo():
	return ""

def getDiaNacimiento():
	return ""

def getMesNacimiento():
	return ""

def getPassword():
	return ""

def getAnoNacimiento():
	return ""

def getDireccion():
	return ""

def getNumeroVisa():
	return ""

def getFormaPago():
	return ""


def close():
	db.close()
