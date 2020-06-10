# Descrição

Aplicação que recebe um CPF do usuário e retorna na tela se o mesmo é válido. Se for válido, também será exibida a UF do CPF.

# User Stories

- [X] O usuário poderá inserir o CPF através de um campo de texto
    - [X] O CPF deve ser inserido sem pontos e hífen
- [X] A aplicação irá verificar se o CPF inserido está no padrão necessário para validação
    - [X] Padrão: 11 dígitos numéricos inteiros sem pontos e hífen (ex. XXXXXXXXXXX)
- [X] A aplicação realizará a validação do CPF
    - [X] Verificar se o número inserido possui exatamente 11 dígitos inteiros
    - [ ] Verificar se o o número inserido não possui todos os dígitos iguais (ex. 00000000000, 33333333333, etc), uma vez que tais valores são considerados CPFs inválidos
- [X] A aplicação retornará na tela uma mensagem com o CPF inserido e se o mesmo é válido
    - [X] O CPF deverá ser exibido com pontos e hífen
    - [X] Se o CPF for válido, deverá ser exibida sua UF
    - [X] O formato da UF será 2 letras maiúsculas
