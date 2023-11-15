def encode_rle(data):
    if not data:
        return ""

    encoded_data = ""
    count = 1
    prev_char = data[0]

    for char in data[1:]:
        if char == prev_char:
            count += 1
        else:
            encoded_data += str(count) + prev_char
            count = 1
            prev_char = char

    encoded_data += str(count) + prev_char

    return encoded_data


def decode_rle(encoded_data):
    decoded_data = ""
    i = 0

    while i < len(encoded_data):
        count = ""
        while i < len(encoded_data) and encoded_data[i].isdigit():
            count += encoded_data[i]
            i += 1
        char = encoded_data[i]
        decoded_data += char * int(count)
        i += 1

    return decoded_data


# Exemple 1
data = "AAABBBCCD"
encoded_data = encode_rle(data)
decoded_data = decode_rle(encoded_data)
print("Exemple 1:")
print("Données d'origine:", data)
print("Données encodées:", encoded_data)
print("Données décodées:", decoded_data)
print()
