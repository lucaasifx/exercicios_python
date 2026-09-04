"""
beecrowd 1041 — Coordenadas de um Ponto
Dificuldade: Médio

Receba coordenadas de ponto flutuante (x, y) e determine se o ponto está na "Origem",
sobre os eixos ("Eixo X", "Eixo Y") ou nos quadrantes ("Q1", "Q2", "Q3", "Q4").
"""


def localizar_ponto(x: float, y: float) -> str:
    pass


if __name__ == "__main__":
    casos = [
        ((0.0, 0.0), 'Origem'),
        ((0.0, 5.0), 'Eixo Y'),
        ((3.0, 0.0), 'Eixo X'),
        ((0.1, 0.1), 'Q1'),
        ((-0.1, 0.1), 'Q2'),
        ((-0.1, -0.1), 'Q3'),
        ((0.1, -0.1), 'Q4')
    ]

    print("=" * 50)
    print("Iniciando testes para: localizar_ponto")
    print("=" * 50)

    sucessos = 0
    for idx, (entrada, esperado) in enumerate(casos, 1):
        try:
            obtido = localizar_ponto(*entrada)
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
