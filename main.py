"""
Auteur : Zhurina Iuliia
№ etudiant : 22004388
"""
import sys
import math
#import binascii
import hashlib
from Crypto.Cipher import AES
from termcolor import colored, cprint


print(colored('\n 1.PARTIE DE CERTIFICAT :', attrs=["bold"]), '\n\n')

"""
pour déchiffrer le certificat de Bob, on utiliser les fonctions suivantes:
1. si le nb est premier
2. euclide_etendu (a= q*b+r)
3. phi(n)
4. exponontiation rapide (a^e mod n = res)
"""

#nombre est premier ou pas
def isprem(n):
	if n == 1 or n == 2:
		return True
	if n%2 == 0:
		return False
	r = n**0.5
	if r == int(r):
		return False
	for x in range(3, int(r), 2):
		if n % x == 0:
			return False	
	return True
  
#algorithme d'euclide etendu
def euclide_etendu (a,b):
    x = 1 ; x1 = 0
    y = 0 ; y1 = 1
    while b != 0 :
        q = a // b
        a,b = b, a%b
        x1, x = x-q*x1, x1
        y1, y = y-q*y1, y1
    return (a,x,y)
  
#inverse de a modulo n
def inverse (a,n):
    c,u,v = euclide_etendu(a,n)
    if c != 1: 
        return 0
    else :
        return u % n

#phi(n)
def phi (n):
    for i in range (2,n):
        if n % i == 0:
            if isprem(i) and isprem(n//i):
                return (i-1)*(n//i -1)
    return n-1

#exponontiation rapide
def expo_rap(a,e,n):
    res=1
    while e!=0:
        if e%2==1:
            res*=a
            res = res % n
        a*=a
        e//=2
    return res

#Clé publique de l'autorité de certification : 
e_AC = 1873
n_AC = 544798091

#Certificat de Bob (en décimal, chaque nombre est le chiffrement de 3 octets correspondant à 3 caractères en ASCII) :
C_Bob = [216255373, 41441753, 113546610, 222852952, 19374672, 48437626, 205547068, 475817152, 402693798, 486452830, 28646373, 485751517, 481985257, 33780802, 416515979, 428708414, 270328343, 52649231, 414749801, 41441753, 293596547, 424115, 469394829, 458830119, 482300780, 183977217, 446816519, 362845278, 374712679, 101429161, 348514522, 161792227]

#dechiffrer le certificat
DC_Bob = []
for x in C_Bob:
    DC_Bob.append(hex(expo_rap(x,e_AC,n_AC)))
t = 2
chaine = ''
for i in range (len(DC_Bob)):
    m = str(DC_Bob[i])[2:]
    chaine += chr(int(m[:t],16)) + chr(int(m[t:t*2],16)) + chr(int(m[t*2:t*4],16))
print(colored('Certificat déchiffré :', attrs=["bold"]))
print(chaine,'\n')

#Clé publique de Bob :
e_B = 1217
n_B = 2301598423
print(colored('Clé publique de Bob : (',attrs=["bold"]), colored('e', "blue"),',',colored('n', "magenta"),') = (', colored(e_B, "blue"),',',colored(n_B, "magenta"),')\n', sep='')


#Clé privée de Bod :
#d = 597595937
d_B = inverse(1217,phi(2301598423))
print(colored('Clé privée de Bob : (', attrs=["bold"]), colored('d', "cyan"),',',colored('n', "magenta"),') = (', colored(d_B, "cyan"),',',colored(n_B, "magenta"),')\n', sep='')

"""
pour trouver ordre de la courbe elliptique (Card(E)) https://andrea.corbellini.name/ecc/interactive/modk-add.html
il faut mettre mes valeurs
a = 5, b = 5, p = 56009
The curve has 56009 points 
"""
print('Card(E) = ', colored(56139, "red"),'\n',sep='')


print(colored('\n 2.PARTIE D\'E.C.D.H :', attrs=["bold"]), '\n\n')

#G(x,y)
xg = 8

#P
p = 56009

"""
a, b = 5
x = 8
y^2 = x^3 + a*x + b
y^2 = 8^3 +8*5+5
y^2 = 557
"""
y2 = 557

#reference : https://gist.github.com/cicorias/b1ebcc847205de3c5ad5254f7a1b85e0
#modular_sqrt calcule y de G en utilisant y^2 et p
def modular_sqrt(a, p):
    def legendre_symbol(a, p):
       
        ls = pow(a, (p - 1) // 2, p)
        return -1 if ls == p - 1 else ls

    if legendre_symbol(a, p) != 1:
        return 0
    elif a == 0:
        return 0
    elif p == 2:
        return p
    elif p % 4 == 3:
        return pow(a, (p + 1) // 4, p)

    s = p - 1
    e = 0
    while s % 2 == 0:
        s //= 2
        e += 1

    n = 2
    while legendre_symbol(n, p) != -1:
        n += 1

    x = pow(a, (s + 1) // 2, p)
    b = pow(a, s, p)
    g = pow(n, s, p)
    r = e

    while True:
        t = b
        m = 0
        for m in range(r):
            if t == 1:
                break
            t = pow(t, 2, p)

        if m == 0:
            return x

        gs = pow(g, 2 ** (r - m - 1), p)
        g = (gs * gs) % p
        x = (x * gs) % p
        b = (b * g) % p
        r = m

yg = modular_sqrt(y2, p)
#y de G = 3372
print('G(x,',colored('y', "red"),') = (%d,'% xg,colored(yg, "red"),')\n',sep='')

#aG de Bob
xg_a = 11062
yg_a = 35063

"""
#pour trouver a de aG on peut utiliser ce programme : https://replit.com/@zhurinajuli/CRYPTO-NP#main.py ou file "crypto nP.py"
donc :
1414G =(11062, ...)
a demandé = 1414
"""
a = 1414 
print(colored('a', "red"),'G(11062,35063) = ', colored(a, "red"),'G(%d,%d)'%(xg_a, yg_a),'\n', sep='')

#bG d'Alice
xg_b = 48094
yg_b = 4810

#pour trouver b, j'ai cherché nP avec x = 48094 en utilisent la programme CRYPTO NP
b=54267

#dernier point nP = (8, 3372) = P avec n = 56138
#k = n+1
k = 56139
print('Le premier entier non nul k tel que ',colored('k', 'yellow'),'G = O : ', colored('k', 'yellow'),' = ',  colored(k, 'yellow'),'\n', sep = '')

#on doit trouver ab en utilisant k
#ab = a*b mod p
ab = (a*b)%k
#ab = 47664
#47664G = (4182,39566), ou x = 4182
xg_ab = 4182
yg_ab = 39566
print(colored('ab', 'green'),'G(',colored('x', 'red'),',y) = ',colored(ab, 'green'),'G(',colored(xg_ab, 'red'),',%d)'% yg_ab ,'\n', sep='')


print(colored('\n 3.PARTIE DE AES, SHA256 ET RSA :', attrs=["bold"]), '\n\n')

#on dechiffre message de Bob avec AES mode opératoire CBC
message = bytes.fromhex("51d474d8deb898ed1c7fa5a6dcfcab76cf99bb8e51a58a31d92955466dd280fd51cc4d9cf8f325f00c1abb8d451a566c5634c81c737dd4f9aaad50013c3029ca10f4a31209bfddcc7f04ffa4956612ff")
#x = 4182 en hex = 00000000000000000000000000001056
cle = bytes.fromhex("00000000000000000000000000001056")
iv = bytes.fromhex("0"*32)

def dechiffrer(data):
  aes = AES.new(cle, AES.MODE_CBC, iv)
  dechif = aes.decrypt(data)
  return dechif
print(colored('Message clair de Bob : ', attrs=["bold"]),colored(dechiffrer(message).decode(), 'cyan'),'\n', sep='')
#Rendez-vous le 1/1/2022 a 12h00 sur le parvis de la cathedrale de Strasbourg

#message clair de Bob altéré : 
message_a = b'Rendez-vous le 1/1/2022 a 11h00 sur le parvis de la cathedrale de Strasbourg'

#on change l'heure et chiffre nouvelle message avec AES mode opératoire CBC
message_c = b'Rendez-vous le 1/1/2022 a 11h00 sur le parvis de la cathedrale de Strasbourg\x00\x00\x00\x00'

def chiffrer(data):
  aes = AES.new(cle, AES.MODE_CBC, iv)
  chif = aes.encrypt(data)
# return binascii.hexlify(chif)
  return chif.hex()
print(colored('Message de Bob altéré et chiffré comme Bob : ', attrs=["bold"]))
print(chiffrer(message_c), '\n')

#SHA256RSA sigianture : 
# Etudiant Efe ERKEN a aidé avec le code 
def decoupe_hash(hash_digest):
    binary_digest = ""
    for i in hash_digest:
        hash_digest_binary_suffix = str(bin(i)[2:])
        hash_digest_binary_prefix = "0" * (8 - len(hash_digest_binary_suffix))
        binary_digest += hash_digest_binary_prefix + hash_digest_binary_suffix
    l = []
    for i in range(0, len(binary_digest) - (len(binary_digest) % 24), 24):
        l += [int(binary_digest[i:i+24], 2)]
    l += [int(binary_digest[(len(binary_digest) // 24) * 24:] + ("0" * (24 - (len(binary_digest) % 24))), 2)]
    return l

def chiffre_nombres_RSA(liste_nbs, d_B, n_B):
    for i, val in enumerate(liste_nbs):
        liste_nbs[i] = pow(val, d_B, n_B)
    return liste_nbs

hash_decoupe = decoupe_hash((hashlib.sha256(message_a)).digest())
print(colored('Le hash (SHA256) du message altéré clair est :', attrs=["bold"]))
print(*hash_decoupe,'\n', sep = ", ")

#pour RSA on doit utiliser hash découpé et clé privée de Bob
nb_chif = chiffre_nombres_RSA(hash_decoupe, d_B, n_B)
print(colored('11 nombres chiffré avec RSA(clé privé de Bob) :', attrs=["bold"]))
print(*nb_chif, sep = ", ")
