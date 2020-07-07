# Descrição

Aplicação com possibilidade de validar um CPF inserido pelo usuário e gerar um CPF válido.

## Aviso importante: esta aplicação deve ser utilizada para fins de teste de software.

# Fluxo de desenvolvimento e validação

## Geral

- [ ] A aplicação irá exibir uma mensagem solicitando que o usuário escolha entre (1) gerar um CPF válido, (2) validar um CPF ou (3) sair do programa
- [ ] Se o usuário escolher (1) ou (2), a aplicação irá limpar a tela e exibir o respectivo programa

## Gerar CPF

- [X] A aplicação irá gerar um número de CPF válido
    - [X] O CPF gerado tem de conter 11 dígitos numéricos inteiros
    - [X] O CPF gerado não pode conter todos os dígitos iguais (ex. 00000000000, 33333333333), uma vez que tais valores são considerados CPFs inválidos
- [X] A aplicação retornará na tela o CPF no formato abaixo e sua UF
    - [X] Formato: 14 dígitos, sendo 11 numéricos inteiros, com pontos e hífen (ex. XXX.XXX.XXX-XX)
    - [X] UF: formato de 2 letras maiúsculas

## Validar CPF

- [X] A aplicação exibirá uma mensagem solicitando que o usuário insira o CPF para validação
    - [X] O CPF deve ser inserido sem pontos e sem hífen
- [X] A aplicação irá verificar se o CPF inserido está no padrão necessário para validação
    - [X] Padrão: 11 dígitos numéricos inteiros sem pontos e hífen (ex. XXXXXXXXXXX)
- [X] A aplicação realizará a validação do CPF
    - [X] Verificar se o número inserido possui exatamente 11 dígitos inteiros
    - [X] Verificar se o o número inserido não possui todos os dígitos iguais (ex. 00000000000, 33333333333, etc), uma vez que tais valores são considerados CPFs inválidos
- [X] A aplicação retornará na tela uma mensagem com o CPF inserido e se o mesmo é válido
    - [X] O CPF deverá ser exibido com pontos e hífen
    - [X] Se o CPF for válido, deverá ser exibida sua UF
    - [X] O formato da UF será 2 letras maiúsculas
