from fractions import Fraction
import sympy

ask = ""
A = []
B = []
k = 0
g = 0
LU = []
while ask != "1" and ask != "2" and ask != "3":
    ask = input("1)Doo-Little\n2)Crout\n3)Cholesky\nChoose: ")
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


def equation_solver(equation):
    k, start, end = 0, 0, 0
    number, temp, temp2 = [], [], []
    equation = list(equation)
    eq = equation[equation.index("=")::-1][::-1]
    output = equation[equation.index("=") + 1::]
    for i in range(len(eq)):
        temp.append(eq[i])
        if (eq[i + 1] == "+" or eq[i + 1] == "-" or eq[i - 1] == "+" or eq[i - 1] == "-") and (
                eq[i + 1] != "*" and eq[i - 1] != "*"):  # 3*x + 2 =
            # if all(item.isdigit() for item in temp):
            #     number = temp
            #     end = len(temp)
            #     break
            if eq[i - 1] == "-":
                number.append("-")
                k = 1
            j = i
            while eq[j] != "=" and eq[j] != "+" and eq[j] != "-" and eq[j] != "*":
                number.append(eq[j])
                j += 1
            start = i - k
            end = j
            break
        # else:
        #     for d in eq:
        #         if d.isdigit() or d == "+" or d == "-":
        #             temp2.append(d)
        #     if temp2[len(temp2) - 1] == "+" or temp2[len(temp2) - 1] == "-":
        #         temp2.pop()
        #     temp2 = "".join(temp2)
        #     output = "".join(output)
        #     return eval(output) / eval(temp2)
    if number[0] != "+" and number[0] != "-":
        output.append("-")
        for m in range(start, end):
            output.append(eq[m])
        for p in range(len(number)):
            eq.pop(start)
        if eq[0] == "*":
            eq.pop(0)
    elif number[0] == '-':
        output.append("+")
        for m in range(start + 1, end):
            output.append(eq[m])
        for p in range(len(number)):
            eq.pop(start)
        if eq[0] == "*":
            eq.pop(0)
    elif number[0] == '+':
        output.append("-")
        for m in range(start, end):
            output.append(eq[m])
        for p in range(len(number)):
            eq.pop(start)
        if eq[0] == "*":
            eq.pop(0)
    for d in eq:
        if d.isdigit() or d == "+" or d == "-":
            temp2.append(d)
    if temp2[len(temp2) - 1] == "+" or temp2[len(temp2) - 1] == "-":
        temp2.pop()

    output = eval("".join(output))
    temp2 = eval("".join(temp2))
    return output / temp2


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
            L[i][j] = "abcdefghijklmnopqrstuvwxyz"[g]
            g += 1
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
            U[i][j] = "abcdefghijklmnopqrstuvwxyz"[g]
            g += 1
    print("U : ")
    printer_2dimensions(U, 6)


    def update():
        global LU
        LU1 = sympy.Matrix(L).multiply(sympy.Matrix(U))
        LU = []
        k = 0
        for i in range(n):  # making LU1 into LU =  List inside Lists
            l_lines = []
            for j in range(n):
                l_lines.append(LU1[k])
                k += 1
            LU.append(l_lines)


    update()
    print("L*U : ")
    printer_2dimensions(LU, 24)
    print("L*U = A :\n")

    for i in range(n):  # printing the equations
        for j in range(n):
            print(f"{LU[i][j]} = {A[i][j]}")

    for i in range(n):
        U[0][i] = A[0][i]
    update()
    printer_2dimensions(LU, 24)

if ask == "2":
    pass

else:
    pass
