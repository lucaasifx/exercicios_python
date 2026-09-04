"""
beecrowd 1003 — Soma Simples
Dificuldade: Muito Fácil

Receba dois inteiros, calcule a soma algébrica entre eles e retorne o valor resultante.
"""


def soma(a: int, b: int) -> int:
    return a + b


if __name__ == "__main__":
    casos = [
        ((30, 10), 40),
        ((-30, 10), -20),
        ((0, 0), 0)
    ]

    print("=" * 50)
    print("Iniciando testes para: soma")
    print("=" * 50)

    sucessos = 0
    for idx, (entrada, esperado) in enumerate(casos, 1):
        try:
            obtido = soma(*entrada)
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
