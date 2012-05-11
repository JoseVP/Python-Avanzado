#!/usr/python
# -*- coding: utf-8 -*-

import re

patron_fecha="^([a-zA-Z]+\s*)+[0-3]?\d/(Ene|Feb|Mar|Abr|May|Jun|Jul|Ago|Sep|Oct|Nov|Dic)/2\d{3}\s+[0-2]?\d:[0-5]?\d\s+(A|P)M$"

fecha =raw_input("Introduzca Poblacion y fecha a validar : ")

if re.match(patron_fecha,fecha):
    print "La fecha introducida es valida"
else:
    print "La fecha introducida es erronea, revisela"