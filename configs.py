from os import getenv

class Config:
    API_ID = int(getenv("API_ID", "21419016"))
    API_HASH = getenv("API_HASH", "79198e1eb4cfd0f771a89d83b9144e7e")
    BOT_TOKEN = getenv("BOT_TOKEN", "7299707119:AAHyKZdC7nM85vnxbiqbgX1cn6M7XGYxkk0")

    # Admin / Owner IDs
    SUDO = list(map(int, getenv(
        "SUDO",
        "7554081592 7736226123 7564050858 5656436152"
    ).split()))

    MONGO_URI = getenv(
        "MONGO_URI",
        "mongodb+srv://melodysotto4_db_user:BCUKIKDEAqFEzeCj@cluster0.trrt89o.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    )

    # Posts to copy
    POSTS = [
        "https://t.me/forward_hack_lnx/46",
        "https://t.me/forward_hack_lnx/39",
        "https://t.me/forward_hack_lnx/40"
    ]

    # 🚫 ILLEGAL WORDS (BOT SIDE FILTER)
    ILLEGAL_WORDS = [
        "@controllerbot",
        "creatings",
        "tasks",
        "tasks.",
        "@LivegramBot",
        "accomplish"
    ]

cfg = Config()
