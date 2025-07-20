import discord
from discord.ext import commands
from colorama import init, Fore, Style
init()
purple = Fore.MAGENTA
white = Fore.WHITE
reset = Style.RESET_ALL
def styled_input(prompt):
    print(f"{purple}┌───────────────[ {white}AirFlow - SERVER INFO{purple} ]───────────────┐{reset}")
    print(f"{purple}│{white} {prompt:<50} {reset}")
    print(f"{purple}│{white} >> {reset}", end="")
    user_input = input()
    print(f"{purple}└──────────────────────────────────────────────────┘{reset}")
    return user_input.strip()
def status_message(message):
    print(f"{purple}[EXECUTING]{white} {message}...{reset}")
def completion_message(message):
    print(f"{purple}[COMPLETE]{white} {message}{reset}")
async def server_info(token, bot):
    guild_id = styled_input("Enter the server (guild) ID to fetch info for:")
    if not guild_id:
        print(f"{purple}[ERROR]{white} No server ID provided. Exiting...{reset}")
        return
    try:
        guild_id = int(guild_id)
    except ValueError:
        print(f"{purple}[ERROR]{white} Invalid server ID. Must be a number.{reset}")
        return
    guild = bot.get_guild(guild_id)
    if not guild:
        print(f"{purple}[ERROR]{white} Bot is not in the server or invalid server ID.{reset}")
        print(f"{purple}[INFO]{white} Ensure the bot is invited to the server with sufficient permissions.{reset}")
        return
    status_message(f"Fetching info for server: {guild.name}")
    owner = guild.owner
    member_count = guild.member_count
    creation_date = guild.created_at.strftime("%Y-%m-%d %H:%M:%S")
    text_channels = len([ch for ch in guild.channels if isinstance(ch, discord.TextChannel)])
    voice_channels = len([ch for ch in guild.channels if isinstance(ch, discord.VoiceChannel)])
    role_count = len(guild.roles) - 1
    bot_count = len([member for member in guild.members if member.bot])
    print(f"{purple}[INFO]{white} Server Info for {guild.name}:{reset}")
    print(f"  - Server ID: {white}{guild.id}{reset}")
    print(f"  - Name: {white}{guild.name}{reset}")
    print(f"  - Owner: {white}{owner.name}#{owner.discriminator}{reset}")
    print(f"  - Member Count: {white}{member_count}{reset}")
    print(f"  - Bot Count: {white}{bot_count}{reset}")
    print(f"  - Created On: {white}{creation_date}{reset}")
    print(f"  - Text Channels: {white}{text_channels}{reset}")
    print(f"  - Voice Channels: {white}{voice_channels}{reset}")
    print(f"  - Role Count: {white}{role_count}{reset}")
    print(f"  - Region: {white}{getattr(guild, 'region', 'Automatic (Not Available)')}{reset}")
    completion_message("Server Info retrieval completed")
def main():
    token = styled_input("Enter your Discord bot token:")
    if not token:
        print(f"{purple}[ERROR]{white} No bot token provided. Exiting...{reset}")
        return
    intents = discord.Intents.default()
    intents.members = True
    intents.guilds = True
    bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)
    @bot.event
    async def on_ready():
        print(f"{purple}[INFO]{white} Bot logged in as {bot.user.name}#{bot.user.discriminator}{reset}")
        await server_info(token, bot)
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