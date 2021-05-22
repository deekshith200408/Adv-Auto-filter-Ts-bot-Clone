#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG | @Hillard_Har 

class Translation(object):
    
    START_TEXT = """🤓🤹ʜɪ ʜᴇʟᴏ {},🧸
••••••••••••••••••••••••••••••••••••••••••••••
[ 🧐ɪ ᴀᴍ ᴀ sɪᴍᴘʟᴇ ᴀᴅᴠᴀɴᴄᴇᴅ Aᴜᴛᴏ Fɪʟᴛᴇʀ Bᴏᴛ🏇..🧸ᴡᴏʀᴋɪɴɢ ᴏɴ @UM_Requests⚡ ]

Bᴏᴛ sɪᴍᴘʟʏ sᴇᴀʀᴄʜ ғᴏʀ ᴛʜᴇ ғɪʟᴇs ғʀᴏᴍ ᴘʀᴏᴠɪᴅᴇᴅ ᴄʜᴀɴɴᴇʟ ᴀᴄᴄᴏʀᴅɪɴɢ ᴛᴏ ɢɪᴠᴇɴ ᴏ̨ᴜᴇʀʏ ᴀɴᴅ ɢɪᴠᴇs ʟɪɴᴋ ᴛᴏ ᴛʜᴏsᴇ ғɪʟᴇs ᴀs ʙᴜᴛᴛᴏɴs!


🧬ғᴏʀ ᴍᴏʀᴇ ɪɴғᴏ /help....🔭

🔬🧲© ᴄʀᴇᴀᴛᴏʀ : @Deeks_04_8🎩,

\/°•°•°•°•°•°•°•°•[ 🆄🅼🆁 ]°•°•°•°•°•°•°•°•°\/"""





    
    HELP_TEXT = """
💡 𝐁𝐎𝐓'𝐒 𝐇𝐄𝐋𝐏

🚀ᴀᴅᴅ ʙᴏᴛ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴡɪᴛʜ ᴀᴅᴍɪɴ ʀɪɢʜᴛs.

🛸ᴀᴅᴅ ʙᴏᴛ ᴛᴏ ᴄʜᴀɴɴᴇʟs ᴡʜɪᴄʜ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ʟɪɴᴋ ᴡɪᴛʜ ᴀʟʟ ᴀᴅᴍɪɴ ʀɪɢʜᴛs!🏟️

⭕ 𝐌𝐲 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 (ᴏɴʟʏ ᴡᴏʀᴋs ɪɴ ɢʀᴏᴜᴘ) 🏛

    👉 <code>/add chat_id</code>

                OR                  - To Connect A Group With A Channel (Bot Should Be Admin With Full Previlages In Both Group And Channel)

     <code>/add @Username</code>

     

    👉 <code>/del chat_id</code>

                OR                  - To disconnect A Group With A Channel

     <code>/del @Username</code>

     

    👉 <code>/delall</code>  - This Command Will Disconnect All Connected Channel With The Group And Deletes All Its File From DB

    

    👉 <code>/settings</code> -  This Command Will Display You A Settings Pannel Instance Which Can Be Used To Tweek Bot's Settings Accordingly

🔰 𝐒𝐄𝐓𝐓𝐈𝐍𝐆 𝐏𝐀𝐍𝐄𝐋

            👉 <code>Channel</code> - Button Will Show You All The Connected Chats With The Group And Will Show Buttons Correspnding To There Order For Furthur Controls

            

            👉 <code>Filter Types</code> - Button Will Show You The 3 Filter Option Available In Bot... Pressing Each Buttons Will Either Enable or Disable Them And This Will Take Into Action As Soon As You Use Them Without The Need Of A Restart

            👉 <code>Configure</code> - Button Will Helps You To Change No. of Pages/ Buttons Per Page/ Total Result Without Acutally Editing The Repo... Also It Provide Option To Enable/Disable For Showing Invite Link In Each Results

            

            👉 <code>Status</code> - Button Will Shows The Stats Of Your Channel.


😅 ɴᴏ ɴᴇᴇᴅ ᴀᴅᴅ ᴇᴀᴄʜ ғɪʟᴛᴇʀ ᴀɢᴀɪɴ!📢

📯ʙᴏᴛ ᴡɪʟʟ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ sᴇᴀʀᴄʜ ғᴏʀ ʏᴏᴜʀ ғɪʟᴇs ᴀɴᴅ ɢɪᴠᴇ ʟɪɴᴋs ᴛᴏ ᴛʜᴀᴛ!🗡️


© @UNI_MOVIES_BOX | @UM_Requests ⚡

•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•"""
            


    
    ABOUT_TEXT = """
📕 𝐀𝐛𝐨𝐮𝐭 𝐌𝐞 ,⚔️

[°=°][°=°][°=°][°=°][°=°][°=°][°=°][°=°]

○ ᴍʏ ɴᴀᴍᴇ : υмя мονιєѕ ∂οиєя.

○ ʟᴀɴɢᴜᴀɢᴇ : ᴘʏᴛʜᴏɴ .

○ ғʀᴀᴍᴇᴡᴏʀᴋ : ᴘʏʀᴏɢʀᴀᴍ .

○ sᴇʀᴠᴇʀ : ʜᴇʀᴏᴋᴜ .

○ ᴠᴇʀsɪᴏɴ : 1.0.0.

○ ᴄʀᴇᴀᴛᴏʀ : @Deeks_04_8 🇮🇳

•∆• ᴊᴏɪɴ  ➠ @UM_Requests •~•

°^°^°^°^°^°^°^°^°^°^°^°^°^°^°^°^°^
"""
