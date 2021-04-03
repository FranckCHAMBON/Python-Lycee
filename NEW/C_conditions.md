---
export_on_save:
  html: true
---

### Structures conditionnelles

Avec Python, on a les constructions suivantes possibles :

```python
"""
`action()` n'est exécutée que si condition est évalué à `True`
"""
if condition:
    action()
```

```python
"""
`action()` n'est exécutée que si condition est évalué à `True`
sinon, c'est `autre_action()` qui est exécutée.
"""
if condition:
    action()
else:
    autre_action()
```

```python
"""
`elif` est la contraction de `else if`, pour « sinon si ».
Il peut y avoir autant de blocs `elif` que l'on souhaite.
On peut terminer, par un bloc `else` pour les cas non traités.
"""
if condition_1:
    action_1()
elif condition_2:
    action_2()
elif condition_3:
    action_3()
else:
    action_autres_cas()
```

Exemple

La suite de Syracuse d'un entier $N>0$ est définie par récurrence, de la manière suivante :
- $u_0 = N$
- pour tout entier naturel $n$ : $u_{n+1} = \begin{cases}\dfrac{u_n}{2}&\text{si } u_n \text{ est pair,}\\3×u_n + 1&\text{si } u_n \text{ est impair.}\end{cases}$

On peut alors définir la fonction `terme_suivant`

```python
def terme_suivant(u_n):
    """ Renvoie le terme suivant `u_n` dans une suite de Syracuse.
    """
    if u_n % 2 == 0:
        return u_n // 2
    else:
        return 3 * u_n + 1
```

