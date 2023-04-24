# Variables

my_string_variable = "My String Variable"
print(my_string_variable)

my_int_variable = 5  # defino mi variable entera
print(my_int_variable)

# defino que mi variable entera sera un string
my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
# compruebo si el cambio de mi int a str fue correcto
print(type(my_int_to_str_variable))

my_bool_variable = True
print(my_bool_variable)

# ahora crearemos un print uniendo varias variables ---> concatenacion de variables
print(my_string_variable, my_int_variable, my_bool_variable)
print("este es el numero:", my_int_variable)

# Funciones del sistema
# len devuelve el numero de espacios usados en cualqueir variable
print(len(my_string_variable))

# imput
primer_nombre = input("mi primer nombre es: ")
edad = input("mi edad es: ")
print(primer_nombre)
print(edad)

# Variables en una sola linea
nombre, apellido, edad, alias = "Jorge", "Quispe", 35, "George"
print("mi nombre es:", nombre, apellido,
      ". Mi edad es:", edad,  ". Y mi alias es:", alias)
