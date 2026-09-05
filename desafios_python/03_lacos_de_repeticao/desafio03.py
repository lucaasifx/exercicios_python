"""
beecrowd 1165 — Número Primo
Dificuldade: Médio

Verifique se um inteiro n (> 1) é divisível unicamente por 1 e por ele mesmo, retornando o booleano correspondente.
"""
import math

def eh_primo(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True
            
                   
                   


if __name__ == "__main__":
    casos = [
        ((97,), True),
        ((4,), False),
        ((2,), True),
        ((51,), False)
    ]

    print("=" * 50)
    print("Iniciando testes para: eh_primo")
    print("=" * 50)

    sucessos = 0
    for idx, (entrada, esperado) in enumerate(casos, 1):
        try:
            obtido = eh_primo(*entrada)
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
