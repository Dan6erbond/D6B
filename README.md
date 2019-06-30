# D6B
D6B is Dan6erbond's personal Discord bot. In addition to a swear filter it has a couple of commands as well as implements [Banhammer.py](https://github.com/Dan6erbond/Banhammer.py) to aid in moderating Dan6erbond's subreddits.

## Key Features
Besides the commands the bot is setup to welcome new users that join the guild with a default welcome message as well as stream reports and new items on [/r/dan6erbond](https://www.reddit.com/r/dan6erbond) and other subreddits to a dedicated channel in which reactions are added for Dan6erbond to moderate the subreddit.

### Commands
D6B has a couple of commands, most of them are quite simple. All commands use the `$` prefix:
 - `help`: This is the default Discord.py implementation of the help command as it hasn't been altered yet.
 - `nick`: Sets your nickname in the server to a titled version of what's fed to the command.
 - `sad`: Reponds with "*S A D.*".
 - `subreddits`: Displays the configured subreddits for Banhammer in a neat embed.
 - `reactions`: Shows all the reactions that a subreddit has configured.
 - `addsub` (admin only): Adds a subreddit to the `SUBREDDITS` category as well as the Banhammer instance.
 - `delsub` (admin only): Removes the current channel's assigned subreddit from the file as well as Banhammer.
 
### Subreddit moderation
Using the Banhammer.py framework as well as some local files the bot keeps tabs on what subreddits to scan as well as handle reactions for. It knows the `SUBREDDITS` category and maintains [subreddits.json](files/subreddits.json) which is a simple JSON list of subreddit's names as well as their channel's ID. With an iteration the bot then checks where content is to be sent to every time Banhammer calls `handle_item(item)`.

Before calling `bh.run()` the bot iterates through all the subreddits and adds them to Banhammer as well as when `$addsub` is called. Using this system you can have a category for many of your subreddits you want to moderate and handle them all from the same Discord server!

## Usage
Though this bot isn't designed to be used by others, it is a GPL3.0 project which means you're free to use its code to build your own bot! It also serves as a good starting point for people trying to become familiar with Banhammer.py.

[Banhacker](https://github.com/Dan6erbond/Banhacker/) is a Mariavi bot that implements Banhammer.py in a different way and may be what you're looking for if you just want to handle one subreddit.

A improved swear filter is being worked on so that could be of use to some users once it has been tested and released. If you do want to use the code, make sure you have the dependancies, namely [Discord.py](https://discordpy.readthedocs.io) if you want the base features as well as [PRAW](https://praw.readthedocs.io) if you want to use the Banhammer.py. Those can be installed with the following terminal commands:
 - `pip3 install -U discord.py`
 - `pip3 install -U praw`
 
## Links
 - [Banhammer.py](https://github.com/Dan6erbond/Banhammer.py)
 - [Discord server](https://discord.gg/wMEyKZk)

## Roadmap
 - [ ] More dynamic subreddit moderation.
 - [ ] Improved swear filter.
