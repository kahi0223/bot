# bot

Using Telegram Bot API to create a bot that can send messages to a group.

# setup

## create a bot

1. talk to @BotFather
2. create a new bot
3. copy the token
4. create a file named `.env` in the root directory of this project
5. paste the token into the file with parameter `TELEGRAM_TOKEN=`

## create a group (if needed)

1. create a group
2. add the bot to the group
3. make the bot an admin of the group

# method

## get bot status

```python
from bot import Bot
Bot().is_active()
```

## send message

```python
from bot import Bot
Bot().send_message(chat_id=123, text='hello world')
```

## get group chat id of the first group

bot has to be an admin of the group.

```python
from bot import Bot
chat_id = Bot().get_first_group_chat_id()
```
