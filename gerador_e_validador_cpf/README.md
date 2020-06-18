# Descrição

Aplicação com possibilidade de validar um CPF inserido pelo usuário e gerar um CPF válido.

## Aviso importante: esta aplicação deve ser utilizada para fins de teste de software.

# Fluxo de utilização

## Geral

 - [X] Ao iniciar a aplicação, o usuário irá visualizar uma mensagem solicitando que escolha entre gerar um CPF válido ou validar um CPF
 - [X] O usuário irá escolher entre gerar um CPF válido ou validar um CPF
 - [ ] Ao receber o resultado de sua solicitação na tela, o usuário poderá escolher se deseja receber a saída obtida em um arquivo nos seguintes formatos:
    - [ ] TXT
    - [ ] XML
    - [ ] CSV
    - [ ] JSON
    - [ ] YAML
    - [ ] Não deseja receber via arquivo
- [ ] O usuário poderá ver na tela o caminho onde os arquivos escolhidos foram salvos

## Gerar CPF

- [X] O usuário poderá ver na tela o CPF gerado no formato abaixo, bem como sua UF
    - [X] Formato: 14 dígitos, sendo 11 numéricos inteiros, com pontos e hífen (ex. XXX.XXX.XXX-XX)
    - [X] UF: formato de 2 letras maiúsculas

## Validar CPF

- [X] O usuário irá visualizar uma mensagem solicitando que insira um CPF para validação, no formato numérico
- [X] O usuário irá inserir um valor para validação
- [X] O usuário irá visualizar na tela se o valor inserido é ou não um CPF válido
    - [X] Se for um CPF válido, o usuário também visualizará na tela a UF do CPF inserido

# Fluxo de desenvolvimento

## Geral

- [X] A aplicação irá exibir uma mensagem solicitando que o usuário escolha entre gerar um CPF válido ou validar um CPF
- [X] A aplicação irá exibir na tela o programa referente à escolha do usuário
- [ ] Após enviar a saída na tela, a aplicação solicitará que o usuário escolha se deseja receber a saída obtida em um arquivo nos seguintes formatos:
    - [ ] TXT
    - [ ] XML
    - [ ] CSV
    - [ ] JSON
    - [ ] YAML
    - [ ] Não deseja receber via arquivo
- [ ] A aplicação exibirá na tela o caminho onde os arquivos escolhidos foram salvos
    - [ ] No Windows: a definir
    - [ ] No Linux: a definir

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
