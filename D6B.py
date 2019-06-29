import configparser

import discord
from discord.ext import commands

import login
from banhammer import banhammer

desc = "Dan6erbond support bot."
bot = commands.Bot("$", description=desc)
bh = banhammer.Banhammer(login.get_reddit(), embed_color=discord.Colour(0).from_rgb(207, 206, 23))
bh.add_subreddits("dan6erbond")
bh.add_subreddits("substarters")
bh.add_subreddits("jealousasfuck")

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
    bh.run()


@bh.new(subreddit="dan6erbond")
@bh.reports()
async def handle_dan6erbond_new(post):
    channel_id = 593131220041465868 if str(post.subreddit).lower() == "dan6erbond" else 593712450487058433 if str(
        post.subreddit).lower() == "substarters" else 593816541464625205
    msg = await bot.get_channel(channel_id).send(embed=post.get_embed())
    for react in post.get_reactions():
        try:
            await msg.add_reaction(react.emoji)
        except:
            continue


@bot.event
async def on_message(m):
    if "pussy" in m.content.lower() or ("puss" in m.content.lower() and m.author.id == 483880415124520971):
        print(m.content)
        await m.delete()
    if m.channel.id in [593131220041465868, 593712450487058433, 593816541464625205] and not m.author.bot:
        item = bh.get_item(m.content)
        if item is not None:
            for react in item.get_reactions():
                try:
                    await msg.add_reaction(react.emoji)
                except:
                    continue
    await bot.process_commands(m)


@bot.event
async def on_raw_reaction_add(p):
    c = bot.get_channel(p.channel_id)
    u = c.guild.get_member(p.user_id)
    if u.bot:
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
    # await ctx.send(string.capwords(new_nick))
    await ctx.author.edit(nick=new_nick.title())


@bot.command()
async def sad(ctx):
    await ctx.send("*S A D.*")


async def analyze_idealists():
    Idealist = bot.get_guild(568012485320245258)
    substarters = bot.get_guild(531782661564399626)

    print(Idealist)
    print(substarters)

    for member in substarters.members:
        if Idealist.get_member(member.id) is not None:
            print("<@!{}>".format(member.id))


config = configparser.ConfigParser()
config.read("discord.ini")
bot.run(config["D6B"]["token"])
