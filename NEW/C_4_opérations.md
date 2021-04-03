---
export_on_save:
  html: true
---


# Les opérations simples sur les entiers

## ==À savoir==

Comme avec la plupart des langages de programmation :

- `+` : addition
- `-` : soustraction
- `*` : multiplication
- Les priorités usuelles sont respectées.
- Les multiplications doivent être **explicites**.
    - On ne peut pas écrire `3n + 1` pour $3n + 1$,
    - mais `3*n + 1`.
- On peut mettre des parenthèses.

De plus avec Python,

- `**` désigne la puissance.
- Le calcul sur les entiers est en précision arbitraire, la seule limite étant la mémoire de l'ordinateur. *On peut **travailler** avec des entiers qui ont des millions de chiffres, mais **pas afficher** ceux qui sont trop grands.*


### Exemples

```python
>>> 43 * 47
2021
>>> (45 - 2) * (45 + 2)
2021
>>> 23**2 + 197**2
39338
>>> 97**2 + 173**2
39338
>>> 107**2 + 167**2
39338
>>> 113**2 + 163**2
39338
>>> 180 * (2**127 - 1)**2 + 1
5210644015679228794060694325390955853335898483908056458352183851018372555735221
```

Le dernier exemple est célèbre pour avoir été en 1951 le record du plus grand nombre premier connu.


## Et les divisions ?

On verra cela bientôt ; patience.

## Pour en savoir plus

Les entiers sont stockés en mémoire sous forme binaire ; les calculs sont plus pratiques. Pour l'affichage d'un entier, il y a une étape de conversion vers le système décimal, et ensuite l'affichage. L'affichage est très rapide, mais pas la conversion, ce qui explique qu'on peut travailler avec des nombres gigantesques, mais sans pouvoir les afficher.



---

:arrow_backward: [Retour au sommaire](python-maths-1.html)

---

:arrow_forward: Activité [Découverte des nombres de Mersenne](1_Mersenne.html)

