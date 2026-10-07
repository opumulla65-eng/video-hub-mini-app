import os

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes


BOT_TOKEN = os.getenv("8749971153:AAERNf4VZGLbaGdvXboiVd3MNaHu3DQKYEU")

MINI_APP_URL = "https://opumulla65-eng.github.io/video-hub-mini-app/"

IMAGES = [
    "https://yourimageshare.com/ib/2CG3laxvWW.jpg",
    "https://yourimageshare.com/ib/1TefjkpvgF.jpg",
    "https://yourimageshare.com/ib/Oy3CGsVwbe.jpg",
    "https://yourimageshare.com/ib/zTAMaZ8Hi5.jpg",
    "https://yourimageshare.com/ib/FeEsFEYkC4.jpg",
    "https://yourimageshare.com/ib/eMARgYk7AJ.jpg",
]

CAPTION = (
    "🎬 <b>WELCOME TO VIDEO HUB</b>\n\n"
    "🔥 <b>MOVIES • DRAMA • VIRAL VIDEOS</b>\n\n"
    "🎥 Discover the latest movies, drama, "
    "viral clips and trending videos in one place.\n\n"
    "✨ Latest & trending content\n"
    "🎞️ Movies and drama collection\n"
    "🔥 Viral & popular videos\n"
    "📱 Fast & mobile-friendly experience\n\n"
    "🚀 <b>READY TO WATCH?</b>\n"
    "👇 Tap the button below and explore Video Hub."
)

BUTTON = InlineKeyboardMarkup([
    [
        InlineKeyboardButton(
            "🎬 WATCH VIDEOS",
            web_app={"url": MINI_APP_URL}
        )
    ]
])


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for image in IMAGES:
        await update.message.reply_photo(
            photo=image,
            caption=CAPTION,
            parse_mode="HTML",
            reply_markup=BUTTON
        )


def main():
    if not BOT_TOKEN:
        print("❌ BOT_TOKEN পাওয়া যায়নি")
        return

    port = int(os.getenv("PORT", "10000"))
    hostname = os.getenv("RENDER_EXTERNAL_HOSTNAME")

    if not hostname:
        print("❌ RENDER_EXTERNAL_HOSTNAME পাওয়া যায়নি")
        return

    webhook_url = f"https://{hostname}/telegram/webhook"

    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    print("✅ Bot service is starting...")
    print(f"🌐 Webhook: {webhook_url}")

    app.run_webhook(
        listen="0.0.0.0",
        port=port,
        url_path="telegram/webhook",
        webhook_url=webhook_url,
    )


if __name__ == "__main__":
    main()
