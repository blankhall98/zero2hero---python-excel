import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# lectura de la base de datos clientes
ruta_clientes = './raw/clientes.csv'
clientes = pd.read_csv(ruta_clientes)

action = input('Ver la base de datos (ver) o Agregar nuevo cliente (nuevo): ')

#cliente escoge ver base de datos
if action == 'ver':
    print('\n'+'BASE DE DATOS CLIENTES'+'\n'+'--------------------')
    print(clientes)
#cliente escoge agregar nuevo usuario
elif action == 'nuevo':
    print('\n'+'AGREGAR NUEVO CLIENTE'+'\n'+'--------------------')
    print('Por favor, responde las siguientes preguntas')
    #recolectar la información del cliente
    nombre = input('Nombre: ')
    apellido = input('Apellido: ')
    sexo = input('Sexo (Masculino/Femenino): ')
    edad = input('Edad: ')
    print(f'¡Hola {nombre} {apellido}, {sexo} de {edad} años!')
    #agregar la información a la base de datos
    nuevo_cliente = [nombre,apellido,edad,sexo]

    #agregar renglon
    n = len(clientes)
    clientes.loc[n] = nuevo_cliente

    #sobreescribir la base
    clientes.to_csv(ruta_clientes,index=False)

#cliente no escoge opción válida
else:
    print('Opción no válida')