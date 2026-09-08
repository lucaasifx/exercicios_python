"""
beecrowd 1067 — Números Ímpares
Dificuldade: Muito Fácil

Retorne uma lista contendo todos os números inteiros ímpares no intervalo fechado de 1 até n.
"""


# nessa aqui vou tentar treinar list comprehension alem da resposta
def obter_impares(n: int) -> list[int]:
    # resposta trivial
    # ans = []
    # for i in range(n + 1):
    #     if i % 2 != 0:
    #         ans.append(i)
    # return ans
    return [i for i in range(n + 1) if i % 2 != 0 ]


if __name__ == "__main__":
    casos = [
        ((8,), [1, 3, 5, 7]),
        ((1,), [1]),
        ((11,), [1, 3, 5, 7, 9, 11])
    ]

    print("=" * 50)
    print("Iniciando testes para: obter_impares")
    print("=" * 50)

    sucessos = 0
    for idx, (entrada, esperado) in enumerate(casos, 1):
        try:
            obtido = obter_impares(*entrada)
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
