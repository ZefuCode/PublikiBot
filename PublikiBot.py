import sqlite3
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, CallbackContext, CommandHandler

TOKEN = "7986044887:AAGKRw8_EGIQQRf-r4dqe0bFDsf7aZvnaQQ"
DB_PATH = "bot_respuestas.db"

# inicio el bot
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("🎬 ¡Bienvenido a Publiki! Envíanos tu número de ticket (8 dígitos).")

# Manejo de mensajes
async def echo(update: Update, context: CallbackContext):
    user_text = update.message.text.strip().lower()

    if user_text == "hola":
        await update.message.reply_text("🎬 ¡Bienvenido a Publiki! Envíanos tu número de ticket (8 dígitos).")
        return

    if user_text.isdigit() and len(user_text) == 8:
        ticket = user_text

        # Conexión con SQLite bot_respuestas
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # Buscar respuesta 
        cursor.execute('''
            SELECT r.contenido
            FROM palabras_clave pc
            JOIN respuestas r ON pc.respuesta_id = r.id
            WHERE pc.palabra = ?
        ''', (ticket,))
        
        result = cursor.fetchone()
        conn.close()

        if result:
            contenido = result[0]
            await update.message.reply_text(f"🎉 ¡Promoción encontrada!\n\n{contenido}")
        else:
            await update.message.reply_text("❌ El número de ticket no es válido.")
    else:
        await update.message.reply_text("Por favor, ingresa un número de ticket válido de 8 dígitos.")


app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

if __name__ == "__main__":
    print("🤖 Bot Publiki iniciado y esperando mensajes...")
    app.run_polling()
