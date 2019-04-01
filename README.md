# Example Telegram Bot
This is exampke how telegram bot work on python

## How to use
First of all, install requirements. `pip install -r requirements.txt`

Then edit bot.py using text editor, edit `Token` and `CreatorID`

And then run the bot by `python bot.py`

Done, now you can send message to your bot

## For Heroku User
1. Fork this git

2. Go to heroku, and create new project. Select Python 3 if needed.

3. After you created project, go to Deploy tab

4. Select connect github

5. Search for SimpeTelegramBot and click Connect button

6. After connected, go to settings tab, press Reveal Config Vars, then insert like this

`Var: Yes`

`TokenBot: Your bot token from @botfather`

`MyID: Insert your user id`

7. Then finally, go to Resources tab, click Pen/Pencil button, turn on it, then Confirm

8. Check your bot on telegram

- For get user id, [Check this bot](t.me/EmiliaHikariBot) then type `/id`

- If you need help, [Join my group](https://t.me/BotPythonIndonesia)

## Example script usage

`/start` bot will reply `Hai!`

`/reply` bot will reply your message

`/feedback` bot will send feedback to creator

`/log` send log json output
