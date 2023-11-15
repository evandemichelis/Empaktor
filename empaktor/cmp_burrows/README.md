# Algorithme de Burrows-Wheeler

## Transformée de Burrows-Wheeler

### Prototype
```python
def transform_bwt(data: str) -> Tuple[str, int]:
    """
    Transforme les données en utilisant l'algorithme de Burrows-Wheeler.

    Parameters:
        - data (str): Les données à transformer.

    Returns:
        - Tuple[str, int]: Les données transformées et l'index de la rotation d'origine.
    """
    # Implémentation...

# Autres prototypes et explications...

## Exemple d'utilisation
```python
data = "banana"
transformed_data, key = transform_bwt(data)
original_data = inverse_bwt(transformed_data, key)
print("Données d'origine:", data)
print("Transformée de Burrows-Wheeler:", transformed_data)
print("Données inversées:", original_data)
