class script(object):
    START_TXT = """<blockquote>Hello {},</blockquote>

<i>➤ Just add me to your group as an admin.  
➤ I’ll automatically respond with movies when someone searches.</i>

<b>⚡Powered by ➤ <i><a href=https://t.me/UrvashiTheaters_Main>©𝐓𝐞𝐚𝐦 𝐔𝐫𝐯𝐚𝐬𝐡𝐢 𝐓𝐡𝐞𝐚𝐭𝐞𝐫𝐬™️</a></i></b>"""

    JOIN_TXT = """📢If you want to get the movie you asked for, you need to join both the channels given below. Please join first.\n\n📢നിങ്ങൾ ചോദിച്ചു സിനിമ ലഭിക്കണമെങ്കിൽ താഴെ നൽകിയിരിക്കുന്ന രണ്ട് ചാനലുകളിലും ജോയിൻ ചെയ്യേണ്ടതുണ്ട്.. ദയവായി ആദ്യം ജോയിൻ ചെയ്യുക.\n\nNB🚸 : ആദ്യത്തെ ചാനലിൽ ജോയിൻ ചെയ്ത് 2 Sec കഴിഞ്ഞ് രണ്ടാമത്തെ ചാനലിൽ ജോയിൻ ചെയ്യുക"""
    
    STATUS_TXT = """★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>
★ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱
★ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱"""
    STATUS_TXT2 = """📂 𝖳𝗈𝗍𝖺𝗅 𝖥𝗂𝗅𝖾𝗌     - <code>{}</code>

𒆜  𝗗𝗕 1️⃣
╭ ▸ 𝖳𝗈𝗍𝖺𝗅 𝖥𝗂𝗅𝖾𝗌 : <code>{}</code>
├ ▸ 𝖴𝗌𝖾𝖽 𝖲𝗍𝗈𝗋𝖺𝗀𝖾: <code>{}</code>MB
╰ ▸ 𝖥𝗋𝖾𝖾 𝖲𝗍𝗈𝗋𝖺𝗀𝖾    - <code>{}</code>MB

𒆜 𝗗𝗕 2️⃣
╭ ▸ 𝖳𝗈𝗍𝖺𝗅 𝖥𝗂𝗅𝖾𝗌 : <code>{}</code>
├ ▸ 𝖴𝗌𝖾𝖽 𝖲𝗍𝗈𝗋𝖺𝗀𝖾: <code>{}</code>MB
╰ ▸ 𝖥𝗋𝖾𝖾 𝖲𝗍𝗈𝗋𝖺𝗀𝖾    - <code>{}</code>MB

𒆜 𝗗𝗕 3️⃣
╭ ▸ 𝖴𝗌𝖾𝗋𝗌 : <code>{}</code>
├ ▸ 𝖢𝗁𝖺𝗍𝗌 : <code>{}</code>
├ ▸ 𝖴𝗌𝖾𝖽 𝖲𝗍𝗈𝗋𝖺𝗀𝖾 : <code>{}</code>MB
╰ ▸ 𝖥𝗋𝖾𝖾 𝖲𝗍𝗈𝗋𝖺𝗀𝖾 : <code>{}</code>MB"""
    
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""


    MOVDOW_TXT = """<b> 1. 𝐑𝐞𝐪𝐮𝐞𝐬𝐭 𝐌𝐨𝐯𝐢𝐞𝐬 𝐆𝐫𝐨𝐮𝐩 - 𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞

2. 𝖱𝖾𝗊𝗎𝖾𝗌𝗍 𝖢𝗈𝗋𝗋𝖾𝖼𝗍 𝖲𝗉𝖾𝗅𝗅𝗂𝗇𝗀 𝖨𝗇 𝖤𝗇𝗀𝗅𝗂𝗌𝗁 𝖫𝖾𝗍𝗍𝖾𝗋𝗌. 𝖬𝗎𝗌𝗍 𝖥𝗈𝗅𝗅𝗈𝗐𝗂𝗇𝗀 𝖧𝗈𝗐 𝖳𝗈 𝖱𝖾𝗊𝗎𝖾𝗌𝗍 ⚙

3. 𝖸𝗈𝗎 𝖢𝖺𝗇 𝖢𝗅𝗂𝖼𝗄 𝖮𝗇 𝖳𝗁𝖾 𝖬𝗈𝗏𝗂𝖾 𝖡𝗎𝗍𝗍𝗈𝗇 𝖥𝗂𝗅𝖾𝗌 𝖨𝗇 𝖳𝗁𝖾 𝖰𝗎𝖺𝗅𝗂𝗍𝗒 𝖸𝗈𝗎 𝖶𝖺𝗇𝗍 𝖨𝗇 𝖬𝗒 𝖬𝖾𝗌𝗌𝖺𝗀𝖾 𝖳𝗁𝖺𝗍 𝖢𝗈𝗆𝖾𝗌 𝖠𝗌 𝖠 𝖱𝖾𝗉𝗅𝗒 𝖳𝗈 𝖳𝗁𝖾 𝗆𝗈𝗏𝗂𝖾 𝖸𝗈𝗎 𝖱𝖾𝗊𝗎𝖾𝗌𝗍𝖾𝖽🎯

4. 𝖳𝗁𝖾𝗇 𝖢𝗅𝗂𝖼𝗄 𝖲𝗍𝖺𝗋𝗍 𝖡𝖾𝗅𝗈𝗐 𝖮𝗋 𝖠𝗎𝗍𝗈 𝖲𝗍𝖺𝗋𝗍. 𝖥𝗂𝗇𝖺𝗅𝗅𝗒 𝖸𝗈𝗁 𝖶𝗂𝗅𝗅 𝖦𝖾𝗍 𝖳𝗁𝖾 𝖥𝗂𝗅𝖾𝗌 🌎

𝖭𝖡: 𝖸𝗈𝗎𝗋 𝖱𝖾𝗊𝗎𝖾𝗌𝗍 𝖮𝗇𝗅𝗒 𝖨𝗇 𝖬𝗒 𝖬𝗈𝗏𝗂𝖾𝗌 𝖦𝗋𝗈𝗎𝗉 𝖫𝗂𝗇𝗄 𝖢𝗁𝖾𝖼𝗄 𝗂𝗇 𝖠𝖻𝗈𝗏𝖾..!!</b>"""

    
    MOVREQ_TXT = """<b><i><u>🚸Instructions🚸</u></b></i>

<blockquote><b><i>🌿 Request Movies/Series in English language only.
🌿 Do not waste time asking for unreleased movies.
🌿 Just send the Movie Name and Year.And Language
🌿 Do not use stylish or fancy fonts.</b></i>
🥵 𝙈𝙪𝙨𝙩 𝘾𝙝𝙚𝙘𝙠 𝙎𝙥𝙚𝙡𝙡𝙞𝙣𝙜 𝙒𝙞𝙩𝙝 𝘼𝙫𝙖𝙞𝙡𝙖𝙗𝙡𝙚 𝘽𝙪𝙩𝙩𝙤𝙣𝙨 𝙖𝙣𝙙 𝙘𝙤𝙥𝙮 𝙥𝙖𝙨𝙩𝙚 𝙝𝙚𝙧𝙚👇</blockquote>

<b><i><u>🚸നിർദ്ദേശങ്ങൾ🚸</u></b></i>

<b><blockquote><i>🌿 ഇംഗ്ലീഷ് ഭാഷയിൽ തന്നെ movies/Series റിക്വസ്റ്റ് ചെയ്യുക 
🌿 റിലീസ് ആവാത്ത മൂവീസ് ചോദിച്ചു സമയം കളയണ്ട കിട്ടില്ല 🚫
🌿 സിനിമയുടെ പേര് വർഷം എന്നിവ മാത്രം അയച്ചാൽ മതി (വേണമെങ്കിൽ ഭാഷ🫴)
🌿 സ്റ്റൈലിഷ് അക്ഷരങ്ങൾ ഉപയോഗിക്കരുത്</i>
<u>🥵 പ്രധാനമായും താഴെയുള്ള ബട്ടനുകൾ ഉപയോഗിച്ച് സ്പെല്ലിങ് കറക്റ്റ് ആണോന്നു നോക്കി ഇവിടെ കോപ്പി പേസ്റ്റ് ചെയ്യുക</b></u><blockquote>"""
    
    NORSLTS = """𝗜𝗗 <b>: {}</b>
𝗡𝗮𝗺𝗲 <b>: {}</b>


𝗠𝗲𝘀𝘀𝗮𝗴𝗲 <code>{}</code>"""


    CUSTOM_FILE_CAPTION = """
<i><b><blockquote>📚 {file_name}</blockquote></b></i>
<b><a href=https://t.me/UrvashiTheaters_Main>©𝐓𝐞𝐚𝐦 𝐔𝐫𝐯𝐚𝐬𝐡𝐢 𝐓𝐡𝐞𝐚𝐭𝐞𝐫𝐬™️</a></b>
"""
        
