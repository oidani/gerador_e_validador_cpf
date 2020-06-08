# Descrição

Aplicação que recebe um CPF e retorna se o mesmo é válido.

# User Stories

- [ ] O usuário poderá inserir o CPF através de um campo de texto
    - [ ] O CPF pode ser inserido com pontos e hífen
    - [ ] O CPF pode ser inserido sem pontos e hífen
- [ ] A aplicação irá verificar se o CPF inserido está no padrão necessário para validação
    - [ ] Padrão 1: 11 dígitos numéricos inteiros sem pontos e hífen (ex. XXXXXXXXXXX)
    - [ ] Padrão 2: 14 dígitos, sendo 11 numéricos inteiros, com 1 ponto na 4ª posição, 1 ponto na 8ª posição e 1 hífen na 12ª posição (ex. XXX.XXX.XXX-XX)
- [ ] A aplicação irá validar o CPF verificando se existem pontos e hífen
    - [ ] Se existirem, deverão ser retirados e mantidos apenas os números
- [ ] A aplicação realizará a validação do CPF
- [ ] A aplicação retornará na tela uma mensagem com o CPF inserido e se o mesmo é válido
    - [ ] O CPF deverá ser exibido com pontos e hífen
