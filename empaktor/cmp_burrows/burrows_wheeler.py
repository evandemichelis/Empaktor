def transform_bwt(data):
    rotations = [data[i:] + data[:i] for i in range(len(data))]
    sorted_rotations = sorted(rotations)
    transformed_data = "".join(rotation[-1] for rotation in sorted_rotations)
    key = sorted_rotations.index(data)
    return transformed_data, key


def inverse_bwt(transformed_data, key):
    table = [''] * len(transformed_data)
    for i in range(len(transformed_data)):
        table = sorted([transformed_data[i] + table[i] for i in range(len(transformed_data))])
    original_data = table[key]
    return original_data


# Exemple 1
data = "banana"
transformed_data, key = transform_bwt(data)
original_data = inverse_bwt(transformed_data, key)
print("Exemple 1:")
print("Données d'origine:", data)
print("Transformée de Burrows-Wheeler:", transformed_data)
print("Données inversées:", original_data)
