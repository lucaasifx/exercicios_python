"""
beecrowd 1044 — Múltiplos
Dificuldade: Muito Fácil

Avalie se dois números inteiros são múltiplos entre si (ou seja, se a divisão de um pelo outro deixa resto 0).
"""


def sao_multiplos(a: int, b: int) -> bool:
    pass


if __name__ == "__main__":
    casos = [
        ((6, 24), True),
        ((6, 25), False),
        ((24, 6), True)
    ]

    print("=" * 50)
    print("Iniciando testes para: sao_multiplos")
    print("=" * 50)

    sucessos = 0
    for idx, (entrada, esperado) in enumerate(casos, 1):
        try:
            obtido = sao_multiplos(*entrada)
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
