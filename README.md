# Crypto2023
Projet sur la cryptographie mis en œuvre à la faculté d'informatique en 2023

## Résultats :

### 1.PARTIE DE CERTIFICAT : 

Certificat déchiffré :
Bob est bien celui qu'il pretend etre, et sa cle publique est (e,n)=(1217,2301598423) en decimal 
Clé publique de Bob : (e,n) = (1217,2301598423)
Clé privée de Bob : (d,n) = (597595937,2301598423)
Card(E) = 56139

### 2.PARTIE D'E.C.D.H : 

G(x,y) = (8,3372)
aG(11062,35063) = 1414G(11062,35063)
Le premier entier non nul k tel que kG = O : k = 56139
abG(x,y) = 47664G(4182,39566)

### 3.PARTIE DE AES, SHA256 ET RSA : 

Message clair de Bob : Rendez-vous le 1/1/2022 a 12h00 sur le parvis de la cathedrale de Strasbourg

Message de Bob altéré et chiffré comme Bob : 
51d474d8deb898ed1c7fa5a6dcfcab76faa73e78fdbab8650d5b1afe0a8b2c17094f53b6a7ac85395dbf22381463d3b4a09c9c59a768f303adeeaff783b97961fec2d45c551116464a5b3d60934c8274 
Le hash (SHA256) du message altéré clair est :
16560234, 14938888, 6330371, 557200, 15488796, 16460933, 14605818, 10097331, 15646299, 12041452, 9542912, 

11 nombres chiffré avec RSA(clé privé de Bob) :
1473726753, 1981501518, 1562046610, 2153560545, 2044747377, 2011544337, 220075384, 43698537, 963375031, 1355529144, 2063334637
