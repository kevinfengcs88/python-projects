import sys

code = []

A = ".-"
B = "-..."
C = "-.-."
D = "-.."
E = "."
F = "..-."
G = "--."
H = "...."
I = ".."
J = ".---"
K = "-.-"
L = ".-.."
M = "--"
N = "-."
O = "---"
P = ".--."
Q = "--.-"
R = ".-."
S = "..."
T = "-"
U = "..-"
V = "...-"
W = ".--"
X = "-..-"
Y = "-.--"
Z = "--.."


def decrypt():
    string = input("Enter morse code: ")
    global code
    code = string.split(" ")
    final_code = []
    for i in code:
        if i == A:
            final_code.append("A")
        elif i == B:
            final_code.append("B")
        elif i == C:
            final_code.append("C")
        elif i == D:
            final_code.append("D")
        elif i == E:
            final_code.append("E")
        elif i == F:
            final_code.append("F")
        elif i == G:
            final_code.append("G")
        elif i == H:
            final_code.append("H")
        elif i == I:
            final_code.append("I")
        elif i == J:
            final_code.append("J")
        elif i == K:
            final_code.append("K")
        elif i == L:
            final_code.append("L")
        elif i == M:
            final_code.append("M")
        elif i == N:
            final_code.append("N")
        elif i == O:
            final_code.append("O")
        elif i == P:
            final_code.append("P")
        elif i == Q:
            final_code.append("Q")
        elif i == R:
            final_code.append("R")
        elif i == S:
            final_code.append("S")
        elif i == T:
            final_code.append("T")
        elif i == U:
            final_code.append("U")
        elif i == V:
            final_code.append("V")
        elif i == W:
            final_code.append("W")
        elif i == X:
            final_code.append("X")
        elif i == Y:
            final_code.append("Y")
        elif i == Z:
            final_code.append("Z")
    for index in final_code:
        print(index, end = "")


def encrypt():
    string = input("Enter text: ")
    for char in string:
        if char.upper() == "A":
            code.append(A)
        elif char.upper() == "B":
            code.append(B)
        elif char.upper() == "C":
            code.append(C)
        elif char.upper() == "D":
            code.append(D)
        elif char.upper() == "E":
            code.append(E)
        elif char.upper() == "F":
            code.append(F)
        elif char.upper() == "G":
            code.append(G)
        elif char.upper() == "H":
            code.append(H)
        elif char.upper() == "I":
            code.append(I)
        elif char.upper() == "J":
            code.append(J)
        elif char.upper() == "K":
            code.append(K)
        elif char.upper() == "L":
            code.append(L)
        elif char.upper() == "M":
            code.append(M)
        elif char.upper() == "N":
            code.append(N)
        elif char.upper() == "O":
            code.append(O)
        elif char.upper() == "P":
            code.append(P)
        elif char.upper() == "Q":
            code.append(Q)
        elif char.upper() == "R":
            code.append(R)
        elif char.upper() == "S":
            code.append(S)
        elif char.upper() == "T":
            code.append(T)
        elif char.upper() == "U":
            code.append(U)
        elif char.upper() == "V":
            code.append(V)
        elif char.upper() == "W":
            code.append(W)
        elif char.upper() == "X":
            code.append(X)
        elif char.upper() == "Y":
            code.append(Y)
        elif char.upper() == "Z":
            code.append(Z)
    for i in code:
        print(i, end = " ")


option = input("Enter \"decrypt\" to convert morse code to text or enter \"encrypt\" to convert text to morse code: ")

if option == "decrypt":
    decrypt()
elif option == "encrypt":
    encrypt()
else:
    print("Error")

code.clear()

input("\nPress any key to quit.")
sys.exit()
