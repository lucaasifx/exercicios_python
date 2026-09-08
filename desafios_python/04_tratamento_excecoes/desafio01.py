"""
Divisão com Captura de Zero
Dificuldade: Muito Fácil

Execute a divisão de a por b. Trate explicitamente ZeroDivisionError para retornar None em divisões inválidas.
"""


def dividir(a: float, b: float) -> float | None:
    pass


if __name__ == "__main__":
    casos = [
        ((10.0, 2.0), 5.0),
        ((10.0, 0.0), None),
        ((0.0, 5.0), 0.0)
    ]

    print("=" * 50)
    print("Iniciando testes para: dividir")
    print("=" * 50)

    sucessos = 0
    for idx, (entrada, esperado) in enumerate(casos, 1):
        try:
            obtido = dividir(*entrada)
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
