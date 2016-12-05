# coding: utf-8
import os
import zipfile
import sys

def main(path):

    zfile = None
    try:
        zfile = zipfile.ZipFile(path)
    except FileNotFoundError:
        print("Arquivo {} não existe".format(path))
        sys.exit(-1)
    else:
        zfile.extractall()
        print("Arquivos extraídos")
    finally:
        zfile.close(), print("Closing File...") if zfile else None

if __name__ == '__main__':
    main(sys.argv[1])
