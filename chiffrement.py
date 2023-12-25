def feistel_cipher(plain_text, permutation, shift_order, num_rounds):
    # Vérification de la longueur de la permutation
    if len(permutation) != 8:
        raise ValueError("La permutation doit être de longueur 8.")

    # Vérification de l'ordre de décalage
    if shift_order <= 0:
        raise ValueError("L'ordre de décalage doit être supérieur à zéro.")

    # Conversion du texte en une liste de caractères
    text = list(plain_text)

    # Conversion de la permutation en une liste d'indices
    p = [int(i) for i in permutation]

    # Boucle principale
    for _ in range(num_rounds):
        left = text[:4]
        right = text[4:]

        # Application de la permutation
        permuted_right = [right[i] for i in p]

        # Décalage à gauche du bloc de droite
        shift_amount = shift_order % 4
        shifted_right = permuted_right[shift_amount:] + permuted_right[:shift_amount]

        # XOR entre le bloc de gauche et le bloc de droite décalé
        result = [chr(ord(left[i]) ^ ord(shifted_right[i])) for i in range(4)]

        # Échange des blocs
        text = right + result

    # Conversion de la liste de caractères en une chaîne de texte chiffrée
    cipher_text = ''.join(text)
    return cipher_text


# Exemple d'utilisation
plain_text = input("Entrez le texte à chiffrer : ")
permutation = input("Entrez la permutation (8 chiffres distincts) : ")
shift_order = int(input("Entrez l'ordre de décalage : "))
num_rounds = int(input("Entrez le nombre de tours : "))

cipher_text = feistel_cipher(plain_text, permutation, shift_order, num_rounds)
print("Texte chiffré :", cipher_text)