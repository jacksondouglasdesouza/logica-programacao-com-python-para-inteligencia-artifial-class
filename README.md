# PROJETO FINAL DO CURSO DE LÓGICA DE PROGRAMAÇÃO PARA DATA SCIENCE E AI COM PYTHON
## Verificação da Lei de Benford

## Descrição do Projeto

Este projeto implementa uma verificação para determinar se um conjunto de dados numéricos segue a **Lei de Benford**, que afirma que, em muitos conjuntos de dados, o primeiro dígito dos números tende a seguir uma distribuição não uniforme. Os dígitos menores ocorrem com mais frequência como o primeiro dígito em comparação com os maiores.

A Lei de Benford prevê as seguintes proporções para o primeiro dígito dos números:

| Dígito | Proporção (%) |
|--------|---------------|
| 1      | 30.1%         |
| 2      | 17.6%         |
| 3      | 12.5%         |
| 4      | 9.7%          |
| 5      | 7.9%          |
| 6      | 6.7%          |
| 7      | 5.8%          |
| 8      | 5.1%          |
| 9      | 4.6%          |

Este programa compara as proporções encontradas no conjunto de dados fornecido com as proporções esperadas pela Lei de Benford e exibe a diferença.

## Estrutura do Código

### 1. Coleta do Primeiro Dígito
O primeiro passo do programa é percorrer cada número na lista `dados` e extrair o primeiro dígito significativo. Em seguida, o programa atualiza uma lista de contagem (`contagem_digitos`) para cada dígito de 1 a 9.

```python
for numero in dados:
    primeiro_digito = int(str(numero)[0])
    contagem_digitos[primeiro_digito] += 1
#--
```

### 2. Cálculo das Proporções Encontradas
O número total de elementos no conjunto de dados é obtido e utilizado para calcular a proporção real de cada dígito:

```python
total_numeros = len(dados)
proporcao_encontrada = [0] * 10

for i in range(1, 9):
    proporcao_encontrada[i] = (contagem_digitos[i] / total_numeros) * 100
#--
```

### 3. Comparação com a Lei de Benford
Para cada dígito de 1 a 9, o programa compara a proporção encontrada com a proporção esperada da Lei de Benford, exibindo a diferença em uma tabela:

```python
print("Dígito | Proporção Esperada (%) | Proporção Encontrada (%) | Diferença (%)")
for i in range(1, 10):
    esperado = benford_proporcoes[i]
    encontrado = proporcao_encontrada[i]
    diferenca = abs(esperado - encontrado)
    print("%5d   | %21.1f   | %24.1f   | %12.1f" % (i, esperado, encontrado, diferenca))
#--
```

### 4. Alerta de Diferenças Significativas
Caso a diferença entre a proporção esperada e a proporção encontrada para qualquer dígito seja maior que 1%, o programa exibe uma mensagem de alerta:

```python
if diferenca > 1:
    print("** Diferença significativa encontrada no dígito %d: %.1f%% **" % (i, diferenca))
#--
```

## Requisitos

- Python 3.12.6 ou Superior

## Como Executar

1. Clone este repositório ou copie o código para seu ambiente local.
2. Execute o arquivo principal que contém o código da verificação da Lei de Benford.
3. O resultado será uma tabela comparativa com as proporções esperadas e encontradas, além de alertas sobre diferenças significativas.

## Dados

Os dados utilizados no programa são uma lista de números predefinidos para análise:

```python
dados = [
    4562.73, 1140.67, 1436.83, 1140.67, 4562.73, 1140.67, 4562.73, 1859.86, 1859.86, 27.66,
    ...
    # (continua com a lista completa de dados)
]
```

## Exemplo de Saída

```text
Dígito | Proporção Esperada (%) | Proporção Encontrada (%) | Diferença (%)
-------|-----------------------|--------------------------|---------------
    1   |                 30.1   |                   29.8   |          0.3
    2   |                 17.6   |                   18.1   |          0.5
    3   |                 12.5   |                   12.9   |          0.4
    ...
** Diferença significativa encontrada no dígito 4: 1.5% **
```

## Conclusão

Este programa permite verificar rapidamente se os dados seguem ou não a Lei de Benford, o que pode ser útil em análises de fraudes ou verificações de dados financeiros, por exemplo.

---

Sinta-se à vontade para sugerir melhorias ou abrir issues no repositório caso encontre algum problema!

> 💻 Me adicione nas redes sociais:

<p><a href="https://twitter.com/catmorphnft"><img src="https://img.shields.io/twitter/follow/catmorphnft?style=social" alt="Twitter: @catmorphnft"></a><a href="https://www.linkedin.com/in/jacksondouglasdesouzaa"><img src="https://img.shields.io/badge/-jackson%20Douglas-blue?style=flat-square&amp;logo=Linkedin&amp;logoColor=white&amp;link=https://www.linkedin.com/in/jacksondouglasdesouzaa/" alt="Linkedin: @jacksondouglasdesouzaa">
</a><a href="https://github.com/jacksondouglasdesouza"><img src="https://img.shields.io/github/followers/jacksondouglasdesouza?label=follow&amp;style=social" alt="GitHub:@jacksondouglasdesouza"></a><a href="https://github.com/jacksondouglasdesouza"><img src="https://img.shields.io/github/followers/jacksondouglasdesouza?label=follow&amp;style=social" alt="GitHub: @jacksondouglasdesouza"></a><a href="https://dev.to/jacksondouglasdesouzaa"><img src="https://d2fltix0v2e0sb.cloudfront.net/dev-badge.svg" alt="Perfil DEV de jacksondouglasdesouzaa" height="20" width="25">
</a><a href="mailto:jacksondouglasdesouza@gmail.com"><img src="https://img.shields.io/badge/Gmail-jacksondouglasdesouza-red" alt="Gmail: disponível"></a>