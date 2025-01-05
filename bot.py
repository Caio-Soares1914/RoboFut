from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import pandas as pd
from datetime import datetime

# Função para buscar os jogos do dia
def buscar_jogos():
    arquivo = r"C:\Users\caios\OneDrive\Área de Trabalho\bot.py\jogos.xlsx"
    try:
        # Lendo a planilha
        df = pd.read_excel(arquivo)
        df['Data'] = pd.to_datetime(df['Data'], format='%d/%m/%Y')
        hoje = datetime.now().date()
        jogos_hoje = df[df['Data'] == hoje]

        if jogos_hoje.empty:
            return "Nenhum jogo encontrado para hoje!"
        else:
            jogos = "Jogos de hoje:\n"
            for _, row in jogos_hoje.iterrows():
                jogos += f"{row['Time Casa']} x {row['Time Fora']} às {row['Horário']} no {row['Local']}\n"
            return jogos
    except FileNotFoundError:
        return "Erro: Arquivo da planilha não encontrado."
    except Exception as e:
        return f"Erro ao processar a planilha: {e}"

# Função para o comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Olá! Eu sou seu bot Telegram!")

# Função para o comando /jogos
async def jogos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    jogos_do_dia = buscar_jogos()
    await update.message.reply_text(jogos_do_dia)

# Configurando o bot
def main():
    # Substitua 'SEU_TOKEN_AQUI' pelo token do seu bot do Telegram
    application = ApplicationBuilder().token("7639695224:AAEctEShMuztWgFfSnzJpGHhlgomTEAnT-w").build()

    # Adicionando os manipuladores de comandos
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("jogos", jogos))

    # Inicia o bot
    application.run_polling()

if __name__ == "__main__":
    main()
