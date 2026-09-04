"""
LeetCode 67 — Add Binary
Dificuldade: Médio

Receba duas strings que representam números binários e retorne a sua soma também formatada como string binária.
"""


def somar_binarios(a: str, b: str) -> str:
    pass


if __name__ == "__main__":
    casos = [
        (('11', '1'), '100'),
        (('1010', '1011'), '10101'),
        (('0', '0'), '0')
    ]

    print("=" * 50)
    print("Iniciando testes para: somar_binarios")
    print("=" * 50)

    sucessos = 0
    for idx, (entrada, esperado) in enumerate(casos, 1):
        try:
            obtido = somar_binarios(*entrada)
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
