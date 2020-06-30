import discord
import random

client = discord.Client()

# 起動時に通知してくれる処理
@client.event
async def on_ready():
    print('ログインしました')

# リプライ処理
@client.event
async def on_message(message):
	if message.content.startswith('本田とじゃんけん　グー'):
		a = random.randint(1, 100)
		if a == 100:
			reply = 'やるやん！\n明日俺にリベンジさせて。\n'
			await message.channel.send(reply.format(message))
			await message.channel.send(file=discord.File('Douzo.PNG'))
		else:
			reply = '俺の勝ち！\n負けは次に繋がるチャンスです。\nネバーギブアップ！\n'
			await message.channel.send(reply.format(message))
			await message.channel.send(file=discord.File('Pa.PNG'))

	if message.content.startswith('本田とじゃんけん　チョキ'):
		a = random.randint(1, 100)
		if a == 100:
			reply = 'やるやん！\n明日俺にリベンジさせて。\n'
			await message.channel.send(reply.format(message))
			await message.channel.send(file=discord.File('Douzo.PNG'))
		else:
			reply = '俺の勝ち！\nたかがじゃんけん。そう思ってませんか？\nそれやったら明日も俺が勝ちますよ。\n'
			await message.channel.send(reply.format(message))
			await message.channel.send(file=discord.File('Gu.PNG'))

	if message.content.startswith('本田とじゃんけん　パー'):
		a = random.randint(1, 100)
		if a == 100:
			reply = 'やるやん！\n明日俺にリベンジさせて。\n'
			await message.channel.send(reply.format(message))
			await message.channel.send(file=discord.File('Douzo.PNG'))
		else:
			reply = '俺の勝ち！\nなんで負けたか明日まで考えてください。\nそしたら何か見えてくるはずです。\n'
			await message.channel.send(reply.format(message))
			await message.channel.send(file=discord.File('Choki.PNG'))

# botの接続と起動
# (tokenにはbotアカウントのアクセストークンを入れてください)
# 発行したトークンを入力
client.run('input token')
