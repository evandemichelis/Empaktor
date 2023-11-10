# empaktor.py

import argparse
import os
import tarfile
from burrows_wheeler import transform_bwt, inverse_bwt
from huffman import compress_data
from rle import encode_rle, decode_rle

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
            compressed_data = compress_data(data)
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
                decompressed_data = decompress_data(file_data)
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
                decompressed_data = decode_rle(file_data)
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

def main():
    parser = argparse.ArgumentParser(description="Empaktor - Compression and Decompression Tool")
    parser.add_argument("archive_name", type=str, help="Name of the archive file")
    parser.add_argument("--compression", type=str, help="Compression algorithm (huffman, rle, bwt)")
    parser.add_argument("files", type=str, nargs="*", help="List of files to process")

    args = parser.parse_args()

    if not args.compression or not args.files:
        print("Please specify a compression algorithm and a list of files.")
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
