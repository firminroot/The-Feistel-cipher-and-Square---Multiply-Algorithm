def feistel_decipher(cipher_text, permutation, shift_order, num_rounds):
    # Vérification de la longueur de la permutation
    if len(permutation) != 8:
        raise ValueError("La permutation doit être de longueur 8.")

    # Vérification de l'ordre de décalage
    if shift_order <= 0:
        raise ValueError("L'ordre de décalage doit être supérieur à zéro.")

    # Conversion du texte chiffré en une liste de caractères
    text = list(cipher_text)

    # Conversion de la permutation en une liste d'indices inverses
    p = [0] * 8
    for i, val in enumerate(permutation):
        p[int(val)] = i

    # Boucle principale (déchiffrement inverse)
    for _ in range(num_rounds):
        left = text[:4]
        right = text[4:]

        # XOR entre le bloc de gauche et le bloc de droite décalé
        shift_amount = shift_order % 4
        shifted_right = left

        # Décalage à droite du bloc de droite
        shifted_right += right[:4 - shift_amount]
        shifted_right = right[4 - shift_amount:] + shifted_right

        result = [chr(ord(shifted_right[i]) ^ ord(left[i])) for i in range(4)]

        # Application de la permutation inverse
        permuted_right = [result[i] for i in p]

        # Échange des blocs
        text = permuted_right + right

    # Conversion de la liste de caractères en une chaîne de texte déchiffrée
    plain_text = ''.join(text)
    return plain_text


# Exemple d'utilisation
cipher_text = input("Entrez le texte chiffré : ")
permutation = input("Entrez la permutation (8 chiffres distincts) : ")
shift_order = int(input("Entrez l'ordre de décalage : "))
num_rounds = int(input("Entrez le nombre de tours : "))

plain_text = feistel_decipher(cipher_text, permutation, shift_order, num_rounds)
print("Texte déchiffré :", plain_text)