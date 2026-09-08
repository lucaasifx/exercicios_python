"""
Conversor Seguro de Inteiro
Dificuldade: Fácil

Tente converter uma string para inteiro. Intercepte ValueError caso a conversão falhe e retorne o sentinela -1.
"""


def parse_inteiro(texto: str) -> int:
    pass


if __name__ == "__main__":
    casos = [
        (('42',), 42),
        (('abc',), -1),
        (('  100 \n',), 100),
        (('12.34',), -1)
    ]

    print("=" * 50)
    print("Iniciando testes para: parse_inteiro")
    print("=" * 50)

    sucessos = 0
    for idx, (entrada, esperado) in enumerate(casos, 1):
        try:
            obtido = parse_inteiro(*entrada)
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
