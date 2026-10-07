import os

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes


# ==============================
# BOT CONFIG
# ==============================

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = os.getenv("ADMIN_ID")

MINI_APP_URL = "https://opumulla65-eng.github.io/video-hub-mini-app/"


# ==============================
# IMAGES
# ==============================

IMAGES = [
    "https://yourimageshare.com/ib/2CG3laxvWW.jpg",
    "https://yourimageshare.com/ib/1TefjkpvgF.jpg",
    "https://yourimageshare.com/ib/Oy3CGsVwbe.jpg",
    "https://yourimageshare.com/ib/zTAMaZ8Hi5.jpg",
    "https://yourimageshare.com/ib/FeEsFEYkC4.jpg",
    "https://yourimageshare.com/ib/eMARgYk7AJ.jpg",
]


# ==============================
# MAIN TEXT
# ==============================

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


# ==============================
# MINI APP BUTTON
# ==============================

BUTTON = InlineKeyboardMarkup([
    [
        InlineKeyboardButton(
            "🎬 WATCH VIDEOS",
            web_app={"url": MINI_APP_URL}
        )
    ]
])


# ==============================
# /START
# ==============================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    for image in IMAGES:

        await update.message.reply_photo(
            photo=image,
            caption=CAPTION,
            parse_mode="HTML",
            reply_markup=BUTTON
        )


# ==============================
# /MYID
# ==============================

async def myid(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        f"🆔 Your Telegram User ID: "
        f"<code>{update.effective_user.id}</code>",
        parse_mode="HTML",
    )


# ==============================
# ADMIN CHECK
# ==============================

def is_admin(update: Update) -> bool:

    if not ADMIN_ID:
        return False

    if not update.effective_user:
        return False

    return str(update.effective_user.id) == str(ADMIN_ID)


# ==============================
# /ADMIN
# ==============================

async def admin(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not is_admin(update):

        await update.message.reply_text(
            "⛔ You are not authorized to use this command."
        )

        return

    await update.message.reply_text(
        "🛠️ <b>ADMIN PANEL</b>\n\n"
        "✅ Admin access verified.\n\n"
        "📊 Statistics — Coming next\n"
        "🎬 Video management — Coming next\n"
        "📢 Broadcast — Coming next",
        parse_mode="HTML",
    )


# ==============================
# MAIN
# ==============================

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

    app = (
        Application
        .builder()
        .token(BOT_TOKEN)
        .build()
    )

    # Commands
    app.add_handler(
        CommandHandler("start", start)
    )

    app.add_handler(
        CommandHandler("myid", myid)
    )

    app.add_handler(
        CommandHandler("admin", admin)
    )

    print("================================")
    print("✅ Bot service is starting...")
    print(f"🌐 Webhook: {webhook_url}")
    print("================================")

    app.run_webhook(
        listen="0.0.0.0",
        port=port,
        url_path="telegram/webhook",
        webhook_url=webhook_url,
    )


# ==============================
# RUN
# ==============================

if __name__ == "__main__":
    main()
