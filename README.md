<h1 align="center"> 
    ✨ Duat ✨ 
</h1>

<h3 align="center"> 
    Telegram Group Manager Bot + Userbot Written In Python Using Pyrogram.
</h3>

<p align="center">
    <a href="https://python.org">
        <img src="http://forthebadge.com/images/badges/made-with-python.svg" alt="made-with-python">
    </a>
    <a href="https://GitHub.com/lalrochhara">
        <img src="http://ForTheBadge.com/images/badges/built-with-love.svg" alt="built-with-love">
    </a> <br>
    <img src="https://img.shields.io/github/license/lalrochhara/Duat?style=for-the-badge&logo=appveyor" alt="LICENSE">
    <img src="https://img.shields.io/github/contributors/lalrochhara/Duat?style=for-the-badge&logo=appveyor" alt="Contributors">
    <img src="https://img.shields.io/github/repo-size/lalrochhara/Duat?style=for-the-badge&logo=appveyor" alt="Repository Size"> <br>
    <img src="https://img.shields.io/badge/python-3.9-green?style=for-the-badge&logo=appveyor" alt="Python Version">
    <img src="https://img.shields.io/github/issues/lalrochhara/Duat?style=for-the-badge&logo=appveyor" alt="Issues">
    <img src="https://img.shields.io/github/forks/lalrochhara/Duat?style=for-the-badge&logo=appveyor" alt="Forks">
    <img src="https://img.shields.io/github/stars/lalrochhara/Duat?style=for-the-badge&logo=appveyor" alt="Stars">
</p>

<h3 align="center"> 
    Ready to use method
</h3>

<p align="center">
    A Support Group and ready-to-use running instance of this bot can be found on Telegram <br>
    <a href="https://t.me/DuatBot"> Duat </a> | 
    <a href="https://t.me/DuatiSupports">Miss Duati Supports </a>
</p>

<h2 align="center"> 
   ⇝ Requirements ⇜
</h2>

<p align="center">
    <a href="https://www.python.org/downloads/release/python-390/"> Python3.9 </a> |
    <a href="https://docs.pyrogram.org/intro/setup#api-keys"> Telegram API Key </a> |
    <a href="https://t.me/botfather"> Telegram Bot Token </a> | 
    <a href="https://telegra.ph/How-To-get-Mongodb-URI-04-06"> MongoDB URI </a>
</p>

<h2 align="center"> 
   ⇝ Install Locally Or On A VPS ⇜
</h2>

```console
lalrochhara@arch:~$ git clone https://github.com/lalrochhara/Duat
lalrochhara@arch:~$ cd Duat
lalrochhara@arch:~$ pip3 install -U -r requirements.txt
lalrochhara@arch:~$ cp sample_config.py config.py
```
 
<h3 align="center"> 
    Edit <b>config.py</b> with your own values
</h3>

<h2 align="center"> 
   ⇝ Run Directly ⇜
</h2>

```console
lalrochhara@arch:~$ python3 -m Duat
```

<h1>
    <p align="center">
        <a href="https://heroku.com/deploy?template=https://github.com/lalrochhara/Duat">
            <img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy">
        </a>
    </p>
</h1>

<h3 align="center"> 
   Generating Pyrogram Session For Heroku
</h3>

```console
lalrochhara@arch:~$ git clone https://github.com/lalrochhara/Duat
lalrochhara@arch:~$ cd Duat
lalrochhara@arch:~$ pip3 install pyrogram TgCrypto
lalrochhara@arch:~$ python3 str_gen.py
```

<h1 align="center"> 
   ⇝ Docker ⇜
</h1>

```console
lalrochhara@arch:~$ git clone https://github.com/lalrochhara/Duat
lalrochhara@arch:~$ cd Duat
lalrochhara@arch:~$ cp sample_config.env config.env
```

<h3 align="center"> 
    Edit <b> config.env </b> with your own values
</h3>

```console
lalrochhara@arch:~$ sudo docker build . -t Duat
lalrochhara@arch:~$ sudo docker run Duat
```

<h2 align="center"> 
   ⇝ Write new modules ⇜
</h2>

```py
# Add license text here, get it from below

from Duat import app # This is bot's client
from Duat import app2 # userbot client, import it if module is related to userbot
from pyrogram import filters # pyrogram filters
...


# For /help menu
__MODULE__ = "Module Name"
__HELP__ = "Module help message"


@app.on_message(~filters.edited & filters.command("start"))
async def some_function(_, message):
    await message.reply_text("I'm already up!!")

# Many useful functions are in, Duat/utils/, Duat, and Duat/core/
```

<h3 align="center"> 
   And put that file in Duat/modules/, restart and test your bot.
</h3>
