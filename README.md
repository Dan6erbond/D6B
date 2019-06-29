# D6B
D6B is Dan6erbond's personal Discord bot. In addition to a swear filter it has a couple of commands as well as implements the [Banhammer framework](https://github.com/Dan6erbond/Banhammer.py) to aid in moderating Dan6erbond's subreddits.

## Key Features
Besides the commands the bot is setup to welcome new users that join the guild with a default welcome message as well as stream reports and new items on [/r/dan6erbond](https://www.reddit.com/r/dan6erbond) and other subreddits to a dedicated channel in which reactions are added for Dan6erbond to moderate the subreddit.

### Commands
D6B has a couple of commands, most of them are quite simple. All commands use the `$` prefix:
 - `help`: This is the default Discord.py implementation of the help command as it hasn't been altered yet.
 - `nick`: Sets your nickname in the server to a titled version of what's fed to the command.
 - `sad`: Reponds with "*S A D.*".

## Usage
Though this bot isn't designed to be used by others, it is a GPL3.0 project which means you're free to use its code to build your own bot! It also serves as a good starting point for people trying to become familiar with the Banhammer framework though the [Banhacker bot](https://github.com/Dan6erbond/Banhacker/) may suit your needs better.

A improved swear filter is being worked on so that could be of use to some users once it has been tested and released. If you do want to use the code, make sure you have the dependancies, namely [Discord.py](https://discordpy.readthedocs.io) if you want the base features as well as [PRAW](https://praw.readthedocs.io) if you want to use the Banhammer framework. Those can be installed with the following terminal commands:
 - `pip3 install -U discord.py`
 - `pip3 install -U praw`

## Roadmap
 - [ ] More dynamic subreddit moderation.
 - [ ] Improved swear filter.
