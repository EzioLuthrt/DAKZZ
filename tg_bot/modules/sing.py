import random
from telegram.ext import run_async, Filters
from telegram import Message, Chat, Update, Bot, MessageEntity
from tg_bot import dispatcher
from tg_bot.modules.disable import DisableAbleCommandHandler

SFW_STRINGS = (
    "🎶 മിഴിയറിയാതെ വന്നു നീ മിഴിയൂഞ്ഞാലിൽ... കനവറിയാതെയേതോ കിനാവു പോലെ... 🎶.",
    "🎶 നിലാവിന്റെ നീലഭസ്മ കുറിയണിഞ്ഞവളേ... കാതിലോലക്കമ്മലിട്ടു കുണുങ്ങി നിന്നവളേ... 🎶",
    "🎶 എന്തിനു വേറൊരു സൂര്യോദയം... നീയെൻ പൊന്നുഷസ്സന്ധ്യയല്ലേ... 🎶",
    "🎶 ശ്രീരാഗമോ തേടുന്നിതെൻ വീണതൻ പൊൻ തന്ത്രിയിൽ... 🎶",
    "🎶 മഴത്തുള്ളികൾ പൊഴിഞ്ഞീടുമീ നാടൻ വഴി... നനഞ്ഞോടിയെൻ കുടക്കീഴിൽ നീ വന്ന നാൾ... 🎶",
    "🎶 നീയൊരു പുഴയായ് തഴുകുമ്പോൾ ഞാൻ പ്രണയം വിടരും കരയാവും... 🎶",
    "🎶 അല്ലിമലർ കാവിൽ പൂരം കാണാൻ... അന്നു നമ്മൾ പോയി രാവിൽ നിലാവിൽ... 🎶",
    "🎶 ചന്ദനച്ചോലയിൽ മുങ്ങിനീരാടിയെൻ ഇളമാൻ കിടാവേ ഉറക്കമായോ... 🎶",
    "🎶 അന്തിപ്പൊൻവെട്ടം കടലിൽ മെല്ലെത്താഴുമ്പോൾ... മാനത്തെ മുല്ലത്തറയില് മാണിക്യച്ചെപ്പ്... 🎶",
    "🎶 താമരപ്പൂവിൽ വാഴും ദേവിയല്ലോ നീ... പൂനിലാക്കടവിൽ പൂക്കും പുണ്യമല്ലോ നീ... 🎶",
    "🎶 കുന്നിമണിച്ചെപ്പു തുറന്നെണ്ണി നോക്കും നേരം, പിന്നിൽവന്നു കണ്ണു പൊത്തും കള്ളനെങ്ങു പോയി... 🎶",
  )

@run_async
def sing(bot: Bot, update: Update):
    bot.sendChatAction(update.effective_chat.id, "typing") # Bot typing before send messages
    message = update.effective_message
    if message.reply_to_message:
      message.reply_to_message.reply_text(random.choice(SFW_STRINGS))
    else:
      message.reply_text(random.choice(SFW_STRINGS))

__help__ = """
- /sing  ചില മലയാളം പാട്ടുകളുടെ ആദ്യ വരികൾ ലഭിക്കും.
"""

__mod_name__ = "Sing Malayalam"

SING_HANDLER = DisableAbleCommandHandler("sing", sing)

dispatcher.add_handler(SING_HANDLER)
