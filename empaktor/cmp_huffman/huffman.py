import heapq
# Module permettant de manipuler des tas
from heapq import heappop, heappush
# heappop: extraie le plus petit élément de heap en préservant l'invariant du tas
# heappush: introduit la valeur item dans le tas heap, en conservant l'invariance du tas


def leaf(root):
    return root.left is None and root.right is None
# Créé un modèle de feuille portant deux racines


class Node:
    def __init__(self, ch, freq, left=None, right=None):
        # __init__ : méthode appelée lors de la création d'une instance pour initialiser des attributs
        self.ch = ch
        self.freq = freq
        self.left = left
        self.right = right
# Donnne à un noeud ses attributs

    def __lt__(self, other):
        # __lt__ : méthode utilisée pour définir une opération de comparaison "inférieur que" (<) pour les objets d'une classe, avec "other"
        return self.freq < other.freq
# Place les caractères les moins fréquents avant les plus fréquents


def encode(root, s, huffman_code):

    if root is None:
        return

    if leaf(root):
        huffman_code[root.ch] = s if len(s) > 0 else '1'
# Attribue des codes binaires aux caractères en parcourant l'arbre

    encode(root.left, s + '0', huffman_code)
    encode(root.right, s + '1', huffman_code)
# Fonction parcourant l'arbre et reconstruisant le code


def decode(root, index, s):

    if root is None:
        return index

    if leaf(root):
        print(root.ch, end='')
        return index

    index = index + 1
    root = root.left if s[index] == '0' else root.right
    return decode(root, index, s)
# Lis et retourne en format décompressé le contenu d'une chaine encodée avec l'algorithme de Huffman


def buildHuffmanTree(text):

    if len(text) == 0:
        return
# Retourne si la chaine est vide
    freq = {i: text.count(i) for i in text}
    pq = [Node(k, v) for k, v in freq.items()]
    heapq.heapify(pq)
# Construit un tas avec les nœuds de l'arbre basé sur la fréquence des caractères

    while len(pq) != 1:
        left = heappop(pq)
        right = heappop(pq)

        total = left.freq + right.freq
        heappush(pq, Node(None, total, left, right))
# Construit l'arbre en fusionnant les nœuds avec les fréquences les plus basses

    root = pq[0]

    huffmanCode = {}
    encode(root, '', huffmanCode)

    print('Characters are:         ', huffmanCode)
    print('The original string is: ', text)

    s = ''
    for i in text:
        s += huffmanCode.get(i)
# Encode la chaine d'origine avec les codes de Huffman

    print('The encoded string is:  ', s)
    print('The decoded string is:   ', end='')

    if leaf(root):
        while root.freq > 0:
            print(root.ch, end='')
            root.freq = root.freq - 1
    else:
        index = -1
        while index < len(s) - 1:
            index = decode(root, index, s)
# Décodage de la chaine binaire avec l'arbre de Huffman


text = 'aabbbccdddd'
buildHuffmanTree(text)
print('')
# Exécute le programme avec une chaine de caractères
