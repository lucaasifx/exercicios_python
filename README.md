# 🐍 Nivelamento Python — Trilha Backend Django

Guia oficial de nivelamento prático em Python para a equipe de desenvolvimento. Este material foi estruturado para desenvolvedores que já dominam lógica de programação em outras linguagens e precisam se habituar com a sintaxe, tipagem e estruturas fundamentais do ecossistema Python antes de iniciarmos a API em Django.

---

## 🎯 Objetivo do Treinamento

Resolver os **15 exercícios práticos** distribuídos nos 5 módulos essenciais da linguagem. Cada desafio deve ser implementado no formato de função pura e validado através dos testes locais automatizados contidos em cada arquivo.

---

## 📁 Estrutura de Diretórios do Projeto

```text
.
├── 01_tipos_de_dados/
│   ├── desafio01.py
│   ├── desafio02.py
│   └── desafio03.py
│
├── 02_condicionais/
│   ├── desafio01.py
│   ├── desafio02.py
│   └── desafio03.py
│
├── 03_lacos_de_repeticao/
│   ├── desafio01.py
│   ├── desafio02.py
│   └── desafio03.py
│
├── 04_tratamento_excecoes/
│   ├── desafio01.py
│   ├── desafio02.py
│   └── desafio03.py
│
└── 05_estruturas_de_dados/
    ├── desafio01.py
    ├── desafio02.py
    └── desafio03.py
```

---

## 🚀 Como Usar este Repositório (Passo a Passo)

Siga rigorosamente o fluxo de trabalho abaixo para desenvolver e versionar as resoluções:

### 1. Clonar o repositório
Abra o terminal no diretório onde deseja trabalhar e execute:
```bash
git clone <URL_DO_REPOSITORIO>
cd <NOME_DO_REPOSITORIO>
```

### 2. Criar a sua branch de trabalho
**Nunca faça alterações diretamente na branch `main`**. Crie uma branch própria utilizando o padrão `resolucao/seu-nome`:
```bash
git checkout -b resolucao/fulano
```

### 3. Escolher e abrir a questão
- Navegue até a pasta do tópico correspondente (ex: `01_tipos_de_dados/`).
- Abra o arquivo do desafio no seu editor de código (ex: `desafio01.py`).
- Leia a descrição do problema e os exemplos contidos na docstring no topo do arquivo.

### 4. Implementar a lógica
- Localize a assinatura da função.
- **APAGUE O `pass`** que está no corpo da função.
- Escreva a lógica da solução respeitando a tipagem dos argumentos e utilizando `return` para entregar o resultado esperado:

```python
# ANTES:
def soma(a: int, b: int) -> int:
    pass

# DEPOIS:
def soma(a: int, b: int) -> int:
    return a + b
```

### 5. Executar o código e testar
Cada arquivo possui um script embutido com múltiplos casos de teste para validar a resposta.

Você pode rodar de duas formas:
- **Pelo Terminal:**
  ```bash
  python 01_tipos_de_dados/desafio01.py
  ```
  *(ou `python3 01_tipos_de_dados/desafio01.py`, dependendo do seu sistema operacional)*

- **Pelo VS Code (Interface Visual):**
  - Instale a extensão oficial **Python** (desenvolvida pela Microsoft).
  - Abra o arquivo desejado e clique no botão de play (**Run Python File**) no canto superior direito do editor, ou use o atalho padrão de execução.

### 6. Conferir o resultado no terminal
Ao rodar o arquivo, logs informativos indicarão se o código funcionou:
- Se acertar tudo, você verá a mensagem de sucesso com `[OK]` em todos os casos:
  ```text
  ==================================================
  Iniciando testes para: soma
  ==================================================
  [OK] Teste 1 passou!
  [OK] Teste 2 passou!
  [OK] Teste 3 passou!
  --------------------------------------------------
  Resultado: 3/3 testes passaram.
  ==================================================
  ```
- Se errar, o script indicará `[FALHA]`, mostrando a entrada avaliada, o resultado esperado e o que a sua função retornou:
  ```text
  [FALHA] Teste 2 falhou!
    Entrada:  (1900,)
    Esperado: False
    Obtido:   True
  ```
  Ajuste o seu código até que todos os testes passem.

### 7. Comitar e salvar NA SUA BRANCH
Após garantir que todos os testes do arquivo passaram com sucesso, faça o commit **na sua branch**:
```bash
git add 01_tipos_de_dados/desafio01.py
git commit -m "feat: resolve desafio 01 de tipos de dados"
```

Para subir o seu progresso para o repositório remoto:
```bash
git push -u origin resolucao/fulano
```

---

## 💡 Observações para Iniciantes em Python

- **Indentação:** Blocos de código em Python são definidos por recuo (4 espaços), não por chaves `{}`. Mantenha o alinhamento consistente.
- **O que é o `pass`:** O comando `pass` é apenas um marcador de bloco vazio exigido pela sintaxe do Python. Ele **deve ser apagado** ao escrever sua lógica.
- **Iterações:** Evite laços com índices manuais (`range(len(lista))`). Em Python, itere diretamente sobre os itens: `for item in lista:`.
