"""
LeetCode 1 — Two Sum
Dificuldade: Médio

Encontre os índices dos dois elementos cujo somatório atinge o valor alvo utilizando um dicionário para busca em tempo O(n).
"""

# depois implemento a solucao O(n)
def dois_soma(nums: list[int], alvo: int) -> tuple[int, int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == alvo:
                return (i, j)


if __name__ == "__main__":
    casos = [
        (([2, 7, 11, 15], 9), (0, 1)),
        (([3, 2, 4], 6), (1, 2)),
        (([3, 3], 6), (0, 1))
    ]

    print("=" * 50)
    print("Iniciando testes para: dois_soma")
    print("=" * 50)

    sucessos = 0
    for idx, (entrada, esperado) in enumerate(casos, 1):
        try:
            obtido = dois_soma(*entrada)
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
