---
export_on_save:
  html: true
---


# Comparaisons : `<` `<=` `==` `!=` `<>` `>=` `>`

## ==À savoir==

Avec Python, on a les opérateurs de comparaison :

- `<` strictement inférieur à
- `<=` inférieur ou égal à
- `==` égal à
- `!=` différent de
- `<>` différent de *(variante)*
- `>=` supérieur ou égal à
- `>` strictement supérieur à

Ces opérateurs renvoient un **booléen** :
- `True`, pour Vrai
- `False`, pour Faux

### Exemples

1. une identité remarquable $(a+b)^2 = a^2 +2ab + b^2$ et
2. des nombres très grands ; trop grands pour une calculatrice.

```python
>>> (50 + 3)**2 == 50**2 + 2*50*3 + 3**2
True
>>> 2**10000 <= 10**3000
False
>>> 2**10000 <= 10**3100
True
```

## Pour comprendre l'exemple

L'avant dernier résultat n'est pas une surprise, sachant que $2^{10} = 1024 > 1000 = 10^3$.

$$2^{10000} = 2^{10×1000} = {2^{10}}^{1000} > {10^3}^1000 = 10^{3000}$$



---

:arrow_backward: [Retour au sommaire](python-maths-1.html)

---

:arrow_forward: Activité : [Découverte de la dichotomie](A_Dichotomie.html)

