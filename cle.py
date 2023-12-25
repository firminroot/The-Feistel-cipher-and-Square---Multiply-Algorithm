def generate_feistel_keys(key, permutation, shift_order):
    # Vérification de la longueur de la clé
    if len(key) != 8:
        raise ValueError("La clé doit être de longueur 8.")

    # Vérification de la longueur de la permutation
    if len(permutation) != 8:
        raise ValueError("La permutation doit être de longueur 8.")

    # Vérification de l'ordre de décalage
    if shift_order <= 0:
        raise ValueError("L'ordre de décalage doit être supérieur à zéro.")

    # Conversion de la clé en une liste de caractères
    key_list = list(key)

    # Conversion de la permutation en une liste d'indices
    p = [int(i) for i in permutation]

    # Décalage à gauche de la clé
    shift_amount = shift_order % 8
    shifted_key = key_list[shift_amount:] + key_list[:shift_amount]

    # Application de la permutation à la clé décalée
    permuted_key = [shifted_key[i] for i in p]

    # Division de la clé permuée en deux sous-clés
    sub_key1 = permuted_key[:4]
    sub_key2 = permuted_key[4:]

    return sub_key1, sub_key2


# Exemple d'utilisation
key = input("Entrez la clé (8 caractères) : ")
permutation = input("Entrez la permutation (8 chiffres distincts) : ")
shift_order = int(input("Entrez l'ordre de décalage : "))

sub_key1, sub_key2 = generate_feistel_keys(key, permutation, shift_order)
print("Sous-clé 1 :", sub_key1)
print("Sous-clé 2 :", sub_key2)