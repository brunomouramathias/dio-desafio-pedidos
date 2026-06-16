# Desafio de Código: Gerando Relatório de Pedidos por Embalagem 📦

Repositório destinado à resolução do desafio prático de código da trilha de Python da **Digital Innovation One (DIO)**. O objetivo é demonstrar proficiência em manipulação de **Strings**, **Laços de Repetição (For)** e estruturação de dados em **Dicionários**.

## 📝 Descrição do Desafio

Uma empresa produtora de papéis para embalagens precisa gerar um relatório totalizador de pedidos. O programa recebe uma quantidade `N` de pedidos e, em seguida, as informações de cada pedido em formato de string separada por vírgula (`Nome, Tipo de Embalagem, Quantidade`).

O algoritmo deve extrair as informações, somar a quantidade solicitada de cada tipo de embalagem e exibir um relatório contendo a tonelagem total de `"saco"`, `"papelao ondulado"` e `"papel kraft"`.

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python 3
* **Conceitos Aplicados:** 
  - Manipulação de Strings (`.split()`)
  - Estruturas de Dados Dinâmicas (`dict` / Dicionários)
  - Estruturas de Repetição (`for` loops)
  - Operadores Ternários (`if/else` inline) para formatação de saída

## 🧠 Lógica da Solução

1. **Leitura de Dados:** O programa inicia lendo o valor `N`, determinando o número de iterações do laço de repetição.
2. **Processamento da String:** A cada iteração, o programa utiliza a função `split(", ")` para desempacotar a string em três variáveis (`cliente`, `embalagem`, `quantidade`).
3. **Agrupamento com Dicionário:** O dicionário `totais` é utilizado como uma estrutura chave-valor para somar as toneladas. O uso do método `.get(chave, valor_padrao)` previne erros caso a chave ainda não exista no dicionário, inicializando-a com `0` e somando a nova `quantidade`.
4. **Formatação de Saída:** Por fim, um laço `for` percorre uma lista estática com a ordem exata exigida pela regra de negócios e realiza a impressão. Utilizamos a função `.is_integer()` para garantir que toneladas inteiras não sejam impressas com casas decimais desnecessárias (ex: `22.0` vira `22`).

## 🚀 Como Executar

Clone este repositório e execute o script em qualquer terminal que tenha o Python instalado:

```bash
git clone https://github.com/SEU_USUARIO/dio-desafio-pedidos.git
cd dio-desafio-pedidos
python main.py
```

Exemplo de entrada:
```text
3
Joao, saco, 10
Maria, papelao ondulado, 8
Pedro, saco, 12
```

Exemplo de saída esperada:
```text
saco: 22
papelao ondulado: 8
papel kraft: 0
```

---
*Desafio resolvido por Bruno Moura Mathias.*
