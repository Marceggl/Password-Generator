# Gerador de senha simple

Este gerador de senha aceita dois parametros:

|    **Argumentos**    |                   **Descrição**                   |
|:--------------------:|:-------------------------------------------------:|
|   **-t, --tamanho**  | Tamanho da senha a ser gerada (padrão: 15)        |
| **-q, --quantidade** | Quantidade de senhas a serem geradas (padrão: 10) |

## Adicionar no Path

Para utiliza-la sem necessitar digitar o caminho adicione o executável no PATH do usuário:
1. Acesse Propriedades do sistema > Avançado
2. Acesse Variaveis de ambiente
3. Localize "Path" em "váriaveis de usuário para \<seu user\>" e clique 2x vezes nele
4. Clique em novo e adicione o caminho até o local em que você salvou o usuário
5. E clique em "ok" para salvar

## Gerar senhas

1. Selecionar quantidade de characteres:

Apenas utilize -t ou --tamanho seguido de um número e a senha será gerada, no exemplo abaixo é gerado uma senha de 10 characteres

```
geradorSenha -t 10
# Output: 
Random password is: TYL'QY,]c)
```

2. Gerar várias senhas:

Apenas utilize -q ou --quantidade seguido de um número e a senha será gerada, no exemplo abaixo é gerado 5 senhas

```
geradorSenha -q 5
# Output: 
Random password is: clL'IMi1uRLyyl}
Random password is: k\lTgc&_;KspG#=
Random password is: L|S]7!|Ui_<H\8Q
Random password is: 38.T&Rr^l,Ca|W%
Random password is: "cqvec/362Ak<KL
```