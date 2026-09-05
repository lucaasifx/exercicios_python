"""
LeetCode 217 — Contains Duplicate
Dificuldade: Muito Fácil

Verifique a presença de elementos repetidos em uma lista de inteiros utilizando um conjunto (set).
"""


def contem_duplicata(nums: list[int]) -> bool:
    conj = set(nums)
    return len(conj) < len(nums)



if __name__ == "__main__":
    casos = [
        (([1, 2, 3, 1],), True),
        (([1, 2, 3, 4],), False),
        (([],), False),
        (([1, 1, 1, 3, 3, 4, 3, 2, 4, 2],), True)
    ]

    print("=" * 50)
    print("Iniciando testes para: contem_duplicata")
    print("=" * 50)

    sucessos = 0
    for idx, (entrada, esperado) in enumerate(casos, 1):
        try:
            obtido = contem_duplicata(*entrada)
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
