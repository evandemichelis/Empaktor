class Node:
    def __init__(self, char, frequency):
        self.char = char
        self.frequency = frequency
        self.left = None
        self.right = None


def compress_data(data):
    """
    Compresses data using the Huffman algorithm.

    Args:
        data: The string of characters to compress.

    Returns:
        The compressed data.
    """

    # Create a frequency table of the characters in the data.
    frequencies = {}
    for char in data:
        if char not in frequencies:
            frequencies[char] = 0
        frequencies[char] += 1

    # Create a Huffman tree from the frequency table.
    nodes = [Node(char, frequency) for char, frequency in frequencies.items()]

    while len(nodes) > 1:
        nodes.sort(key=lambda node: node.frequency)
        left_node, right_node = nodes.pop(0), nodes.pop(0)

        new_node = Node(None, left_node.frequency + right_node.frequency)
        new_node.left = left_node
        new_node.right = right_node

        nodes.append(new_node)

    root = nodes[0]

    # Create a code table where each character is associated with its Huffman code.
    code_table = {}
    def traverse(node, code):
        if node.char is not None:
            code_table[node.char] = code
            # Stop traversing if we have reached a leaf node.
            return

        traverse(node.left, code + "0")
        traverse(node.right, code + "1")


    # Convert the data to compressed form by appending the corresponding Huffman codes.
    compressed_data = ""
    for char in data:
        compressed_data += code_table[char]

    return compressed_data



# Exemple 1
data = "aabbbccdddd"
compressed_data = compress_data(data)
print("Données compressées:", compressed_data)
