"""
Sanitizador de Parâmetro Numérico
Dificuldade: Fácil

Enunciado:
Receba uma string contendo um valor numérico que pode vir cercado de espaços em branco
ou quebras de linha (ex: "  42 \n"). Limpe os caracteres vazios e retorne o valor como inteiro.
"""


def sanitizar_parametro(param: str) -> int:
    return int(param.strip())


if __name__ == "__main__":
    casos = [
        (("  42 \n",), 42),
        (("120",), 120),
        (("\t 999 \r\n",), 999),
        (("-15  ",), -15)
    ]

    print("=" * 50)
    print("Iniciando testes para: sanitizar_parametro")
    print("=" * 50)

    sucessos = 0
    for idx, (entrada, esperado) in enumerate(casos, 1):
        try:
            obtido = sanitizar_parametro(*entrada)
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
