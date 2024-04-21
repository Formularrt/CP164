from functions import is_valid

print("var:", is_valid("var"))  # Expected output: True
print("var2:", is_valid("var2"))  # Expected output: True
print("2var:", is_valid("2var"))  # Expected output: False
print("var?:", is_valid("var?"))  # Expected output: False
print("camelCase:", is_valid("camelCase"))  # Expected output: True