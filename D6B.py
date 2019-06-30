import configparser
import json

import discord
from discord.ext import commands

import fuzzle
import login
from banhammer import banhammer

bot = commands.Bot("$", description="Dan6erbond support bot.")
bh = banhammer.Banhammer(login.get_reddit(), bot=bot, change_presence=True,
                         embed_color=discord.Colour(0).from_rgb(67, 181, 129))


@bot.event
async def on_command_error(ctx, error):
    print(error)


@bot.event
async def on_member_join(member):
    if member.guild.id == 583362545440522377:
        welcome = "Hey, {0.mention}! Welcome to the server, read <#583963046884671507> before you disturb Ravi.".format(
            member)
        await bot.get_channel(583964848300490752).send(welcome)
        await member.add_roles(member.guild.get_role(583969007724527636))


@bot.event
async def on_ready():
    print(str(bot.user) + ' is running.')
    with open("files/subreddits.json") as f:
        subs = json.loads(f.read())
        for sub in subs:
            bh.add_subreddits(sub["sub"])
    bh.run()


@bot.command()
async def subreddits(ctx):
    await ctx.send(embed=bh.get_subreddits_embed())


@bot.command()
async def reactions(ctx):
    await ctx.send(embed=bh.get_reactions_embed())


@bot.command()
@commands.has_permissions(administrator=True)
async def addsub(ctx, subreddit):
    with open("files/subreddits.json") as f:
        subs = json.loads(f.read())
        for sub in subs:
            if sub["sub"].lower() == subreddit.lower():
                await ctx.send("/r/{} already added!".format(subreddit))
                return
        for cat in ctx.guild.categories:
            if cat.id == 594461395039551519:
                bh.add_subreddits(sub["sub"])
                await ctx.guild.create_text_channel(subreddit, category=cat)
                subs.append({
                    "sub": subreddit,
                    "id": channel.id
                })
                with open("files/subreddits.json", "w+") as f:
                    f.write(json.dumps(subs, indent=4))
                await ctx.send("Successfully added /r/{}!".format(subreddit))
                break


@bot.command()
@commands.has_permissions(administrator=True)
async def delsub(ctx):
    if ctx.channel.category is None or ctx.channel.category.id != 594461395039551519:
        return
    with open("files/subreddits.json") as f:
        subs = json.loads(f.read())
        found = False
        for sub in subs:
            if sub["sub"].lower() == ctx.channel.name.lower():
                subs.remove(sub)
                found = True
                break
        if found:
            with open("files/subreddits.json", "w+") as f:
                f.write(json.dumps(subs, indent=4))
            await ctx.send("Successfully removed /r/{}!".format(ctx.channel.name))
        else:
            await ctx.send("/r/{} was never added!".format(ctx.channel.name))


@bh.new()
@bh.comments()
@bh.mail()
@bh.reports()
@bh.reports("Anti-Evil Operations")
async def handle_item(item):
    with open("files/subreddits.json") as f:
        subs = json.loads(f.read())
        for sub in subs:
            if sub["sub"].lower() == str(item.subreddit).lower():
                msg = await bot.get_channel(sub["id"]).send(embed=item.get_embed())
                await item.add_reactions(msg)
                break


@bot.event
async def on_message(m):
    if m.author.bot:
        return

    swear = False

    swears = list()
    with open("files/swear_words.json") as f:
        swears = json.loads(f.read())

    for word in m.content.split(" "):
        if not swear:
            for result in fuzzle.find(swears, word):
                if result["accuracy"] > 0.9:
                    print(result)
                    swear = True
                    break
        else:
            break

    if swear: await m.channel.send("Watch yo mouth!")
    if swear and m.author.id in [483880415124520971]: await m.delete()

    if m.channel.category is not None and m.channel.category.id == 594461395039551519:
        item = bh.get_item(m.content)
        if item is not None:
            await item.add_reactions(m)
    await bot.process_commands(m)


@bot.event
async def on_raw_reaction_add(p):
    c = bot.get_channel(p.channel_id)
    if c.category is None or c.category.id != 594461395039551519:
        return
    u = c.guild.get_member(p.user_id)
    if u.bot or u.id != 383657174674702346:
        return
    m = await c.fetch_message(p.message_id)
    e = p.emoji.name if not p.emoji.is_custom_emoji() else "<:{}:{}>".format(p.emoji.name, p.emoji.id)
    item = bh.get_item(m.content) if len(m.embeds) == 0 else bh.get_item(m.embeds[0])
    if item is None:
        return
    await m.delete()
    await c.send(item.get_reaction(e).handle(u.nick)["message"])


@bot.command()
async def nick(ctx, *, new_nick):
    await ctx.author.edit(nick=new_nick.title())


@bot.command()
async def sad(ctx):
    await ctx.send("*S A D.*")


config = configparser.ConfigParser()
config.read("discord.ini")
bot.run(config["D6B"]["token"])
