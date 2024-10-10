#solictar al usuario una vocal en minúscula
vocal_minúscula = input("Introduce una vocal en minúscula")

# solicitar al usuario una vocal en mayúscula
vocal_mayúscula = input("Introduce una vocal mayúscula")

# invertir la vocal minúscula a mayúscula
vocal_minúscula_convertida = vocal_minúscula.upper()

#convertir vocal mayúscula a munúscula
vocal_mayúscula_convertida = vocal_mayúscula.lower()

#concatenar ambas
resultado = vocal_minúscula_convertida + vocal_mayúscula_convertida

#resultado
print(f"Resultado de la concatenación: {resultado}")