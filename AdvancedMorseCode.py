import sys

global code
code = []

class Morse:
    def __init__(self, morse, text):
        self.morse = morse
        self.text = text

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

string = str(input("Enter morse code or text to be translated into text or morse code respectively: "))

if string.replace(" ", "").isalpha():
    m2 = Morse("", string)
    for char in string:
        if char.upper() == "A":
            m2.morse += A + " "
        elif char.upper() == "B":
            m2.morse += B + " "
        elif char.upper() == "C":
            m2.morse += C + " "
        elif char.upper() == "D":
            m2.morse += D + " "
        elif char.upper() == "E":
            m2.morse += E + " "
        elif char.upper() == "F":
            m2.morse += F + " "
        elif char.upper() == "G":
            m2.morse += G + " "
        elif char.upper() == "H":
            m2.morse += H + " "
        elif char.upper() == "I":
            m2.morse += I + " "
        elif char.upper() == "J":
            m2.morse += J + " "
        elif char.upper() == "K":
            m2.morse += K + " "
        elif char.upper() == "L":
            m2.morse += L + " "
        elif char.upper() == "M":
            m2.morse += M + " "
        elif char.upper() == "N":
            m2.morse += N + " "
        elif char.upper() == "O":
            m2.morse += O + " "
        elif char.upper() == "P":
            m2.morse += P + " "
        elif char.upper() == "Q":
            m2.morse += Q + " "
        elif char.upper() == "R":
            m2.morse += R + " "
        elif char.upper() == "S":
            m2.morse += S + " "
        elif char.upper() == "T":
            m2.morse += T + " "
        elif char.upper() == "U":
            m2.morse += U + " "
        elif char.upper() == "V":
            m2.morse += V + " "
        elif char.upper() == "W":
            m2.morse += W + " "
        elif char.upper() == "X":
            m2.morse += X + " "
        elif char.upper() == "Y":
            m2.morse += Y + " "
        elif char.upper() == "Z":
            m2.morse += Z + " "
    print(m2.morse)
else:
    for char in string:
        if char.isalpha():
            print("Error")
            sys.exit()
    m1 = Morse(string, "")
    code = string.split(" ")
    for i in code:
        if i == A:
            m1.text += "A"
        elif i == B:
            m1.text += "B"
        elif i == C:
            m1.text += "C"
        elif i == D:
            m1.text += "D"
        elif i == E:
            m1.text += "E"
        elif i == F:
            m1.text += "F"
        elif i == G:
            m1.text += "G"
        elif i == H:
            m1.text += "H"
        elif i == I:
            m1.text += "I"
        elif i == J:
            m1.text += "J"
        elif i == K:
            m1.text += "K"
        elif i == L:
            m1.text += "L"
        elif i == M:
            m1.text += "M"
        elif i == N:
            m1.text += "N"
        elif i == O:
            m1.text += "O"
        elif i == P:
            m1.text += "P"
        elif i == Q:
            m1.text += "Q"
        elif i == R:
            m1.text += "R"
        elif i == S:
            m1.text += "S"
        elif i == T:
            m1.text += "T"
        elif i == U:
            m1.text += "U"
        elif i == V:
            m1.text += "V"
        elif i == W:
            m1.text += "W"
        elif i == X:
            m1.text += "X"
        elif i == Y:
            m1.text += "Y"
        elif i == Z:
            m1.text += "Z"
    print(m1.text)
