# Operadores --------------------------------------
# Aritmeticos -------------------------------------
A = 1+3 # retorna la suma de 1+3=4
B = 1-3 # retorna la resta de 1-3=-2
C = 2*3 # retorna la multiplicacion de 2*3=6
D = 10/3 # retorna la division de 10/3=3.333
E = 10%3 # retorna el modulo (excedente) de 10%3=1
F = 2**3 # Retorna la potencia de 2^3 =8 
G = 10//3 # retorna la division entera de 10/3=3

# Binarios ----------------------------------------
A = 1&0 # &=AND pone el bit en 1 si ambos son 1
B = 1|0 # |=OR pone el bit en 1 si uno de los dos es 1
C = 1^0 # ^=XOR pone el bit en 1 solo si uno de los dos es 1
D = ~1 # ~=NOT invierte todos los bits
E = 1<<0 # Empuja los bist por la derecha y deja caer los de la izquierda
F = 1>>0 # Empuja los bits por la izquierda y deja caer los de la de derecha
A &= 3 #
A |= 3 #
A ^= 3 #
A >>= 3 #
A <<= 3 #

# Comparacion--------------------------------------
A = 2==3 # 2==3=False 2 no es igual a 3
B = 2!=3 # 2!=3=True 2 es diferente de 3
C = 2>3 # 2>3=False 2 no es a que 3
D = 2<2 # 2<3=True 2 es menor a 3
E = 2>=3 # 2>3=False 2 no es mayor o igual a 3
F = 2<=2 # 2<3=True 2 es menor a igual a 3

# Logicos------------------------------------------
A = True
B = False
C = A and B # A and B = False A y B no son True
D = A or B # A or B = True A o B es True
E = not A # not A = False el apuesto de True es False

# Asignacion---------------------------------------
A = 2 # Se asigna a A el valor de 85
A += 2 # A=4 se incrementa el valor de A en 2
A -= 2 # A=2 se decrementa el valor de A en 2
A *= 3 # A=6 se multiplica el valor de A por 3
A /= 3 # A=2 se divide el valor de A por 3
A %= 3 # A=2 se saca el modulo de A%2
A**= 3 # A=8 se saca la potencia A**3
A//= 3 # A=2 se saca la division entera A//3

# Especiales---------------------------------------
A = 2 is 3 # 2 is 3 = False 2 no es 3
B = 2 is not 3 # 2 is not 3 = True 2 no es 3
C = 2 in [1,2] # 2 in [1,2] = True 2 esta en [1,2]
C = 2 not in [1,2] # 2 not in [1,2] = False 2 esta en [1,2]