def solve_quadratic_equation(a, b, c):
    
    discriminant = b**2 - 4*a*c
    
    if discriminant > 0:
    
        root1 = (-b + discriminant**0.5) / (2*a)
        root2 = (-b - discriminant**0.5) / (2*a)
        print()
        print("Корінь 1:", root1)
        print("Корінь 2:", root2)
    elif discriminant == 0:
    
        root = -b / (2*a)
        print()
        print("Корінь:", root)
    else:

        real_part = -b / (2*a)
        imaginary_part = (abs(discriminant)**0.5) / (2*a)
        print()
        print("Корінь 1:", real_part, "+", imaginary_part, "i")
        print("Корінь 2:", real_part, "-", imaginary_part, "i")

a = float(input("Введіть коефіцієнт a: "))
b = float(input("Введіть коефіцієнт b: "))
c = float(input("Введіть коефіцієнт c: "))

solve_quadratic_equation(a, b, c)