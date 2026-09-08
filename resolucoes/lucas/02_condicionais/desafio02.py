"""
HackerRank — Ano Bissexto
Dificuldade: Fácil

Determine se um ano é bissexto: divisível por 4, exceto múltiplos de 100 (a menos que sejam também múltiplos de 400).
"""


def eh_bissexto(ano: int) -> bool:
    return ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)


if __name__ == "__main__":
    casos = [
        ((2000,), True),
        ((1900,), False),
        ((2024,), True),
        ((2023,), False)
    ]

    print("=" * 50)
    print("Iniciando testes para: eh_bissexto")
    print("=" * 50)

    sucessos = 0
    for idx, (entrada, esperado) in enumerate(casos, 1):
        try:
            obtido = eh_bissexto(*entrada)
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
