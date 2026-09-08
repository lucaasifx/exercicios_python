"""
Somador de Lista Heterogênea
Dificuldade: Médio

Percorra uma lista mista somando valores conversíveis para float. Capture ValueError e TypeError para ignorar itens não numéricos.
"""


def somar_validos(itens: list) -> float:
    sum = 0
    for item in itens:
        try:
            sum += float(item)
        except ValueError:
            continue
        except TypeError:
            continue
    return sum



if __name__ == "__main__":
    casos = [
        ((('10.5', 'erro', 5, None, '2.5'),), 18.0),
        (([],), 0.0),
        ((('a', None, {}),), 0.0),
        (([1, 2, 3],), 6.0)
    ]

    print("=" * 50)
    print("Iniciando testes para: somar_validos")
    print("=" * 50)

    sucessos = 0
    for idx, (entrada, esperado) in enumerate(casos, 1):
        try:
            obtido = somar_validos(*entrada)
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
