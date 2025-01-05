Meu Bot Telegram para Jogos

Este bot foi desenvolvido por Caio Soares e é capaz de exibir os jogos de futebol do dia de forma simples e eficiente utilizando dados de uma planilha.

Funcionalidades

/start: Mensagem de boas-vindas.

/jogos: Mostra os jogos de futebol do dia com base em uma planilha.

Leitura de uma planilha Excel com informações como times, horários e locais dos jogos.

Como Configurar

1. Pré-requisitos

Certifique-se de ter as seguintes ferramentas instaladas:

Python 3.10 ou superior

pip

Instale as dependências necessárias:

pip install python-telegram-bot pandas openpyxl

2. Estrutura do Projeto

A estrutura do projeto deve ser semelhante a:

D:\bot.py
├── bot.py       # Arquivo principal com o código do bot
├── jogos.xlsx   # Planilha contendo os jogos

3. Configuração do Bot no Telegram

Crie um novo bot utilizando o BotFather.

Copie o token fornecido pelo BotFather.

Substitua SEU_TOKEN_AQUI no arquivo bot.py pelo token do seu bot.

4. Estrutura da Planilha

A planilha jogos.xlsx deve conter as seguintes colunas:

Time Casa: Nome do time da casa.

Time Fora: Nome do time visitante.

Horário: Horário do jogo (HH:MM).

Local: Local onde o jogo será realizado.

Data: Data do jogo no formato DD/MM/AAAA.

Exemplo:

Time Casa

Time Fora

Horário

Local

Data

CRB

Água Santa

15:15

Estádio Alonso de Carvalho

03/01/2025

Como Executar

Navegue até o diretório onde o arquivo bot.py está localizado:

cd D:\bot.py

Execute o bot:

python bot.py

Abra o Telegram, encontre o seu bot e utilize os comandos /start ou /jogos para interagir.

Melhorias Futuras

Suporte a múltiplos idiomas.

Integração com bancos de dados.

Notificações automáticas para os jogos do dia.

Adicionar suporte para busca de jogos por time ou data específica.

Contato

Desenvolvido por Caio Soares. Entre em contato para sugestões ou melhorias:

Email: caio.evangelistasoares@hotmail.com

GitHub: https://github.com/Caio-Soares1914
