"""Module de vérification de l'exercice

Usage

- `help(juge)` pour afficher cette aide
- `dir(juge)` pour afficher les tests disponibles

"""

def test_factorielle():
    """Teste votre fonction `factorielle`
    
    - pour un entier donné en entrée inférieur à 100

    """
    fact_mem = [1]
    for n in range(1, 100):
        fact_mem.append(fact_mem[-1] * n)
    def ref(i):
        return fact_mem[i]

    for i in range(100):
        assert factorielle(i) == ref(i), f"Échec avec {i=}"

def test_fibonacci():
    """Teste votre fonction `fibonacci`
    
    - pour un entier donné en entrée inférieur à 100

    """
    fib_mem = [0, 1]
    for _ in range(100):
        fib_mem.append(sum(fib_mem[-2:]))
    def ref(i):
        return fib_mem[i]

    for i in range(100):
        assert fibonacci(i) == ref(i), f"Échec avec {i=}"

def test_tout():
    test_factorielle()
    test_fibonacci()
