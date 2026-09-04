"""
beecrowd 1165 — Número Primo
Dificuldade: Médio

Verifique se um inteiro n (> 1) é divisível unicamente por 1 e por ele mesmo, retornando o booleano correspondente.
"""


def eh_primo(n: int) -> bool:
    primos_fund = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

    for pr in primos_fund:
        if n%pr == 0:
            return n == pr
    
    if n > primos_fund[-1]:
        aux = primos_fund[-1] + 2
        ref = n**(1/2)
        while(aux < ref):
            if n%aux == 0:
                return n == aux
            else:
                aux += 2

    return True

if __name__ == "__main__":
    casos = [
        ((97,), True),
        ((4,), False),
        ((2,), True),
        ((51,), False)
    ]

    print("=" * 50)
    print("Iniciando testes para: eh_primo")
    print("=" * 50)

    sucessos = 0
    for idx, (entrada, esperado) in enumerate(casos, 1):
        try:
            obtido = eh_primo(*entrada)
            if obtido == esperado:
                print(f"[OK] Teste {idx} passou!")
                sucessos += 1
            else:
                print(f"[FALHA] Teste {idx} falhou!")
                print(f"  Entrada:  {entrada}")
                print(f"  Esperado: {esperado!r}")
                print(f"  Obtido:   {obtido!r}")
        except Exception as e:
            print(f"[ERRO] Teste {idx} gerou excecao: {type(e).__name__}: {e}")
            print(f"  Entrada:  {entrada}")

    print("-" * 50)
    print(f"Resultado: {sucessos}/{len(casos)} testes passaram.")
    print("=" * 50)
