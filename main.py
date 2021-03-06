import AdditionalOperations
import MatrixOperations
import VectorOperations

choice = input("""
This is PyCalc. Select from the following:
1) Vector Calculator
2) Matrices Calculator
3) Additional Features
""")
if choice == "1":
    vector_selection = input("""
Selection Menu:
1) Norm 
2) Unit Vector
3) Scalar Multiplication
4) Addition
5) Subtraction
6) Dot Product
7) Angle
8) Cross Product (Only for 3D vectors)
""")

    if vector_selection == "1":
        size = int(input("Enter the size of the vector:"))
        vector = [int(input("Enter value for the vector: ")) for i in range(size)]
        norm = VectorOperations.norm(vector)
        print("Norm: ", norm)
    if vector_selection == "2":
        size = int(input("Enter the size of the vector:"))
        vector = [int(input("Enter value for vector: ")) for i in range(size)]
        unit_vector = VectorOperations.unit(vector)
        print(unit_vector)
    if vector_selection == "3":
        size = int(input("Enter the size of the vector:"))
        vector = [int(input("Enter Value for Vector: ")) for i in range(size)]
        scalar = float(input("Please input scale factor: "))
        scaled_vector = VectorOperations.scalar_multiply(vector, scalar)
        print(scaled_vector)
    if vector_selection == "4":
        size = int(input("Enter the size of the vectors:"))
        vector = [int(input("Enter value for vector 1: ")) for i in range(size)]
        vector2 = [int(input("Enter value for vector 2: ")) for i in range(size)]
        vector_sum = VectorOperations.add(vector, vector2)
        print(vector_sum)
    if vector_selection == "5":
        size = int(input("Enter the size of the vectors:"))
        vector = [int(input("Enter value for minuend vector: ")) for i in range(size)]
        vector2 = [int(input("Enter values of subtrahend vector: ")) for i in range(size)]
        vector_difference = VectorOperations.subtract(vector, vector2)
        print(vector_difference)
    if vector_selection == "6":
        size = int(input("Enter the size of the vectors:"))
        vector = [int(input("Enter Value for Vector 1: ")) for i in range(size)]
        vector2 = [int(input("Enter Values for Vector 2: ")) for i in range(size)]
        dot_product = VectorOperations.dot(vector, vector2)
        print("Dot Product: ", dot_product)
    if vector_selection == "7":
        size = int(input("Enter the size of the vectors:"))
        vector = [int(input("Enter value for vector 1: ")) for i in range(size)]
        vector2 = [int(input("Enter values for vector 2: ")) for i in range(size)]
        vector_angle = VectorOperations.angle(vector, vector2)
        print("Angle: ", round(vector_angle, 2), " radians")
    if vector_selection == "8":
        vector = [int(input("Enter value for vector 1: ")) for i in range(3)]
        vector2 = [int(input("Enter values for vector 2: ")) for i in range(3)]
        cross = VectorOperations.cross_product(vector, vector2)
        print(cross)
elif choice == "2":
    matrix_selection = input("""
Selection Menu: 
1) Determinant 
2) Transpose 
3) Inverse
4) Scalar Multiplication
5) Trace
6) Addition
7) Subtraction
8) Multiplication
9) Matrix Power
""")

    if matrix_selection == "1":
        dimensions = int(input("Enter the dimensions of the SQUARE matrix:"))
        matrix = [[int(input("Enter Value: ")) for i in range(dimensions)] for j in range(dimensions)]
        determinant = MatrixOperations.determinant(matrix)
        print("Determinant: ", determinant)
    elif matrix_selection == "2":
        dimensions = int(input("Enter the dimensions of the SQUARE matrix:"))
        matrix = [[int(input("Enter Value: ")) for i in range(dimensions)] for j in range(dimensions)]
        transpose = MatrixOperations.transpose(matrix)
        MatrixOperations.print_matrix(transpose)
    elif matrix_selection == "3":
        dimensions = int(input("Enter the dimensions of the SQUARE matrix:"))
        matrix = [[int(input("Enter Value: ")) for i in range(dimensions)] for j in range(dimensions)]
        inverse = MatrixOperations.inverse(matrix)
        MatrixOperations.print_matrix(inverse)
    elif matrix_selection == "4":
        dimensions = int(input("Enter the dimensions of the SQUARE matrix:"))
        matrix = [[int(input("Enter Value: ")) for i in range(dimensions)] for j in range(dimensions)]
        scalar = float(input("Please input the scalar:"))
        scaled_matrix = MatrixOperations.scalar_multiply(matrix, scalar)
        MatrixOperations.print_matrix(scaled_matrix)
    elif matrix_selection == "5":
        dimensions = int(input("Enter the dimensions of the SQUARE matrix:"))
        matrix = [[int(input("Enter Value: ")) for i in range(dimensions)] for j in range(dimensions)]
        trace = MatrixOperations.trace(matrix)
        print("Trace: ", trace)
    elif matrix_selection == "6":
        columns = int(input("Enter the number of columns in the matrices:"))
        rows = int(input("Enter the number of rows in the matrices:"))
        matrix1 = [[int(input("Enter Values for Matrix 1: ")) for i in range(columns)] for j in range(rows)]
        matrix2 = [[int(input("Enter Values for Matrix 2: ")) for i in range(columns)] for j in range(rows)]
        sum_matrix = MatrixOperations.add(matrix1, matrix2)
        MatrixOperations.print_matrix(sum_matrix)
    elif matrix_selection == "7":
        columns = int(input("Enter the number of columns in the matrices:"))
        rows = int(input("Enter the number of rows in the matrices:"))
        matrix1 = [[int(input("Enter Values for Matrix 1: ")) for i in range(columns)] for j in range(rows)]
        matrix2 = [[int(input("Enter Values for Matrix 2: ")) for i in range(columns)] for j in range(rows)]
        diff_matrix = MatrixOperations.sub(matrix1, matrix2)
        MatrixOperations.print_matrix(diff_matrix)
    elif matrix_selection == "8":
        columns1 = int(input("Enter the number of columns in matrix 1:"))
        rows1 = int(input("Enter the number of rows in matrix 1:"))
        columns2 = int(input("Enter the number of columns in matrix 2:"))
        rows2 = int(input("Enter the number of rows in matrix 2:"))
        if columns1 != rows2:
            print("Incompatible Matrices")
        else:
            matrix1 = [[int(input("Enter Values for Matrix 1: ")) for i in range(columns1)] for j in range(rows1)]
            matrix2 = [[int(input("Enter Values for Matrix 2: ")) for i in range(columns2)] for j in range(rows2)]
            product = MatrixOperations.multiply(matrix1, matrix2)
            MatrixOperations.print_matrix(product)
    elif matrix_selection == "9":
        dimensions = int(input("Enter the dimensions of the SQUARE matrix:"))
        matrix = [[int(input("Enter Value: ")) for i in range(dimensions)] for j in range(dimensions)]
        n = input("Enter the power: ")
        pow_matrix = MatrixOperations.matrix_pow(matrix, n)
elif choice == "3":
    print("Number Theory Calculator")
    user_input = input("""Choose a Function:
             1) Modulo
             2) Greatest Common Divisor 
             3) Lowest Common Multiple
             4) Factorial
             5) Choose
             6) IsPrime
             7) NPrimes
             8) Maximum
             9) Minimum
             10) Permutation
             11) Parity
             12) Factors
    """)

    if user_input == "1":
        dividend = int(input("Input the dividend: "))
        divisor = int(input("Input the divisor: "))
        modulo = AdditionalOperations.modulo(dividend, divisor)
        print("Modulo: ", modulo)
    elif user_input == "2":
        num1 = int(input("Input first number: "))
        num2 = int(input("Input second number: "))
        GCD = AdditionalOperations.gcd(num1, num2)
        print("GCD: ", GCD)
    elif user_input == "3":
        num1 = int(input("Input first number: "))
        num2 = int(input("Input second number: "))
        LCM = AdditionalOperations.lcm(num1, num2)
        print("LCM: ", LCM)
    elif user_input == "4":
        num = int(input("Input number: "))
        factorial = AdditionalOperations.factorial(num)
        print("Factorial: ", factorial)
    elif user_input == "5":
        n = int(input("Input n: "))
        r = int(input("Input r: "))
        choose = AdditionalOperations.choose(n, r)
        print("nCr: ", choose)
    elif user_input == "6":
        num = int(input("Input number: "))
        prime = AdditionalOperations.is_prime(num)
        print("Is prime? ", prime)
    elif user_input == "7":
        num = int(input("Input the number of Primes: "))
        AdditionalOperations.n_primes(num)
    elif user_input == "8":
        num1 = int(input("Input first number: "))
        num2 = int(input("Input second number: "))
        maximum = AdditionalOperations.maximum(num1, num2)
        print("Max: ", maximum)
    elif user_input == "9":
        num1 = int(input("Input first number: "))
        num2 = int(input("Input second number: "))
        minimum = AdditionalOperations.minimum(num1, num2)
        print("Min: ", minimum)
    elif user_input == "10":
        n = int(input("Input n: "))
        r = int(input("Input r: "))
        permutations = AdditionalOperations.permutation(n, r)
        print("nPr: ", permutations)
    elif user_input == "11":
        num = int(input("Input number: "))
        parity = AdditionalOperations.parity(num)
        print("Parity: ", parity)
    elif user_input == "12":
        num = int(input("Input number: "))
        factors = AdditionalOperations.factors(num)
        print("Factors:", factors)
    else:
        print("Try Again")
