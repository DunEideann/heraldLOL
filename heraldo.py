# Un simple script que use para saber
# las estadisticas de importancia de Heraldo
# en el juego League of Legends

def heraldo():
    niveles=[6,7,8,9,10,11,12]
    hp = []
    dmg = []
    eye = []
    for i,nivel in enumerate(niveles):
        hp.append(7125 + ((nivel-6)*((7125)/6)))
        dmg.append(855 + ((nivel-6)*((1710-855)/6)))
        eye.append((7125 + ((nivel-6)*((7125)/6)))*0.15)
        
    return niveles, hp, dmg, eye

a, b, c, d = heraldo()
for i in range(len(a)):
    print(f"Nivel:{a[i]}, HP:{b[i]}, Daño a heraldo:{c[i]} y HP a la cual deja de abrir el ojo:{d[i]}.")

