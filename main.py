from fractions import Fraction

import sympy

ask = ""
A = []
B = []
k = 0
g = 0
LU, values = [], []

while ask != "1" and ask != "2" and ask != "3":
    ask = input("1)DooLittle\n2)Crout\nChoose: ")  # NOQA
n = int(input("number of equations : "))


def printer_2dimensions(any_list, lenght):  # NOQA
    for LINES in range(n):
        print("∣  ", end="")
        for COLUMNS in range(n):
            try:
                print(
                    f"{str(Fraction(float(any_list[LINES][COLUMNS])).limit_denominator(max_denominator=100000)):{int(lenght)}}",
                    end=' ')
            except (ValueError, TypeError):
                print(f"{str(any_list[LINES][COLUMNS]):{int(lenght)}}", end=' ')
        print("∣")
    print()


def is_number(num):
    try:
        float(num)
        return True
    except (ValueError, TypeError):
        return False


def printer_1dimension(any1_list):
    for K in any1_list:
        try:
            print(f"∣  {str(Fraction(K).limit_denominator(max_denominator=100000)):3} ∣")
        except (ValueError, TypeError):
            print(f"∣ {K} ∣")
    print()


def equation_solver(equation):
    k, start, end = 0, 0, 0  # NOQA
    number, temp, temp2, temp4 = [], [], [], []
    equation = list(equation)
    eq = equation[equation.index("=")::-1][::-1]
    output = equation[equation.index("=") + 1::]
    for i in range(len(eq)):  # NOQA
        temp.append(eq[i])  # all values of the loop
        for b in eq:  # remove all spaces
            if b == " ":
                eq.remove(" ")
        if (eq[i + 1] == "+" or eq[i + 1] == "-" or eq[i - 1] == "+" or eq[i - 1] == "-") and (
                eq[i + 1] != "*" and eq[i - 1] != "*") and is_number(eq[i]):  # the number with this conditions
            temp3 = []
            j = i  # NOQA
            if all(item.isdigit() or item == "." for item in temp):  # specific problem
                number = temp
                end = len(temp)
                break
            while eq[j] != "*" and eq[j] != '=':  # loop to solve -5(5) * x + (3)3 =
                temp3.append(eq[j])
                j += 1
                if eq[j] == "*" or eq[j] == "=":
                    temp3.append(eq[j])
            if temp3[len(temp3) - 1] != "*":  # start adding
                if eq[i - 1] == "-":
                    number.append("-")
                    k = 1  # NOQA
                h = i  # NOQA
                while eq[h] != "=" and eq[h] != "+" and eq[h] != "-" and eq[h] != "*":
                    number.append(eq[h])
                    h += 1
                start = i - k
                end = h
                break
        if i == len(eq) - 2:
            if len(eq) == 2:
                return ''.join(output)
            if len(eq) == 3 and eq[0] == "-":
                return eval(f"-{''.join(output)}")
            if eq[0] == "-":
                temp4.append("-")
            for c in eq:
                if is_number(c) or c == ".":
                    temp4.append(c)
            return eval(''.join(output)) / eval("".join(temp4))

    if len(number) == 0:  # simple equation problem
        for d in eq:
            if d.isdigit() or d == "+" or d == "-":
                temp2.append(d)
        if temp2[len(temp2) - 1] == "+" or temp2[len(temp2) - 1] == "-":
            temp2.pop()
        temp2 = "".join(temp2)
        output = "".join(output)
        return eval(output) / eval(temp2)

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

    if len(eq) == 3:
        return eval(''.join(output))
    if len(eq) == 4 and eq[0] == "-":
        return eval(f"-{''.join(output)}")
    if len(eq) == 2:
        return eval(''.join(output))
    for d in eq:
        if d.isdigit() or d == "+" or d == "-" or d == "." and eq[eq.index(d) + 1] != "=":
            temp2.append(d)

    if len(temp2) == 2:
        temp2.append(1)

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
                      equations.index("xyzabcdefghijklmnopqrstuvw"[columns - 1]) + 1: equations.index(  # NOQA
                          "xyzabcdefghijklmnopqrstuvw"[columns])])  # NOQA

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
            L[i][j] = "abcdefghijklmnopqrstuvwxyz"[g]  # NOQA
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
            U[i][j] = "abcdefghijklmnopqrstuvwxyz"[g]  # NOQA
            g += 1
    print("U : ")
    printer_2dimensions(U, 6)


    def update():
        global LU
        LU1 = sympy.Matrix(L).multiply(sympy.Matrix(U))  # NOQA
        LU = []
        k = 0  # NOQA
        for i in range(n):  # NOQA  # making LU1 into LU =  List inside Lists
            l_lines = []
            for j in range(n):  # NOQA
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

    for y in range(n):
        for t in range(n):
            if not is_number(L[y][t]):
                values.append(str(L[y][t]) + " = " + str(
                    Fraction(equation_solver(f"{LU[y][t]}={A[y][t]}")).limit_denominator(max_denominator=10000)))
                L[y][t] = equation_solver(f"{LU[y][t]}={A[y][t]}")
                update()
        for r in range(n):
            if not is_number(U[y][r]):
                values.append(str(U[y][r]) + " = " + str(
                    Fraction(equation_solver(f"{LU[y][r]}={A[y][r]}")).limit_denominator(max_denominator=10000)))
                U[y][r] = equation_solver(f"{LU[y][r]}={A[y][r]}")
                update()
        update()
    print()

    for f in range(n ** 2):
        print(values[f])

    print("L : ")
    printer_2dimensions(L, 6)
    print("U : ")
    printer_2dimensions(U, 6)
    Y = []
    for h in range(n):  # making Y
        Y.append("abcdefghujklmnopqrstuvw"[h])  # NOQA
    LY = []


    def update2():
        global LY
        LY = []
        LY1 = sympy.Matrix(L).multiply(sympy.Matrix(Y))  # NOQA
        for y in range(n):  # NOQA
            LY.append(LY1[y])


    update2()
    for l in range(n):  # NOQA  # finding Y
        Y[l] = equation_solver(f"{LY[l]}={B[l]}")
        update2()

    print("Y : ")
    printer_1dimension(Y)
    X = []
    for x in range(n):  # making X
        X.append("xyzabcdefghujklmnopqrstuvw"[x])  # NOQA
    UX = []


    def update3():
        global UX
        UX = []
        UX1 = sympy.Matrix(U).multiply(sympy.Matrix(X))  # NOQA
        for v in range(n):  # NOQA
            UX.append(UX1[v])


    update3()
    print('UX = Y :')
    for j in range(n):  # UX = Y
        print(f"{UX[j]} = {Y[j]}")

    for x in range(n - 1, -1, -1):  # finding X
        X[x] = equation_solver(f"{UX[x]} = {Y[x]}")
        update3()
    print("X : ")
    printer_1dimension(X)
    counter = 0
    for answers in X:
        print(
            f'{"xyzabcdefghijklmnopqrstuvwxyz"[counter]} = {str(Fraction(answers).limit_denominator(max_denominator=100000))}')  # NOQA
        counter += 1

if ask == "2":
    L = []
    U = []
    # making L
    for i in range(n):  # List with 0's
        L_lines = []
        for j in range(n):
            L_lines.append(0)
        L.append(L_lines)

    for j in range(n):  # Lower Part
        for i in range(0, j + 1):
            L[j][i] = "abcdefghijklmnopqrstuvwxyz"[g]  # NOQA
            g += 1
    print("L : ")
    printer_2dimensions(L, 6)
    # making U
    for i in range(n):  # making the identity
        U_lines = []
        for j in range(n):
            if i == j:
                U_lines.append(1)
            else:
                U_lines.append(0)
        U.append(U_lines)
    for j in range(n - 1):  # Upper Part
        for i in range(j + 1, n):
            U[j][i] = "abcdefghijklmnopqrstuvwxyz"[g]  # NOQA
            g += 1

    print("U : ")
    printer_2dimensions(U, 6)


    def update():
        global LU
        LU1 = sympy.Matrix(L).multiply(sympy.Matrix(U))  # NOQA
        LU = []
        k = 0  # NOQA
        for i in range(n):  # NOQA  # making LU1 into LU =  List inside Lists
            l_lines = []
            for j in range(n):  # NOQA
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

    for y in range(n):
        for t in range(n):
            if not is_number(L[y][t]):
                values.append(str(L[y][t]) + " = " + str(
                    Fraction(equation_solver(f"{LU[y][t]}={A[y][t]}")).limit_denominator(max_denominator=10000)))
                L[y][t] = equation_solver(f"{LU[y][t]}={A[y][t]}")
                update()
        for r in range(n):
            if not is_number(U[y][r]):
                values.append(str(U[y][r]) + " = " + str(
                    Fraction(equation_solver(f"{LU[y][r]}={A[y][r]}")).limit_denominator(max_denominator=10000)))
                U[y][r] = equation_solver(f"{LU[y][r]}={A[y][r]}")
                update()
        update()
    print()

    for f in range(n ** 2):
        print(values[f])

    print("L : ")
    printer_2dimensions(L, 6)
    print("U : ")
    printer_2dimensions(U, 6)
    Y = []
    for h in range(n):  # making Y
        Y.append("abcdefghujklmnopqrstuvw"[h])  # NOQA
    LY = []


    def update2():
        global LY
        LY = []
        LY1 = sympy.Matrix(L).multiply(sympy.Matrix(Y))  # NOQA
        for y in range(n):  # NOQA
            LY.append(LY1[y])


    update2()
    for l in range(n):  # NOQA  # finding Y
        Y[l] = equation_solver(f"{LY[l]}={B[l]}")
        update2()

    print("Y : ")
    printer_1dimension(Y)
    X = []
    for x in range(n):  # making X
        X.append("xyzabcdefghujklmnopqrstuvw"[x])  # NOQA
    UX = []


    def update3():
        global UX
        UX = []
        UX1 = sympy.Matrix(U).multiply(sympy.Matrix(X))  # NOQA
        for v in range(n):  # NOQA
            UX.append(UX1[v])


    update3()
    print('UX = Y :')
    for j in range(n):  # UX = Y
        print(f"{UX[j]} = {Y[j]}")

    for x in range(n - 1, -1, -1):  # finding X
        X[x] = equation_solver(f"{UX[x]} = {Y[x]}")
        update3()
    print("X : ")
    printer_1dimension(X)
    counter = 0
    for answers in X:
        print(
            f'{"xyzabcdefghijklmnopqrstuvwxyz"[counter]} = {str(Fraction(answers).limit_denominator(max_denominator=100000))}')  # NOQA
        counter += 1
