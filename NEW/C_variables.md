---
export_on_save:
  html: true
---


## Les variables

==**À savoir**==

- On peut désigner des résultats par des variables afin de les réutiliser plus tard. **Attention**, on ne met pas une ~~valeur dans une variable~~, c'est faux. ==On affecte un résultat à une variable==.

- On ne peut pas choisir n’importe quel nom pour une variable.
De manière synthétique, on a :

    - **La règle** : N’utiliser que les caractères : `a→z`, `A→Z`, `0→9` et `_` ; les accents sont tolérés pour un programme en français.
    - **Obligatoire** : Ne pas débuter par un chiffre.
    - **Conseil** : `choisir_un_nom_de_variable_lisible`, `NePaschoisirUnNomDeVariablePeuLisible`, `nepaschoisirunnomdevariableillisible`, `JE_SUIS_UNE_JOLIE_CONSTANTE`.
    - **Exemples** : `nb_triangles`, `x_0` sont valides et lisibles.
    - **Conseil** : on limitera les abréviations à 
        - `nb` pour « nombre »,
        - `id` pour « indice »,

### Les mots réservés de Python3

Il y a **35 mots réservés** (dont deux récents) qui ne peuvent pas être utilisés pour des variables.

> |           |           |           |           |         |
> |:----------|:----------|:----------|:----------|:--------|
> |`False`    |`class`    |`finally`  |`is`       |`return` |
> |`None`     |`continue` |`for`      |`lambda`   |`try`    |
> |`True`     |`def`      |`from`     |`nonlocal` |`while`  |
> |`and`      |`del`      |`global`   |`not`      |`with`   |
> |`as`       |`elif`     |`if`       |`or`       |`yield`  |
> |`assert`   |`else`     |`import`   |`pass`     |`async`        |
> |`break`    |`except`   |`in`       |`raise`    |`await`         |
>
> *Remarque* : Seuls `False`, `None` et `True` commencent ici avec une majuscule.

Nous avons déjà vu :

- `def` pour définir une fonction.
- `return` pour une valeur de retour de la fonction. Elle ~~retourne~~ **renvoie** une valeur.
- `False` et `True` : les booléens Faux et Vrai.
- `if`, `elif`, `else` : pour les structures conditionnelles.

Nous allons bientôt voir :
- `for`, `while` : pour créer des boucles.
- `and`, `or`, `not` : opérateurs sur les booléens : **et**, **ou**, **non**.
- `from` et `import` : pour importer **à partir** d'un module.
- `is` : test d'identité entre objets.
- `None` : pour une donnée 'sans valeur' ; zéro étant un entier possédant une valeur.
- `del` : pour détruire (*<b>del</b>ete*) une variable.
- `lambda` : pour définir une fonction anonyme.
- `pass` : une instruction qui ne fait rien.
- `break`, `continue` : pour les boucles plus complexes.
- `in` : pour un test d'appartenance.

Nous verrons plus tard certains mots réservés parmi ceux qui restent.

- `assert` : pour le débogage facile.
- `try`, `except`, `raise` : pour la gestion des erreurs.
- `with`, `as` : pour la lecture de module ou de fichier.

Pour les utilisateurs avancés :
- `class` : pour la programmation orientée objet (POO).
- `global`, `nonlocal` : pour modifier la portée d'une variable.
- `yield` : pour la construction d'itérateur.

