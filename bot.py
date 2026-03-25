import os
from telegram.ext import ApplicationBuilder, MessageHandler, filters

BOT_TOKEN = os.getenv("BOT_TOKEN")

TARGET_USER_ID = 7214305535
TARGET_CHAT_ID = -1003746059760

async def handler(update, context):
    msg = update.message

    if not msg:
        return

    print("Nachricht von:", msg.from_user.id)

    if msg.from_user.id == TARGET_USER_ID:
        print("MATCH!")
        await context.bot.forward_message(
            chat_id=TARGET_CHAT_ID,
            from_chat_id=msg.chat_id,
            message_id=msg.message_id
        )

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.ALL, handler))

app.run_polling()
