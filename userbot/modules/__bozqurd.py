# RoBotlarimTg - BozQurd UserBot
# t.me/RoBotlarimTg
# t.me/aykhan_s
# t.me/BozQurdResmi
# Support - @BozQurdSup
# Owner - @aykhan_s


from userbot.cmdhelp import CmdHelp
from userbot import cmdhelp
from userbot import CMD_HELP
from userbot.events import register as bozqurd

# ██████ LANGUAGE CONSTANTS ██████ #

from userbot.language import get_value
LANG = get_value("__misaki")

# ████████████████████████████████ #

@bozqurd(outgoing=True, pattern="^.misaki(?: |$)(.*)")
async def bozqurd(event):
    """ necesen """
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await event.edit(str(CMD_HELP[args]))
        else:
            await event.edit(LANG["NEED_PLUGIN"])
    else:
        string = ""
        sayfa = [sorted(list(CMD_HELP))[i:i + 5] for i in range(0, len(sorted(list(CMD_HELP))), 5)]
        
        for i in sayfa:
            string += f'`▶️`'
            for sira, a in enumerate(i):
                string += "`" + str(a)
                if sira == i.index(i[-1]):
                    string += "`"
                else:
                    string += "`, "
            string += "\n"
        await event.edit(LANG["NEED_MODULE"] + '\n\n' + string)
