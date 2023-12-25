def square_and_multiply(x, b, n):
    # Conversion de l'exposant en binaire
    binary_exp = bin(b)[2:]

    # Initialisation du résultat
    result = 1

    # Parcours du binaire de droite à gauche
    for bit in binary_exp[::-1]:
        if bit == '1':
            result = (result * x) % n
        x = (x * x) % n

    return result


# Exemple d'utilisation
x = int(input("Entrez la valeur de x : "))
b = int(input("Entrez la valeur de b : "))
n = int(input("Entrez la valeur de n : "))

result = square_and_multiply(x, b, n)
print("Résultat :", result)