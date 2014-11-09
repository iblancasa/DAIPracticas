#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import DataBase

if __name__ == "__main__":
	DataBase.insertar("paco","rodriguez jimenez","paco fontanero",
		"15","1","1992","calle hortaliza","asddf","4444-4444-4444-4444","tarjeta")

	print DataBase.getNombre()