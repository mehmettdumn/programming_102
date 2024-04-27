# Prompting the user to enter three floating-point numbers
a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))

# Calculating the arithmetic mean
arithmetic_mean = (a + b + c) / 3

# Calculating the harmonic mean
harmonic_mean = 3 / (1/a + 1/b + 1/c)

# Printing the arithmetic mean
print("Arithmetic Mean:", arithmetic_mean)

# Printing the harmonic mean
print("Harmonic Mean:", harmonic_mean)
