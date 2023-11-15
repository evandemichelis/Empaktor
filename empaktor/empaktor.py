import argparse
import os
import tarfile
import io
from compression.burrows_wheeler import transform_bwt, inverse_bwt
from compression.huffman import buildHuffmanTree
from compression.rle import encode_rle, decode_rle


def compress_huffman(archive_name, files):
    """
    Compression de fichiers en utilisant l'algorithme de Huffman.

    Parameters:
    archive_name (str): Le nom du fichier d'archive compressé à créer.
    files (list): La liste des noms de fichiers à compresser.

    Example:
    archive_name = "compressed.tar.gz"
    files = ["file1.txt", "file2.txt"]
    compress_huffman(archive_name, files)
    """
    with tarfile.open(archive_name, "w:gz") as tar:
        for file in files:
            with open(file, "r") as f:
                data = f.read()
            compressed_data = buildHuffmanTree(data)
            tarinfo = tarfile.TarInfo(name=os.path.basename(file))
            tarinfo.size = len(compressed_data)
            tar.addfile(tarinfo, fileobj=io.BytesIO(compressed_data.encode()))


def decompress_huffman(archive_name):
    """
    Décompression de fichiers en utilisant l'algorithme de Huffman.

    Parameters:
    archive_name (str): Le nom de l'archive compressée à extraire.

    Example:
    archive_name = "compressed.tar.gz"
    decompress_huffman(archive_name)
    """
    with tarfile.open(archive_name, "r:gz") as tar:
        for tarinfo in tar:
            if tarinfo.isreg():
                file_data = tar.extractfile(tarinfo).read()
                decompressed_data = buildHuffmanTree(file_data.decode())  # Utilisation de la fonction correcte pour la décompression Huffman
                with open(tarinfo.name, "w") as f:
                    f.write(decompressed_data)


def compress_rle(archive_name, files):
    """
    Compression de fichiers en utilisant l'algorithme RLE (Run-Length Encoding).

    Parameters:
    archive_name (str): Le nom du fichier d'archive compressé à créer.
    files (list): La liste des noms de fichiers à compresser.

    Example:
    archive_name = "compressed.tar.gz"
    files = ["file1.txt", "file2.txt"]
    compress_rle(archive_name, files)
    """
    with tarfile.open(archive_name, "w:gz") as tar:
        for file in files:
            with open(file, "r") as f:
                data = f.read()
            compressed_data = encode_rle(data)
            tarinfo = tarfile.TarInfo(name=os.path.basename(file))
            tarinfo.size = len(compressed_data)
            tar.addfile(tarinfo, fileobj=io.BytesIO(compressed_data.encode()))

def decompress_rle(archive_name):
    """
    Décompression de fichiers en utilisant l'algorithme RLE (Run-Length Encoding).

    Parameters:
    archive_name (str): Le nom de l'archive compressée à extraire.

    Example:
    archive_name = "compressed.tar.gz"
    decompress_rle(archive_name)
    """
    with tarfile.open(archive_name, "r:gz") as tar:
        for tarinfo in tar:
            if tarinfo.isreg():
                file_data = tar.extractfile(tarinfo).read()
                print(f"Compressed Data for {tarinfo.name}: {file_data}")
                decompressed_data = decode_rle(file_data)
                print(f"Decompressed Data for {tarinfo.name}: {decompressed_data}")
                with open(tarinfo.name, "w") as f:
                    f.write(decompressed_data)

def compress_bwt(archive_name, files):
    """
    Compression de fichiers en utilisant l'algorithme de Burrows-Wheeler.

    Parameters:
    archive_name (str): Le nom du fichier d'archive compressé à créer.
    files (list): La liste des noms de fichiers à compresser.

    Example:
    archive_name = "compressed.tar.gz"
    files = ["file1.txt", "file2.txt"]
    compress_bwt(archive_name, files)
    """
    with tarfile.open(archive_name, "w:gz") as tar:
        for file in files:
            with open(file, "r") as f:
                data = f.read()
            transformed_data, key = transform_bwt(data)
            compressed_data = f"{key}:{transformed_data}"
            tarinfo = tarfile.TarInfo(name=os.path.basename(file))
            tarinfo.size = len(compressed_data)
            tar.addfile(tarinfo, fileobj=io.BytesIO(compressed_data.encode()))

def decompress_bwt(archive_name):
    """
    Décompression de fichiers en utilisant l'algorithme de Burrows-Wheeler.

    Parameters:
    archive_name (str): Le nom de l'archive compressée à extraire.

    Example:
    archive_name = "compressed.tar.gz"
    decompress_bwt(archive_name)
    """
    with tarfile.open(archive_name, "r:gz") as tar:
        for tarinfo in tar:
            if tarinfo.isreg():
                file_data = tar.extractfile(tarinfo).read().decode()
                key, transformed_data = file_data.split(":", 1)
                original_data = inverse_bwt(transformed_data, int(key))
                with open(tarinfo.name, "w") as f:
                    f.write(original_data)

def extract(archive_name):
    """
    Extraction des fichiers d'une archive compressée.

    Parameters:
    archive_name (str): Le nom de l'archive compressée à extraire.

    Example:
    archive_name = "compressed.tar.gz"
    extract(archive_name)
    """
    with tarfile.open(archive_name, "r:gz") as tar:
        tar.extractall()


def main():
    parser = argparse.ArgumentParser(description="Empaktor - Compression and Decompression Tool")
    parser.add_argument("archive_name", type=str, help="Name of the archive file")
    parser.add_argument("--compression", type=str, help="Compression algorithm (huffman, rle, bwt)")
    parser.add_argument("--files", type=str, nargs="*",
                        help="List of files to process. If using 'bwt' compression, provide only one file.")
    parser.add_argument("--extract", action="store_true", help="Extract files from the archive")

    args = parser.parse_args()

    if args.extract:
        extract(args.archive_name)
        return

    if not args.compression or not args.files:
        print("Please specify a compression algorithm and a list of files.")
        return

    if args.compression == "bwt" and len(args.files) != 1:
        print("If using 'bwt' compression, provide only one file.")
        return

    if args.compression == "huffman":
        compress_huffman(args.archive_name, args.files)
    elif args.compression == "rle":
        compress_rle(args.archive_name, args.files)
    elif args.compression == "bwt":
        compress_bwt(args.archive_name, args.files)
    else:
        print("Unsupported compression algorithm. Please use huffman, rle, or bwt.")

if __name__ == "__main__":
    main()
