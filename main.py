from fractions import Fraction
import sympy

ask = ""
A = []
B = []
while ask != "1" and ask != "2":
    ask = input("1)Doo-Little\n2)Crout\nChoose: ")
n = int(input("number of equations : "))


def printer_2dimensions(any_list, lenght):
    for LINES in range(n):
        print("∣  ", end="")
        for COLUMNS in range(n):
            try:
                print(
                    f"{str(Fraction(any_list[LINES][COLUMNS]).limit_denominator(max_denominator=10000)):{int(lenght)}}",
                    end=' ')
            except:
                print(f"{str(any_list[LINES][COLUMNS]):{int(lenght)}}", end=' ')
        print("∣")
    print()


def printer_1dimension(any1_list):
    for K in any1_list:
        print(f"∣ {str(Fraction(K).limit_denominator(max_denominator=10000))} ∣")
    print()


def equation_solver(unkonw):
    pass


# making the matrix
for lines in range(n):
    lines_list = []
    equations = input(f"Equation {lines + 1} = ")
    for columns in range(n):
        if columns == 0:
            v = float(equations[0: equations.index("x")])
        else:
            v = float(equations[
                      equations.index("xyzabcdefghijklmnopqrstuvw"[columns - 1]) + 1: equations.index(
                          "xyzabcdefghijklmnopqrstuvw"[columns])])

        lines_list.append(v)
    w = equations[equations.index("=") + 1::]
    B.append(float(w))
    A.append(lines_list)
print("A : ")
printer_2dimensions(A, 6)

if ask == "1":
    L = []
    U = []
    # making L
    for i in range(n):  # making the identity
        L_lines = []
        for j in range(n):
            if i == j:
                L_lines.append(1)
            else:
                L_lines.append(0)
        L.append(L_lines)
    for j in range(n):  # Lower Part
        for i in range(j + 1, n):
            L[i][j] = f"l{i + 1}{j + 1}"
    print("L : ")
    printer_2dimensions(L, 6)
    # making U
    for i in range(n):  # matrix with 0's
        U_lines = []
        for j in range(n):
            U_lines.append(0)
        U.append(U_lines)

    for i in range(n):  # upper part
        for j in range(i, n):
            U[i][j] = f"u{i + 1}{j + 1}"
    print("U : ")
    printer_2dimensions(U, 6)

    LU1 = sympy.Matrix(L).multiply(sympy.Matrix(U))

    LU = []
    k = 0
    for i in range(n):  # making LU1 into LU =  List inside Lists
        l_lines = []
        for j in range(n):
            l_lines.append(LU1[k])
            k += 1
        LU.append(l_lines)
    print("L*U : ")
    printer_2dimensions(LU, 24)

    print("L*U = A :\n")
    for i in range(n):  # printing the equations
        for j in range(n):
            print(f"{LU[i][j]} = {A[i][j]}")

if ask == "2":
    pass
