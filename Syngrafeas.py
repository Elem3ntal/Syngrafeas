#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from source import config
from source.log import log
from pathlib import Path

CONFIG = {}
log = log()
write = log.write

class Syngrafeas:
    def __init__(self, modeRun=None):
        self.modeRun = modeRun
        self.books = []
        self.config = CONFIG['books']

    def book_append(self, bookname = None):
        if type(bookname) is type("cadena"):
            book_path = self.config['TXT_PATH']+bookname+self.config['TXT_EXT']
            my_file = Path(book_path)
            if my_file.is_file():
                self.books.append(bookname)
                write("libro agregado")
                with open(book_path, 'r') as content_file:
                    content = content_file.read()
                for expresion in self.config['parser']:
                    while expresion['from'] in content:
                        content = content.replace(expresion['from'], expresion['to'])
                statements = content.split('.')
                sin_puntos = content.replace('.',' ')
                sin_puntos = sin_puntos.replace(',',' ')
                sin_puntos = sin_puntos.replace('  ',' ')
                print(list(set(sin_puntos.split(' '))))
                print("palabras: ", len(list(set(sin_puntos.split(' ')))))
                print("cantidad de oraciones: ", len(statements))
                prom = sum([len(sentence) for sentence in statements])/len(statements)
                print("largo promedio de oracion: ", prom)
                #input("pausa")
                #print(content)
            else:
                write("libro no existe")
    def book_getAll(self):
        return self.books

if __name__ == '__main__':
    try:
        CONFIG = config.CONFIG
    except:
        write("Unreachable configuration", TYPE=1)
        sys.exit(0)
    write(sys.argv)
    if len(sys.argv) > 1:
        write("modeRun Overide: ", bool(sys.argv[2]), TYPE=0)
    write("Debug: ", CONFIG['debug'])
    write("CONFIG: ", CONFIG)
    syngrafeas = Syngrafeas()
    write("ruta libros: ",CONFIG['books']['TXT_PATH'])
    syngrafeas.book_append("quijote")
    write(syngrafeas.book_getAll())