# cadena inicial
cadena = "Te quiero sólo como amigo"

# imprimir los dos primeros caracteres
print(f"Los dos primeros caracteres: {cadena[:2]}")

# imprimir los últimos dos caracteres
print(f"Los dos últimos caracteres: {cadena[-3:]}") 

# imprimir la cadena cada dos caracteres
print(f"cadena cada dos caracteres: {cadena[::2]}")

# imprimir la cadena en sentido inverso
print(f"cadena en sentido inverso: {cadena[::-1]}")

# imprimir la cadena en un sentido y luego en sentido inverso
cadena_inversa = cadena[::-1]
print(f"Cadena en ambos sentidos: {cadena + cadena_inversa}")