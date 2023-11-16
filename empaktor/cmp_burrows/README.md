# Burrows-Wheeler Transformation

This Python script implements the Burrows-Wheeler Transformation, a reversible text transformation used in data compression algorithms. The transformation rearranges characters in a string to improve compression efficiency.

## Files

- `burrows_wheller.py`: Contains functions for Burrows-Wheeler transformation and its inverse.

## Usage

### Transforming Data

To transform data using Burrows-Wheeler, use the `transform_bwt` function:

```python
from burrows_wheller import transform_bwt, inverse_bwt

# Exemple 1
data = "banana"
transformed_data, key = transform_bwt(data)
original_data = inverse_bwt(transformed_data, key)

print("Exemple 1 :")
print("Données d'origine :", data)
print("Transformation de Burrows-Wheeler :", transformed_data)
print("Données inversées :", original_data)
