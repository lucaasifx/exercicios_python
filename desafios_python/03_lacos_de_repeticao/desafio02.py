"""
LeetCode 412 — Fizz Buzz
Dificuldade: Fácil

Gere uma lista de 1 a n substituindo múltiplos de 3 por "Fizz", de 5 por "Buzz" e de ambos por "FizzBuzz".
"""


def fizz_buzz(n: int) -> list[str]:
    pass


if __name__ == "__main__":
    casos = [
        ((3,), ['1', '2', 'Fizz']),
        ((5,), ['1', '2', 'Fizz', '4', 'Buzz']),
        ((15,), ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz'])
    ]

    print("=" * 50)
    print("Iniciando testes para: fizz_buzz")
    print("=" * 50)

    sucessos = 0
    for idx, (entrada, esperado) in enumerate(casos, 1):
        try:
            obtido = fizz_buzz(*entrada)
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
