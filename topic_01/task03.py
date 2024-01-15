def calculate_discriminant(a, b, c):
    discriminant = b**2 - 4*a*c
    return discriminant

a = 3
b = -9
c = 4

result = calculate_discriminant(a, b, c)
print("Дискримінант рівняння:", result)