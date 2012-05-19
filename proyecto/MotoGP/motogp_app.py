#!/usr/bin/env python
# -*- coding: utf-8 -*-
import MySQLdb
from gi.repository import Gtk
   
    
    

class Moto_GP:
   
    def onVerCircuito(self,menuitem):
        imagen = self.builder.get_object('imagen_circuito')
        imagen.set_from_file(self.cargar_imagenes(menuitem.get_label()))
        
        
        
        
    
    def cargar_imagenes(self,circuito):
        imagenes= {    'Qatar' : 'resources/circuitos/qatar-cir.jpg',
                        'España' : 'resources/circuitos/espana-cir.jpg',
                        'Portugal' : 'resources/circuitos/portugal-cir.jpg',
                        'Francia' : 'resources/circuitos/francia-cir.jpg',
                        'Cataluña' : 'resources/circuitos/catalunya-cir.jpg',
                        'Gran Bretaña' : 'resources/circuitos/gran_bretanya-cir.jpg',
                        'Holanda' : 'resources/circuitos/holanda-cir.jpg',
                        'Alemania' : 'resources/circuitos/alemania-cir.jpg',
                        'Italia' : 'resources/circuitos/italia-cir.jpg',
                        'Estados Unidos' : 'resources/circuitos/estados_unidos-cir.jpg',
                        'Indianapolis' : 'resources/circuitos/indianapolis-cir.jpg',
                        'Republica Checa' : 'resources/circuitos/republica_checa-cir.jpg',
                        'San Marino' : 'resources/circuitos/san_marino-cir.jpg',
                        'Aragon' : 'resources/circuitos/aragon-cir.jpg',
                        'Japon' : 'resources/circuitos/japon-cir.jpg',
                        'Malasia' : 'resources/circuitos/malasia-cir.jpg',
                        'Australia' : 'resources/circuitos/australia-cir.jpg',
                        'Valencia' : 'resources/circuitos/valencia-cir.jpg',
                        }
                        
        return imagenes[circuito]
    
    
    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("interfaz.glade")
        self.handlers = {   "onDeleteWindow": Gtk.main_quit,
                            "onVerCircuito": self.onVerCircuito,
                            }                
        self.builder.connect_signals(self.handlers)
        self.window = self.builder.get_object("window1")
        self.window.show_all()
        
        
         
    
def main():
    window = Moto_GP()
    Gtk.main()

    return 0

if __name__ == '__main__':
    main()
