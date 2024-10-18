### Variables ###

my_string_variable = "My String variable"
print(my_string_variable)

my_float_variable = 1.22
print(my_float_variable)

my_int_to_str_variable = int(my_float_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

# Concatenación de variables en un print
print(my_string_variable, my_int_to_str_variable, my_bool_variable)
print(len("Este es el valor de:"), my_bool_variable, "hola mundo", my_string_variable)

#Algunas funciones del sistema
print(len(my_string_variable))
first_name = "Nicolas"
print("Primer nombre: ", len(first_name))
print("Primer nombre: ", first_name)

#Variables en una sola línea -- ¡Cuidado con abusar de esta sintaxis!
name, surname, alias, age = "Nicolas", "Cordero", "Nico", int(20.1)
print("Me llamo:", name, surname, "Mi edad es:", age, "Y mi alias es:", alias)
print(type(age))

#Inputs
name = input('¿Cuál es tu nombre? ')
age = input('¿Cuántos años tienes? ')
deporte = input('Cuál es tu deporte favorito? ')
print(name)
print(age)

print("Hola",name,"Tienes",age,"años.")
print("Tu deporte favorito es:", deporte)

#Cambiamos su tipo
name = 20
age = "Nicolas"
print(name)
print(age)

# ¿Forzamos el tipo?
direccion: str = "carrera 10b 20-44"
direccion = 30
direccion: float = 20.2
print(type(direccion))