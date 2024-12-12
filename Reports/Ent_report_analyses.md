# Analysis of ESP32-C6 Random Number Generator (Ent)


## 1. Fréquences des valeurs :

Globalement, les valeurs semblent assez bien réparties entre les différentes valeurs possibles, 
ce qui est un bon signe pour un générateur de nombres aléatoires, mais il y a une légère dominance de 
certaines valeurs (notamment 1 et 0).


## 2. Entropie :
Entropie = 3.555 bits par byte.

3.555 bits par byte est assez faible par rapport à l'entropie maximale, indiquant que les données ne sont pas 
parfaitement aléatoires et présentent des schémas ou des motifs répétitifs.

## 3. Compression optimale :

La compression est généralement plus efficace lorsque les données présentent des motifs répétitifs ou
des relations de dépendance. Cela correspond à l'entropie relativement faible.

## 4. Test du chi carré :
Chi-square = 43,310,009.41.
La probabilité qu'un échantillon aléatoire dépasse cette valeur est inférieure à 0.01%.
Le fait que cette valeur dépasse 99.99% des valeurs aléatoires suggère que les données ne sont pas parfaitement aléatoires,
ce qui est cohérent avec l'entropie.

## 5. Monte Carlo pour Pi :
Le test de Monte Carlo pour Pi consiste à utiliser un échantillon aléatoire pour estimer la valeur de Pi. 
Une valeur de 4.0 (et une erreur de 27.32%) est loin de la valeur correcte de 3.14159....
Cela indique que les valeurs RNG ne sont pas complètement aléatoires.

## 6. Coefficient de corrélation serial :
Un coefficient de -0.007 indique que les valeurs sont très légèrement corrélées, 
mais cette corrélation est extrêmement faible.

## Conclusion

Le générateur de nombres aléatoires (RNG) utilisé semble assez bon, mais il montre certains défauts, 
notamment une entropie relativement faible (indiquant une structure ou des motifs répétitifs) et une moyenne
des valeurs plus basse que prévu.
