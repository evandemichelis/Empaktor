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

    encoded_data += str(count) + prev_char + "😄"

    return encoded_data


def decode_rle(encoded_data):
    decoded_data = ""
    parts = encoded_data.split("😄")

    for part in parts:
        if part:
            count, char = part[:-1], part[-1]
            decoded_data += char * int(count)

    return decoded_data


# Exemple 1
data = "111111111111111e"
encoded_data = encode_rle(data)
decoded_data = decode_rle(encoded_data)
print("Exemple 1:")
print("Données d'origine:", data)
print("Données encodées:", encoded_data)
print("Données décodées:", decoded_data)
print()
