# deploy_manual.py
import sys

respuesta = input("¿Confirmas deploy? (s/n): ")
if respuesta.lower() != 's':
    print("Deploy cancelado")
    sys.exit(1)
print("Deploy manual ejecutado correctamente")