"""
beecrowd 1281 — Ida à Feira
Dificuldade: Fácil

Dado um dicionário de preços e uma lista de compras [(produto, quantidade)], calcule o custo financeiro total.
"""


def calcular_feira(tabela: dict[str, float], compras: list[tuple[str, int]]) -> float:
    custo_total = 0.0

    for prod, qtd in compras:
        custo_total += tabela[prod]*qtd

    return custo_total


if __name__ == "__main__":
    casos = [
        (({'banana': 2.5, 'maca': 4.0, 'laranja': 1.5}, [('banana', 2), ('maca', 1)]), 9.0),
        (({'laranja': 1.5}, [('laranja', 4)]), 6.0)
    ]

    print("=" * 50)
    print("Iniciando testes para: calcular_feira")
    print("=" * 50)

    sucessos = 0
    for idx, (entrada, esperado) in enumerate(casos, 1):
        try:
            obtido = calcular_feira(*entrada)
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
