"""
Formatador de Moeda para API
Dificuldade: Médio

Enunciado:
Receba um valor em ponto flutuante representando uma quantia financeira e retorne
uma string formatada no padrão de moeda com prefixo 'R$ ' e exatamente duas casas decimais.
"""


def formatar_moeda(valor: float) -> str:
    return f'R$ {valor:.2f}'


if __name__ == "__main__":
    casos = [
        ((1250.5,), "R$ 1250.50"),
        ((0.0,), "R$ 0.00"),
        ((99.999,), "R$ 100.00"),
        ((7.1,), "R$ 7.10")
    ]

    print("=" * 50)
    print("Iniciando testes para: formatar_moeda")
    print("=" * 50)

    sucessos = 0
    for idx, (entrada, esperado) in enumerate(casos, 1):
        try:
            obtido = formatar_moeda(*entrada)
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
