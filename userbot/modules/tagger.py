# RoBotlarimTg - tyeni.py
# Burdan hər hansı bir şeyi
# Kopyalayan Peysərdi...!!!
# Sahib - @aykhan_s
# _-_-_-_-_-_-_-_-_-_-_-_-_-_ #

import random
import asyncio
from os import execl
import sys
import io
import sys
from userbot.events import register as aykhan
from userbot import BOTLOG, BOTLOG_CHATID, CMD_HELP, bot
from telethon.tl.types import ChannelParticipantsAdmins as cp
from time import sleep
from userbot.cmdhelp import CmdHelp
class FlagContainer:
    is_active = False
# Əkmə Oğlum...!!!
reng = (
 "🔴",
 "🟠",
 "🟡",
 "🟢",
 "🔵",
 "🟣",
 "🟤",
 "⚫",
 "⚪",
)
# Əkmə Oğlum...!!!
reqem = (
 "0️⃣",
 "1️⃣",
 "2️⃣",
 "3️⃣",
 "4️⃣",
 "5️⃣",
 "6️⃣",
 "7️⃣",
 "8️⃣",
 "9️⃣",
)
# Əkmə Oğlum...!!!
status = (
"𝐀𝐦𝐚 𝐚𝐫𝐭ı𝐤 𝐢𝐧𝐚𝐧𝐜ı𝐦 𝐲𝐨𝐤, 𝐧𝐞 𝐬𝐢𝐳𝐞 𝐧𝐞 𝐠ü𝐳𝐞𝐥 𝐠ü𝐧𝐥𝐞𝐫𝐞..’📌🕊",
"İ𝐤𝐢𝐧𝐜𝐢 ş𝐚𝐧𝐬𝐚 𝐠𝐞𝐫𝐞𝐤 𝐲𝐨𝐤, 𝐢𝐧𝐬𝐚𝐧𝐥𝐚𝐫 𝐚𝐬𝐥𝐚 𝐝𝐞𝐠𝐢ş𝐦𝐞𝐳..!",
"𝐌𝐞𝐬𝐚𝐟𝐞 𝐃𝐞𝐝𝐢𝐠‌𝐢𝐧 𝐍𝐞𝐝𝐢𝐫 𝐤𝐢 𝐁𝐢𝐳 𝐀𝐥𝐥𝐚𝐡𝐢 𝐆𝐨‌𝐫𝐦𝐞𝐝𝐞𝐧 𝐒𝐞𝐯𝐦𝐞𝐝𝐢𝐤 𝐌𝐢 🕊️",
"𝑲𝒖𝑺𝒖𝒓𝒂 𝑩𝒂𝒌𝒎𝒂 𝑨𝑵𝑵𝑬𝑴𝒊𝑵 𝑮𝒖‌𝒍𝒖‌𝒔‌𝒖‌ 𝑲𝒂𝒅𝒂𝒓 𝑮𝑼‌𝒁𝑬𝑳 𝑫𝒆𝒈‌𝒊𝒍𝒔𝒊𝒏 ♥️🕊️",
"𝑨𝒏𝒍𝒂𝒎𝒍𝜾 𝑺𝒐‌𝒛𝒍𝒆𝒓 𝒀𝒂𝒛𝒎𝒂𝒚𝒂 𝑮𝒆𝒓𝒆𝒌 𝒀𝒐𝒌. 𝑨𝒏𝒍𝒂𝒎𝒔𝜾𝒛 𝑩𝒊𝒓 𝑯𝒂𝒚𝒂𝒕 𝒀𝒂𝒔‌𝜾𝒚𝒐𝒓𝒌𝒆𝒏...🕊🖤",
"𝐓𝐞𝐥𝐚𝐟𝐢𝐬𝐢 𝐨𝐥𝐦𝐚𝐲𝐚𝐧 𝐬‌𝐞𝐲𝐥𝐞𝐫 𝐲𝐚𝐬‌𝐚𝐧𝐦𝐚𝐝ı 𝐛𝐞𝐧 𝐜‌𝐚𝐛𝐚𝐬ı𝐳𝐥𝛊𝐠‌ı𝐧𝐚 𝐤ı𝐫𝐠ı𝐧ı𝐦... 🥀🍷",
"𝑩𝒆𝒏 𝒈𝒐‌𝒏𝒍𝒖‌𝒎𝒖‌ 𝒔𝒂𝒏𝒂 𝒔𝒆𝒎𝒂𝒗𝒆𝒓 𝒚𝒂𝒑𝒕ı𝒎. 𝑺𝒆𝒏 𝒈𝒊𝒕𝒕𝒊𝒏 𝒔𝒂𝒍𝒍𝒂𝒎𝒂 𝒄‌𝒂𝒚𝒂 𝒔‌𝒆𝒌𝒆𝒓 𝒐𝒍𝒅𝒖𝒏😉",
"𝐇𝐚𝐭𝛊𝐫𝐥𝐚𝐝𝛊𝐧 𝐦𝛊 𝐁𝐞𝐧 𝐒𝐚𝐧𝐚 𝐇𝐚𝐲𝐚𝐥𝐥𝐞𝐫𝐢𝐦𝐢 𝐒𝐞𝐧 𝐁𝐚𝐧𝐚 𝐘𝐚𝐥𝐚𝐧𝐥𝐚𝐫𝛊𝐧𝛊 𝐀𝐧𝐥𝐚𝐭𝛊𝐫𝐝𝛊𝐧.. 🍂",
"𝗗𝘂‌𝗻𝘆𝗮𝗻𝗶𝗻 𝗗𝗲𝗿𝗱𝗶 𝗡𝗲𝗿𝗲𝘀𝗶𝗱𝗶𝗿 𝗕𝗶𝗹𝗺𝗲𝗺 𝗔𝗺𝗮 𝗗𝗲𝗿𝗺𝗮𝗻𝗶 “𝗔𝗡𝗡𝗘𝗠𝗜‌𝗡” 𝗗𝗶𝘇𝗹𝗲𝗿𝗶𝗻𝗱𝗲𝗱𝗶𝗿…🥀",
"𝑽𝒆𝒅𝒂𝒍𝒂𝒓, 𝒂𝒏𝒄𝒂𝒌 𝒈𝒖‌𝒛𝒆𝒍 𝒚𝒖‌𝒓𝒆𝒌𝒍𝒆𝒓𝒊 𝒂𝒄𝜾𝒕𝜾𝒓.🕊️",
"𝐒𝐮𝐬𝐦𝐮𝐬‌ 𝐛𝐢𝐫 𝐊𝐚𝐝𝛊𝐧 𝐢𝐜‌𝐢𝐧,𝐁𝐢𝐭𝐦𝐢𝐬‌ 𝐛𝐢𝐫 𝐀𝐝𝐚𝐦𝐬𝛊𝐧.🖤 kesinlikle👌",
"🕋꧁ঔ𝑳ə𝒃𝒃𝒆𝒚𝒌ə❤𝒚𝒂❤𝑯𝒖‌𝒔𝒆𝒚𝒏♥️﷽ℓฉ iℓฉhฉ ∞الله ∞ iℓℓฉ Аllah❤️",
"𝑨𝒈‌𝒂𝒄‌𝒅𝒂𝒏 𝒅𝒖‌𝒔‌𝒆𝒏 𝒚𝒂𝒑𝒓𝒂𝒌 𝒌𝒖𝒓𝒖𝒎𝒂𝒚𝒂, 𝒈𝒐‌𝒏𝒖‌𝒍𝒅𝒆𝒏 𝒅𝒖‌𝒔‌𝒆𝒏 𝒊𝒏𝒔𝒂𝒏 𝒅𝒂 𝒖𝒏𝒖𝒕𝒖𝒍𝒎𝒂𝒚𝒂 𝒎𝒂𝒉𝒌𝒖𝒎𝒅𝒖𝒓..",
"𝑻𝒆𝒌 𝑲𝜾𝒚𝒂𝒎𝒂𝒅𝜾𝒈‌𝜾𝒎 𝑽𝒂𝒓𝒅𝜾,𝑲𝒆𝒏𝒅𝒊 𝑲𝒆𝒏𝒅𝒊𝒏𝒊 𝑺𝒊𝒍𝒅𝒊🥂",
"𝐄𝐥ə 𝐁𝐢𝐫 𝐌𝐮𝐬𝐢𝐪𝐢𝐬ə𝐧 ♪ 𝐇ə𝐫 𝐍𝐨𝐭𝐮𝐧𝐝𝐚 𝐇ə𝐬𝐫ə𝐭 𝐕𝐚𝐫",
"‘‘𝑩𝒊𝒓 𝒅𝒖𝒂𝒎 𝒗𝒂𝒓, 𝒃𝒊𝒓𝒅𝒆 𝒅𝒖𝒚𝒂𝒏ı𝒎. 𝑮𝒆𝒓𝒊𝒔𝒊 𝒄𝒐𝒌𝒕𝒂 𝒎𝒖𝒉𝒊𝒎 𝒅𝒆𝒈𝒊𝒍’’🖤🥀",
"ẞ𝒆𝒏𝒅𝒆𝒏 𝒖𝒛𝒂𝒌 ẞ𝒊𝒓𝒚𝒆𝒓𝒅𝒆 𝑯𝒆𝒓 ş𝒆𝒚 𝒈𝒐‌𝒏𝒍𝒖‌𝒏𝒖‌𝒛𝒄𝒆 𝒐𝒍𝒔𝒖𝒏.🍷🖤",
"𝐎‌𝐲𝐥𝐞 𝐛𝐢𝐫 𝐌𝐚𝐡𝐤𝐞𝐦𝐞𝐲e 𝐂‌𝛊𝐤𝛊𝐜𝐚𝐳 𝐤𝐢 𝐇𝐚𝐤𝐢𝐦𝐢𝐧 𝐊𝐞𝐧𝐝𝐢𝐬𝐢 𝐒‌𝐚𝐡𝐢𝐭🥀🖤",
"✫𝙽𝚎 ç𝚘𝚡 ö𝚕𝚍ü𝚔 𝚋𝚒𝚛 𝚊𝚣 𝚢𝚊ș𝚊𝚖𝚊𝚚 üçü𝚗✫",
"𝑨𝒍𝒍𝒂𝒉 𝒈𝒆𝒕𝒅𝒊𝒚𝒊𝒏𝒊𝒛 𝒚𝒐𝒍𝒍𝒂𝒓ı 𝒅𝒐𝒈‌𝒓𝒖 𝒊𝒏𝒔𝒂𝒏𝒍𝒂𝒓𝒂 𝒄ı𝒙𝒂𝒓𝒔ı𝒏.🌘",
"𝖡𝖾𝗇 𝖻𝗂𝗅𝗂𝗋𝗂𝗆𝗄𝗂 𝖳𝖾𝗄 𝗒𝖺𝗋 𝖸𝖺𝗋𝖺𝖽𝖺𝗇𝖽ı𝗋 𝗀𝖾𝗋𝗂𝗌𝗂 𝗌𝖺𝖽𝖾𝖼𝖾 𝗒𝖺𝗋𝖺𝗅𝖺𝗒𝖺𝗇𝖽ı𝗋.🖤🩹",
"𝗲𝗴𝗲𝗿 𝗯𝗶𝗿 𝗴ü𝗻 𝘆𝗮𝗻ı𝗻𝗱𝗮 𝗸𝗶𝗺𝘀𝗲 𝗼𝗹𝗺𝗮𝘀𝗮 𝗕𝗶𝗿𝗮𝗸𝗱𝗶𝗴𝗶𝗻 𝘆𝗲𝗿𝗱ə 𝗼𝗹𝗮𝗰𝗮𝗺😏",
"𝑩𝒊𝒓 𝒊𝒏𝒔𝒂𝒏𝜾 𝒚𝒂𝒍𝒂𝒏𝒍𝒂𝒓𝒍𝒂 𝒌𝒂𝒛𝒂𝒏𝒎𝒂𝒌 𝒚𝒆𝒓𝒊𝒏𝒆 𝒅𝒐𝒈‌𝒓𝒖𝒍𝒂𝒓𝒍𝒂 𝒌𝒂𝒚𝒃𝒆𝒕𝒎𝒆𝒚𝒊 𝒕𝒆𝒓𝒄𝒊𝒉 𝒆𝒅𝒆rim",
"𝙆ı𝙯𝙙ı𝙣 𝙢ı 𝙛𝙖𝙡𝙖𝙣 𝙜𝙚𝙘̧𝙞𝙮𝙤𝙧 𝙙𝙖, 𝙎𝙤𝙜̆𝙪𝙙𝙪𝙣 𝙢𝙪 𝙘̧𝙖𝙧𝙚𝙨𝙞 𝙮𝙤𝙠..",
"• 𝑯𝒆𝒚𝒂𝒕 𝒈𝒐̈𝒛𝒆𝒍𝒅𝒊𝒓 𝒅𝒆𝒅𝒊 • 𝑪̧𝒂𝒚𝒌𝒐𝒗𝒔𝒌𝒊 ... • 𝑽𝒆 1 𝒊𝒍 𝒔𝒐𝒏𝒓𝒂 𝒐̈𝒛𝒖̈𝒏𝒖̈ 𝒂𝒔𝒅𝜾 ... 🥀",
"𝕙𝕒𝕥𝕒 𝕓𝕚𝕫𝕕𝕖❕ 𝕪𝕒𝕟𝕝𝕚𝕤 𝕚𝕟𝕤𝕒𝕟𝕝𝕒𝕣𝕒 𝕚𝕪𝕚 𝕜𝕚 𝕧𝕒𝕣𝕤𝕚𝕟 𝕕𝕖𝕕𝕚𝕜💔",
"𝒃𝒂𝒛𝒆𝒏 𝒔𝒂𝒅𝒆𝒄𝒆 𝒔𝒆𝒗𝒆𝒓𝒔𝒊𝒏 ö𝒕𝒆𝒔𝒊 𝒚𝒐𝒌..༗",
"º°”“𝙕𝙖𝙢𝙖𝙣 𝙖𝙠ı𝙥 𝙜𝙚ç𝙞𝙮𝙤𝙧. 𝙖𝙮𝙣ı 𝙮𝙚𝙧𝙙𝙚𝙨𝙞𝙣 𝙖𝙢𝙖 𝙖𝙮𝙣ı 𝙠𝙞ş𝙞 𝙙𝙚ğ𝙞𝙡𝙨𝙞𝙣.”♡●",
"𝓗𝓮𝓻𝓴𝓮𝓼 𝓴𝓪𝔂𝓫𝓮𝓽𝓽𝓲𝓰̆𝓲𝓷𝓮 𝔂𝓪𝓷𝓼𝓲𝓷 𝓼𝓮𝓷 𝓫𝓪𝓷𝓪 𝓫𝓮𝓷 𝔃𝓪𝓶𝓪𝓷𝓪 🥀",
"𝒃𝒊𝒛𝒊 𝒔𝒆𝒗𝒊𝒚𝒐𝒓𝒎𝒖𝒔̧ 𝒈𝒊𝒃𝒊 𝒚𝒂𝒑𝒂𝒏𝒂 𝒃𝒊𝒛𝒅𝒆 𝒊𝒏𝒂𝒏𝜾𝒚𝒐𝒓𝒎𝒖𝒔̧ 𝒈𝒊𝒃𝒊 𝒚𝒂𝒑𝒂𝒓𝜾𝒛 🕊️🥀",
"༆ 𝑯𝒂𝒚𝒂𝒕 𝑻𝒖̈𝒌𝒆𝒏𝒆𝒏 𝑩𝒊𝒓 𝒌𝒂𝒍𝒆𝒎𝒆 𝑻𝒖̈𝒌𝒆𝒏𝒎𝒆𝒛 𝑫𝒆𝒅𝒊𝒌𝒍𝒆𝒓𝒊 𝑲𝒂𝒅𝒂𝒓 𝒀𝒂𝒍𝒂𝒏 .. ༆🌹",
)
# Əkmə Oğlum...!!!
musiqi = (
"🎵 1. MegaBeatsZ - Darıxmışam Sənin Üçün Remix",
"🎵 2. Ulviyye Namazova-İlk Esqim ",
"🎵 3. İdo Tatlıses - Bileklerime Kadar Acıyo",
"🎵 4. Ezhel - Bul Beni ",
"🎵 5. CKay - Love Nwantiti Remix ft. Joeboy & Kuami Eugene Official Video",
"🎵 6. Farid Gasanov - Dolar Prod by. SarkhanBeats ",
"🎵 7. Murat Göğebakan - Vurgunum -  Official Video",
"🎵 8. Javid - Ruhumun Sesi official video",
"🎵 9. Tombul Tombul",
"🎵 10. ЛСП - Бэйби Remix ",
"🎵 11. Ece Mumay - Peri ",
"🎵 12. Eminem - Lose Yourself [HD]",
"🎵 13. Çətin - Sebine Celalzade cover Natavan Habibi 2021 ",
"🎵 14. Фанк",
"🎵 15. Murat Dalkilic feat. Boygar - Leyla",
"🎵 16. Rübabə Muradova-Unuda Bilmirəm ",
"🎵 17. Talıb Tale - Ola Xəbəri 2018 full_HD_Music ",
"🎵 18. İlkin Abbasov ft.Lila - Travma ",
"🎵 19. ЛСП & Oxxxymiron - Безумие Remix ",
"🎵 20. Retro - Lənət qadın Official Music Video ",
"🎵 21. Sezen Aksu - Küçüğüm Lyrics | Şarkı Sözleri ",
"🎵 22. Miyagi & Эндшпиль feat. Рем Дигга - I Got Love Official Video",
"🎵 23. Gorillaz - Clint Eastwood Official Video ",
"🎵 24. BoyWithUke - Toxic Lyrics ",
"🎵 25. Kore Klip - Inanirim ",
"🎵 26. Elsevər Rahimov - Sən Olmayan ",
"🎵 27. Rauf Faik - детство Official audio",
"🎵 28. Ufuk Beydemir - Ay Tenli Kadın",
"🎵 29. Kurtuluş Kuş & Burak Bulut - Baba Yak",
"🎵 30. Athena - Kafama Göre ",
"🎵 1. Непара - Другая семья официальный клип ",
"🎵 2. XXXTENTACION - Hope ",
"🎵 3. Nuri Serinlendirici & Jane - HEYATIMA XOS GELDIN ",
"🎵 4. Иракли   Лондон   Париж ",
"🎵 5. INSTASAMKA - Juicy Премьера клипа, 2021, prod. realmoneyken ",
"🎵 6. İrem Derici - Acemi Balık ",
"🎵 7. İrem Derici - Acemi Balık ",
"🎵 8. Retro Video Club - Chemistry Official Video ",
"🎵 9. Night In ",
"🎵 10. The Cult - Brother Wolf; Sister Moon ",
)
# Əkmə Oğlum...!!!
ad = (
 "Şirin💞",
 "Dəcəl👀",
 "Əsəbi🤨",
 "Qorxulu😠",
 "Vəhşi😡",
 "Pişiy😺",
 "Ceyran🦌",
 "Nəfəs🌬️",
 "Ömür😍",
 "Bal🍯",
 "Ürəy❤️",
 "Evli💍",
 "Dəli😉",
 "Flamingo🦩",
 "Tosbik 🐢 ",
 "Dino 🦖",
 "Kermit🐸",
 "Subay😜",
 "Sərxoş🥴",
 "Kəpənəy🦋",
 "Arı🐝",
 "Balıq🐠",
 "Sevimli😌",
 "Sehirbaz🎩",
 "Alim🎓",
 "Kral👑",
 "Gözəl💄",
 "Çirkin😒",
 "Meymun🙈",
 "Mələy😇",
 "Dovşan🐰",
 "Maral🦌",
 "Ulduz⭐",
 "Günəş🌅",
 "Vor📿",
 "Qıcıq😈",
 "Varlı💵",
 "Almaz💎",
 "Gül🌺",
 "Qızılgül🌹",
 "Bikef🙄",
 "Xəstə🤒",
 "UFO🛸",
 "Şanslı🔮",
 "Avara🚬",
 "Futbolçu⚽",
 "Müğənni🎤",
 "A.Y.E🤘",
 "Qız♀️",
 "Oğlan♂️",
 "Gecə🌃",
 "Cücə🐥",
 "DON🕴️",
 "Məşuqə💃",
 "Gəlin👰",
 "Bəy🤵",
 "Covid19😷",
 "Joker🤡",
 "Ağıllı🧠",
 "Qardaş✊",
 "Saturn🪐",
 "Pullu🤑",
 "Susqun🤐",
 "Nevroz😤",
 "Güclü💪",
 "Virus🦠",
 "Usta👷",
 "Əsgər💂",
 "Üzgüçü🏊",
 "İdmançı🏋️",
 "Tülkü🦊",
 "Supermen🦸",
 "Zombi🧟",
 "Cin🧞",
 "Bəstəkar🎼",
 "Çiyələk🍓",
 "Nərgiz🌼",
 "Robot🤖",
 "İlan🐍",
 "Bahar💮",
 "Yazar✍️",
 "Payız🍂",
 "Qar❄️",
 "Qasırğa🌀",
 "Kaktus🌵"
 "Mesaj💌",
 "Vulkan🌋",
 "Pizza🍕",
 "Nənə🧓",
 "Soyuq🥶",
 "Dino🦕",
 "Ay🌙",
 "Günəbaxan🌻",
 "🛸Plutonium",
 "🪐Neptune",
 "🌀Uranus",
 "🍂Saturn",
 "💫Jupiter",
 "🌑Mars",
 "🌍Earth",
 "🌪️Venus",
 "☄️Mercury",
 "☀Sun",
 "⭐General",
 "Meteor☄️",
 "Hicablı🧕",
 "Gözəl💅",
 "Alpen🍫",
 "Kofe☕",
 "Mişka🧸",
 "Alp🏔️",
 "Pubg🎮",
 "Popcorn🍿",
 "Qartal🦅",
 "Bozqurd🐺",
 "Rəssam🎨",
 "Panda🐼",
 "Aslan🦁",
)
# Əkmə Oğlum...!!!
emj = ['😇','🥰','😎','🤩','😍','👾','🤡','🥳','😻','😼','😽','💋','👸','🤴','🎅🏻','🤶','🧞‍♀️','🧞','🧞‍♂️','🧜‍♀️','🧜','🧚‍♀️','🧚','👑','💍','🕶','🐶','🐱','🐭','🐹','🐰','🦊','🐻','🐼','🐨','🐯','🦁','🐮','🐷','🐽','🐸','🐵','🙈','🙉','🙊','🐒','🐣','🐥','🦅','🐝','🦋','🐞','💐','🌹','🥀','🌺','🌸','🌼','🌻','⭐️','🌟','✨','⚡️','🔥','🌈','☃️','🍫','💅','🐺','🍫','🍕','☕','🧸','🦅','👩‍🦰','🎮','☄️','🌙','🦕','👨🏻‍✈️','🥶','🍿','👀','💀','💟','♥️','💘','💝','💗','💙','💛','🖤','🤑','⚡','😈','🤡','🎊','🔥','😼','💤','✊','👩‍🎨','🧕','🌼','💐','🌹','🥀','🌷','🌺','🌸','🏵️','🌻','🍂','🍁','🌾','🌱','🌿','🍃','☘️','🍀','🌵','🌴','🌳','🌲','🏞️','🌪️','☃️','⛄','❄️','🏔️','🌋','🙋','🤶','👩‍💼','🧓','🧔','💃','🕺','👩‍🦰','🪐','🦄','🐢','🐁','🐤','🐣','🐥','🦉','🐓','🕊️','🦢','🦩','🦈','🐬','🐋','🐳','🐟','🐠','🦚','🐡','🦐','🦞','🦀','🦑','🐙','🦂','🕷️','🕸️','🐜','🦗','🦟','🐝','🐞','🐾','🍓','🍒','🍎','🍉','🍊','🥭','🍍','🍋','🍇','🥝','🍐','🥥','🌶️','🍄','🍔','🧆','🥙','🦞','🍧','🍨','🍦','🥧','🍰','🍮','🎂','🧁','🍭','🍬','🍩','🍺','🍻','🥂','🍾','🍷']
# Əkmə Oğlum...!!!
cumle = (
 "Hayat yalansa gerçek sen ol!",
 "Biz insanların insan olanlarını severiz!",
 "İlahi Azrail, sen adamı öldürürsün.",
 "Dışarıda mucize arama, mucize sensin.",
 "Keşke seni kopyalayıp yanıma yapıştırabilsem…",
 "Son gülen sen olacaksın, çünkü geç anlıyorsun.",
 "Oğlumun adını mafya koydum, artık bir mafya babasıyım.",
 "Bir qızın ən şirin halı, ağlarkən gülməyə çalışanda ortaya çıxan üz ifadəsidir",
"Ya tutulacaq qədər yaxın ol, yada unudulacaq qədər uzaq...",
"Sənə Çox insan, 'Səni Sevirem' deyər... Ama Sadəcə biri Səni Gəlinliklə görmək isdər ...!",
"Gecə mesajlaşarkən sms-in ən şirin yerində,sizi qoyub öküz kimi yatan insana sevgili deyilir :D",
"Bir cümlə ilə xoşbəxtliyimi məhv edən xoşbəxt ol dedi ",
"Göy qurşağinin bitdiyi yerdə bir xəzinə var deyirler. Bir gün təqib etdim, bitdiyi yerdə sən vardın.!",
"Sevgi vaxtsiz gələn qonağın uşağı kimidir... Gələr dağıdar və gedər, səsini belə çıxara bilməzsən..."
"İnsan odun deyil ki, qırıldığı zaman səs çıxartsın... Səssiz-səmirsiz də qırılır bəzən...",
"🤖UserBot: Mesajlar uzun olduğu üçün hər istifadəçini 3 saniyə intervalı ilə tağ edirəm",
"Bir mənə bax görüm",
"Bir mənə bax görüm",
"Bir mənə bax görüm",
"Bir mənə bax görüm",
"Kiməm mən ?",
"Bayaqdan səni gözləyirəme mən 🙄",
"Bayaqdan səni gözləyirəme mən 🙄",
"Bayaqdan səni gözləyirəme mən 🙄",
"Bayaqdan səni gözləyirəme mən 🙄",
"Bayaqdan səni gözləyirəme mən 🙄",
"Bayaqdan səni gözləyirəme mən 🙄",
"Hardasanki sən ?",
"Mənə lazımdı bircədəfə görüm onu fsoo getdi ömrümün axrınacan",
"Bağlanmıyın a kişi kiməsə bax adamın burası ağrıyır",
"Bağlanmıyın a kişi kiməsə bax adamın burası ağrıyır",
"Salam",
"Necəsən",
"Salam necəsən ?",
"Gəl gəl görəy 😐",
"Təzə maşın almışam",
"Gəl desəm gələrsən ?",
"Gəl desəm gələrsən ?",
"Gəl desəm gələrsən ?",
"Gəl desəm gələrsən ?",
"Gəl desəm gələrsən ?",
"Gəl desəm gələrsən ?",
"bir iki adam var danisim gedirem",
"Xoş gəldin 🍾",
"Səhvlərdən yalnızca heç bir şey etməyən kəslər yayına bilər. Səhv etməkdən qorxmayın, səhvi təkrarlamaqdan qorxun.- Teodor Ruzvelt.",   
 "Böyük işi görə bilmənin yalnızca bir üsulu var- o işi sevməniz. - Stiv Cobs.   ",
  "Tırtılın həyatın sonu adlandırdığını ustad kəpənək adlandırır. - Riçard Bax.   ",
 "Xəyallarınızın arxasınca yürüməyin, onları təqib edin. - Riçard Damb.   ",
 "Uğurun asılı olduğu yeganə şərt səbrdir. - Lev Tolstoy.   ",
 "İnsanlarla düzgün rəftar, uğurun ən başlıca üsuludur. - Teodor Ruzvelt.   ",
  "Bəxtəvər insan o insandır ki, başqalarının hələ etməyə hazırlaşdığı işi o artıq həyata keçirmişdir.  ",
 "Hərəkətlər hər zaman xoşbəxtlik gətirmir, lakin onlar olmasa xoşbəxtlik heç olmaz. - Benjamin Dizraeli.   ",
 "Ən yaxşı motivasiya daxildən gəlir. - Maykl Jonson.   ",
 "Hər bir arzu sizlərə onu həyata keçirməkdə yardımcı olacaq qüvvələrlə verilir. - Riçard Bax.","Min mil ölçüsündə olan yol sadəcə bir addımla başlayır. - Lao Szı.   ",
 "Xoşbəxt olmaq qabiliyyəti elə özümüzdən asılıdır. - Şarlotta Bronte.",
   " Mən şəxsən çiyələklə qaymaq yeməyi sevirəm. Amma balıqlar qurd sevir. Ona görə də balıq tutmağa gedəndə mən öz sevdiyim yemək haqda deyil, balığın sevdiyi yemək haqda düşünürəm. Deyl Karnegi",
" Mənim çıxartdığım və hər zaman əməl etdiyim bir dərs var, cəhd etmək, cəhd etmək, yenə də cəhd etmək! Və heç vaxt təslim olmamaq! Riçard Brenson",
" Mən məğlubiyyətlərə dözmürdüm. Mən sadəcə 10 min yol tapırdım, hansılar ki, heç vaxt işləmirdi. Tomas Edison",
 "Mən bunu istəyirəmsə, deməli bu olacaq. Henri Ford",
"Bədbəxt, uğursuz, xoşbəxt və sağlam olmayan o adamdır ki, o tez-tez sabah sözünü işlədir. Robert Kiyosaki",
"Bizim ən böyük çatışmazlığımız ondadır ki, biz çox tez vaz keçirik. Uğura gedən yol yenidən cəhd etməkdən keçir. Tomas Edison",
" Həyatda bir dəfə bəxt insanın qapısını döyür, amma insan həmin vaxtı yaxınlıqdakı pivəxanada oturur və heç bir qapı səsi eşitmir. Mark Tven",
"Optimist bir insan ayaqqabıları oğurlanınca ayaqlarım var dəyə bilən insandır. Sokrat",
 "Kişilər qadınların ilk eşqi, qadınlar kişilərin son eşqi olmaq istər. Oskar Vayld",
 "Mal itirən bir şey itirmişdir, qürurunu itirən bir çox şey itirmişdir, lakin cəsarətini itirən hər şeyini itirmişdir. Höte",
"Çətinlikləri qarşılamanın iki yolu vardır; ya çətinlikləri dəyişdirərsiniz, ya da çətinlikləri həll etmək üçün özünüzü. Filis Botom.",
"Heç bir şey insan qədər yüksələ bilməz və onun qədər də alçala bilməz. Fridrix Holderlin",
"Müvəffəqiyyətin dörd şərti; bilmək, istəmək, cəsarət etmək və susmaq. Aksel Munte",
"Kiçik xərcləmələri gözdən qaçırmayın. Bəzən kiçik bir dəlik böyük bir gəmini batırar. Benjamin Franklin",
 "Düşmənlərinizi sevin, çünki qüsurlarınızı tək onlar açıqca söyləyə bilər. Benjamin Franklin",
 "Həyat o qədər qısadır ki, kiməsə nifrət edərək vaxt itirmə. Anonim",
"Keçmişinlə barış ki, gələcəyini zəhərə döndərməsin. Anonim",
"Həyatını başqalarının həyatı ilə müqayisə etmə. Hansı şərtlər altında bura gəlib çıxdıqlarını bilmirsən. Anonim",
"Həyatda nəyə marağın varsa, arxasınca getməli və bu yolda “yox” sözünü bir cavab olaraq qəbul etməməlisən. Anonim",
 "Xəstə olanda işin sənə baxmayacaq, dostların baxacaq. Əlaqələri kəsmə, dostlarına vaxt ayır. Anonim",
 "Unutma, səni öldürməyən şey, səni daha da güclü edir. Anonim",
 "Həyatı çox sorğu-sual etmə, hərəkətə keç və lazım olanı indi et. Anonim",
" Həyatda nəyə marağın varsa, arxasınca getməli və bu yolda “yox” sözünü bir cavab olaraq qəbul etməməlisən. Anonim",
 "Gözəl bağlanmış qutuda olmasa da, həyat yenə də bir hədiyyədir. Anonim",
 "Nəyəsə nail olacaqsan, yalnız taleyə müqavimət göstərərək…",
"Ola bilər ki, axın səni düşündüyün yerə aparmayacaq.",
"Əgər atdığın addım sənə çətindirsə, o zaman düşün və cavabla. Bu addımı atmağa ehtiyac duyursanmı?",
"Növbəti dəfə ya yaxşısını et, ya da başqa cür.",
"Əgər zaman, məkan, insanlar və hərəkət istiqaməti düzgün seçilməyibsə və nəticədə heç nə alınmırsa, təəccüblənmə.",
"Əgər sən öz səhvinin nəticələrini düzəldə bilirsənsə, demək ki, hələ səhv etməmisən.",
"Əgər sən büdrədinsə və yıxıldınsa, bu o demək deyil ki, sən ora getmirsən.",
"Yol yalnız hamar yerlərdən keçə bilməz.",
"Yolun eyni olan insanın arxasıyca get.",
"Sənin səhvlərin dünyanı dağıtmayacaq.",
"Özün üçün qorxma. Nahaqdan itməyə görə dünya üçün çox dəyərlisən.",
"Nə baş verirsə, vaxtında baş verir.",
"Nə baş verəcəksə, sənin həyatının yaxınlığında baş verəcək.",
"Ümidin sevincli hissləri üçün qaçırdılmış imkanlara təşəkkür et.",
"Dünyaya sənin xeyrin deyil, iştirakın lazımdır.",
"Əgər lazımdırsa əziyyət çək, amma öz əzablarını bu ehtiyaca görə doğrultma.",
"Asanmış kimi davran, bu zaman sənə daha asan görünəcək.",
"Sevinc az oldu deyə kədərlənmə: bununla sən sevincini kədərə çevirəcəksən.",
"Dadmağın və doymağın öz sevinci var. Bunları qarışdırma.",
"Arzu etmək olar ki, külək yox olsun. Arzu etmək olmaz ki, külək həmişəlik yox olsun.",
"Vaxtaşırı kimisə sevindir, heç olmasa özünü…",
"Harmoniya məqsəd deyil, vasitədir. Əgər sən onunla nə etməli olduğunu bilsən, onu tapacaqsan.",
"Pis heçnə yoxdur. Sənin xoşuna gəlməyən var.",
"Bəzən düzgün qərarın axtarışı səhvlərdən daha çətin keçir.",
"Çox deməkdən qorxma. Məgər sən nə dərəcədə demək lazım olduğunu bilmirsən?",
"Məqsədimiz mümkünsüzü mümkün etmək, mümkünü asan etmək, asanı da zərif və zövqlü etmənin yollarını tapmaqdır. Dr.Feldenkrais",
"Kifayət qədər səbəbiniz varsa, hər şeyi edə bilərsiniz. Jim Rohn",
"Həyatdan qorxmayın uşaqlar; yaxşı və doğru bir şeylər etdiyiniz zaman həyat elə gözəl ki! Dostoyevski",
"İnsanoğlunun içində yatan güclər vardır; özü bilsə çaşar. Çünki bu güclərə sahib olduğu ağılından belə keçməz. Bu gücləri oyandırıb hərəkətə keçirə bilən adamın həyatında böyük bir inqilab olar. Swett Marden",
"Möhtəşəm şeylər, ancaq içlərindəki bir şeyin, şərtlərin üzərində olduğuna inanma cəsarətini göstərənlər tərəfindən edilmişdir. Bruce Barton",
"Həyat bir velosipedə minmək kimidir. Pedalı fırlatmağa davam etdiyiniz müddətcə yıxılmazsınız.  Claude Pepper",
"Ümidlə yol getmək gediləcək yerə çatmaqdan daha gözəldir. Louis Stevenson",
"Bir işi doğru etmək, nə üçün yalnış etdiyini izah etməkdən daha az zaman aparır.  Henry Wodsworth",
"Dualarınıza diqqət edin. Həyata keçə bilər. Emerson",
"Məşğul ol, didin, düşün, axtar, tap, qaç. Dayanmaq zamanı keçdi çalışmaq zamanıdır. Tofiq Fikrət",
"Statistika nə deyir desin, hər vəziyyətdə müvəffəqiyyətə gedən bir yol vardır. Bemard Segeln",
"İnsana olanlar deyil, insanın içində olanlar əhəmiyyətlidir. Louis Mann",
"Mənfi düşünən adam, çiy bir yumurtanı bütün halda qabığıyla udmuş ​​bir adama bənzəyir. Yumurtanın qırılacağı qorxusuyla hərəkət edə bilməz, cücə çıxacağı qorxusuyla da hərəkətsiz dayana bilməz. Rus Atalar sözü",
"Yalnız işsiz olanların deyil, daha yaxşısını edə biləcək, amma etməyənlərin də başı boşdur. Sokrates",
"Batan günəş üçün ağlamayın; yenidən doğulduğunda nə edəcəyinizə qərar verin. Dale Camegie",
)

    
# Adlarla Tağ
@aykhan(outgoing=True, pattern="^.adtag.*")
async def adtag(event):
      if event.fwd_from or FlagContainer.is_active:
          return
      try:
          FlagContainer.is_active = True
  
          sozad = None
          aykhan1 = event.message.text.split(" ", 1)
          if len(aykhan1) > 1:
              sozad = aykhan1[1]
  
          chat = await event.get_input_chat()
          await event.edit("❤️ **Adlarla Tağ Başladı**\n⏱️ **İnterval** - 1 saniyə\n👤 **User sayı** - 5")
  
          tags = list(map(lambda m: f"[{random.choice(ad)}](tg://user?id={m.id})", await event.client.get_participants(chat)))
          current_pack = []
          async for participant in event.client.iter_participants(chat):
              if not FlagContainer.is_active:
                  break
  
              current_pack.append(participant)
  
              if len(current_pack) == 5: 
                  tags = list(map(lambda m: f"[{random.choice(ad)}](tg://user?id={m.id})", current_pack))
                  current_pack = []
  
                  if sozad:
                      tags.append(sozad)
  
                  await event.client.send_message(event.chat_id, " ".join(tags))
                  await asyncio.sleep(1) 
      finally:
          FlagContainer.is_active = False
          
 # Rənglərlə Tağ 
@aykhan(outgoing=True, pattern="^.rgtag.*")
async def rgtag(event):
      if event.fwd_from or FlagContainer.is_active:
          return
      try:
          FlagContainer.is_active = True
  
          sozreng = None
          aykhan2 = event.message.text.split(" ", 1)
          if len(aykhan2) > 1:
              soz = aykhan2[1]
  
          chat = await event.get_input_chat()
          await event.edit("❤️ **Rənglərlə Tağ Başladı**\n⏱️ **İnterval** - 0.5 saniyə\n👤 **User sayı** - 4")
  
          tags = list(map(lambda m: f"[{random.choice(reng)}](tg://user?id={m.id})", await event.client.get_participants(chat)))
          current_pack = []
          async for participant in event.client.iter_participants(chat):
              if not FlagContainer.is_active:
                  break
  
              current_pack.append(participant)
  
              if len(current_pack) == 4: 
                  tags = list(map(lambda m: f"[{random.choice(reng)}](tg://user?id={m.id})", current_pack))
                  current_pack = []
  
                  if sozreng:
                      tags.append(sozreng)
  
                  await event.client.send_message(event.chat_id, " ".join(tags))
                  await asyncio.sleep(0.5) 
      finally:
          FlagContainer.is_active = False
 # Rəqəmlərlə Tağ 
@aykhan(outgoing=True, pattern="^.rqtag.*")
async def rqtag(event):
      if event.fwd_from or FlagContainer.is_active:
          return
      try:
          FlagContainer.is_active = True
  
          sozreq = None
          aykhan3 = event.message.text.split(" ", 1)
          if len(aykhan3) > 1:
              sozreq = aykhan3[1]
  
          chat = await event.get_input_chat()
          await event.edit("❤️ **Rəqəmlərlə Tağ Başladı**\n⏱️ **İnterval** - 0.5 saniyə\n👤 **User sayı** - 3")
  
          tags = list(map(lambda m: f"[{random.choice(reqem)}](tg://user?id={m.id})", await event.client.get_participants(chat)))
          current_pack = []
          async for participant in event.client.iter_participants(chat):
              if not FlagContainer.is_active:
                  break
  
              current_pack.append(participant)
  
              if len(current_pack) == 3: 
                  tags = list(map(lambda m: f"[{random.choice(reqem)}](tg://user?id={m.id})", current_pack))
                  current_pack = []
  
                  if sozreq:
                      tags.append(sozreq)
  
                  await event.client.send_message(event.chat_id, " ".join(tags))
                  await asyncio.sleep(0.5) 
      finally:
          FlagContainer.is_active = False
          
 # Emojilərlə Tağ 
@aykhan(outgoing=True, pattern="^.emtag.*")
async def emtag(event):
      if event.fwd_from or FlagContainer.is_active:
          return
      try:
          FlagContainer.is_active = True
  
          sozemj = None
          aykhan4 = event.message.text.split(" ", 1)
          if len(aykhan4) > 1:
              sozemj = aykhan4[1]
  
          chat = await event.get_input_chat()
          await event.edit("❤️ **Emoji Tağ Başladı**\n⏱️ **İnterval** - 0.5 saniyə\n👤 **User sayı** - 5")
  
          tags = list(map(lambda m: f"[{random.choice(emj)}](tg://user?id={m.id})", await event.client.get_participants(chat)))
          current_pack = []
          async for participant in event.client.iter_participants(chat):
              if not FlagContainer.is_active:
                  break
  
              current_pack.append(participant)
  
              if len(current_pack) == 5: 
                  tags = list(map(lambda m: f"[{random.choice(emj)}](tg://user?id={m.id})", current_pack))
                  current_pack = []
  
                  if sozemj:
                      tags.append(sozemj)
  
                  await event.client.send_message(event.chat_id, " ".join(tags))
                  await asyncio.sleep(0.5) 
      finally:
          FlagContainer.is_active = False
  # Cümlələrlə Tağ 
@aykhan(outgoing=True, pattern="^.ctag.*")
async def ctag(event):
      if event.fwd_from or FlagContainer.is_active:
          return
      try:
          FlagContainer.is_active = True
  
          sozcm = None
          aykhan5 = event.message.text.split(" ", 1)
          if len(aykhan5) > 1:
              sozcm = aykhan5[1]
  
          chat = await event.get_input_chat()
          await event.edit("❤️ **Cümlələrlə Tağ Başladı**\n⏱️ **İnterval** - 3 saniyə\n👤 **User sayı** - 1")
  
          tags = list(map(lambda m: f"[{random.choice(cumle)}](tg://user?id={m.id})", await event.client.get_participants(chat)))
          current_pack = []
          async for participant in event.client.iter_participants(chat):
              if not FlagContainer.is_active:
                  break
  
              current_pack.append(participant)
  
              if len(current_pack) == 1: 
                  tags = list(map(lambda m: f"[{random.choice(cumle)}](tg://user?id={m.id})", current_pack))
                  current_pack = []
  
                  if sozcm:
                      tags.append(sozcm)
  
                  await event.client.send_message(event.chat_id, " ".join(tags))
                  await asyncio.sleep(3) 
      finally:
          FlagContainer.is_active = False

# Muisiqi Tağ
@aykhan(outgoing=True, pattern="^.mtag.*")
async def mtag(event):
      if event.fwd_from or FlagContainer.is_active:
          return
      try:
          FlagContainer.is_active = True
  
          sozmus = None
          aykhan6 = event.message.text.split(" ", 1)
          if len(aykhan6) > 1:
              sozmus = aykhan6[1]
  
          chat = await event.get_input_chat()
          await event.edit("❤️ **Musiqi Adlarıyla Tağ Başladı**\n⏱️ **İnterval** - 3 saniyə\n👤 **User sayı** - 1")
  
          tags = list(map(lambda m: f"[{random.choice(musiqi)}](tg://user?id={m.id})", await event.client.get_participants(chat)))
          current_pack = []
          async for participant in event.client.iter_participants(chat):
              if not FlagContainer.is_active:
                  break
  
              current_pack.append(participant)
  
              if len(current_pack) == 1: 
                  tags = list(map(lambda m: f"[{random.choice(musiqi)}](tg://user?id={m.id})", current_pack))
                  current_pack = []
  
                  if sozmus:
                      tags.append(sozmus)
  
                  await event.client.send_message(event.chat_id, " ".join(tags))
                  await asyncio.sleep(3) 
      finally:
          FlagContainer.is_active = False
          
# Statuslarla Tağ
@aykhan(outgoing=True, pattern="^.stag.*")
async def stag(event):
      if event.fwd_from or FlagContainer.is_active:
          return
      try:
          FlagContainer.is_active = True
  
          sozsts = None
          aykhan7 = event.message.text.split(" ", 1)
          if len(aykhan7) > 1:
              sozsts = aykhan7[1]
  
          chat = await event.get_input_chat()
          await event.edit("❤️ **Status Mesajlarıyla Tağ Başladı**\n⏱️ **İnterval** - 3 saniyə\n👤 **User sayı** - 1")
  
          tags = list(map(lambda m: f"[{random.choice(status)}](tg://user?id={m.id})", await event.client.get_participants(chat)))
          current_pack = []
          async for participant in event.client.iter_participants(chat):
              if not FlagContainer.is_active:
                  break
  
              current_pack.append(participant)
  
              if len(current_pack) == 1: 
                  tags = list(map(lambda m: f"[{random.choice(status)}](tg://user?id={m.id})", current_pack))
                  current_pack = []
  
                  if sozsts:
                      tags.append(sozsts)
  
                  await event.client.send_message(event.chat_id, " ".join(tags))
                  await asyncio.sleep(3) 
      finally:
          FlagContainer.is_active = False

# Stop (Tağ Dayandırmaq)
@aykhan(outgoing=True, pattern="^.stp")
async def restart(event):
    await event.edit("⛔ **Tağ prosesi dayandırıldı**")
    if BOTLOG:
        await event.client.send_message(BOTLOG_CHATID, "⛔ **Tağ prosesi dayandırıldı**\n"
                                        )

    try:
        await bot.disconnect()
    except:
        pass

    execl(sys.executable, sys.executable, *sys.argv)
# Əkmə oğul...!!!
CmdHelp('tagger').add_command(
    'mtag', '<Mesajınız>', ' Musiqi adlarıyla tağ edir'
).add_command(
    'adtag', '<Mesajınız>', ' Dəyişiy adlarla tağ edir'
).add_command(
    'stag', '<Mesajınız>', ' Status mesajlarıyla tağ edir'
).add_command(
    'rgtag', '<Mesajınız>', ' Rəngli tağ edir'
).add_command(
    'rqtag', '<Mesajınız>', ' Rəqəmlərlə tağ edir'
).add_command(
    'emtag', '<Mesajınız>', ' Emojilərlə tağ edir'
).add_command(
    'ctag', '<Mesajınız>', ' Cümlələrlə və maraqlı sözlərlə tək tək tağ edir'
).add_command(
    'stp', None, '⛔Aktiv tağ prosesini dayandırır\n\n👨🏻‍💻Sahib - @aykhan_s\n📣 Rəsmi Kanal - @RoBotlarimTg'
).add()
