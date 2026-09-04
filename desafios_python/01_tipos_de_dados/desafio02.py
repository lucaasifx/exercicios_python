"""
beecrowd 1019 — Conversão de Tempo
Dificuldade: Fácil

Converta um total em segundos para o formato de relógio "H:M:S" utilizando divisão inteira e resto.
"""


def segundos_para_horario(segundos: int) -> str:
    pass


if __name__ == "__main__":
    casos = [
        ((556,), '0:9:16'),
        ((1,), '0:0:1'),
        ((140153,), '38:55:53')
    ]

    print("=" * 50)
    print("Iniciando testes para: segundos_para_horario")
    print("=" * 50)

    sucessos = 0
    for idx, (entrada, esperado) in enumerate(casos, 1):
        try:
            obtido = segundos_para_horario(*entrada)
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
