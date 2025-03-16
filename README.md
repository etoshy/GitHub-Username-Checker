# GitHub Username Checker

## Descrição
Este projeto é um script Python que verifica a disponibilidade de nomes de usuário no GitHub. Ele gera combinações de nomes baseadas em parâmetros definidos pelo usuário e testa se os nomes estão disponíveis ou já estão em uso.

## Tecnologias Utilizadas
- **Linguagem:** Python 3
- **Bibliotecas:**
  - `requests`: Para fazer requisições HTTP ao GitHub
  - `beautifulsoup4`: Para analisar o HTML das páginas
  - `itertools`: Para gerar combinações de caracteres

## Pré-requisitos
Antes de rodar o script, certifique-se de ter o Python 3 instalado e as bibliotecas necessárias. Para instalá-las, use:

```bash
pip install requests beautifulsoup4
```

## Como Usar
O script pode ser executado diretamente pelo terminal. O formato do comando é:

```bash
python main.py {numero_de_caracteres} {prefixo} {sufixo} [-a para letras] [-1 para números]
```

### Exemplos
1. **Verificar nomes de 4 caracteres com prefixo "78kj" e sufixo "kj", usando letras e números:**
   ```bash
   python main.py 4 78kj kj -a -1
   ```

2. **Verificar nomes de 5 caracteres apenas com letras:**
   ```bash
   python main.py 5 "" "" -a
   ```

3. **Verificar nomes de 6 caracteres apenas com números, prefixo "12" e sufixo "34":**
   ```bash
   python main.py 6 12 34 -1
   ```

Caso não queira um prefixo ou sufixo, basta deixar em branco (`""`).

## Criador
Projeto desenvolvido por [etoshy](https://github.com/etoshy).
