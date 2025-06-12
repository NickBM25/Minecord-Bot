''' 
TEST TO CHECK JSON RETRIEVED
if json_data:
    json_string = json.dumps(json_data, indent=2)
    truncated_json = json_string[:2000]  # Discord's character limit
'''

import os
from dotenv import load_dotenv
import paramiko
import discord
import asyncio
import json
from discord.ext import commands

load_dotenv()
port = os.getenv('PORT')
hostname = os.getenv('HOSTNAME')
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')

remote_file_path = '/generated.json'

class Teams(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
            
    @discord.slash_command(name='test_sftp', description='Test SFTP Function')
    async def test_sftp(self, ctx: discord.ApplicationContext):
        await ctx.defer() # Remove o timeout de 3 segundos

        # Run SFTP retrieval in a thread to prevent blocking
        json_data = await asyncio.to_thread(
            self.get_file_sftp,
            hostname, port, username, password, remote_file_path
        )

        if json_data:
            name = json_data["teams"]["name"]
        
            await ctx.followup.send(f"Nome da equipe: {name}",  ephemeral=True)
        else:
            await ctx.followup.send("Failed to retrieve or parse the file.")

    def get_file_sftp(self, hostname, port, username, password, remote_file_path):
        try:
            # Create the SSH client
            ssh_client = paramiko.SSHClient()
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh_client.connect(hostname, port, username, password)

            # Open SFTP session
            sftp = ssh_client.open_sftp()
            with sftp.open(remote_file_path, 'r') as remote_file: # Read the json file content
                file_content = remote_file.read()
            sftp.close()

            print(f"File content retrieved successfully from {remote_file_path}")
            # Decode the content and parse it as JSON
            json_data = json.loads(file_content.decode('utf-8'))
            
            return json_data

        except Exception as e:
            print(f"An error occurred: {e}")
            return None
        finally:
            if ssh_client:
                ssh_client.close()

def setup(bot):
    bot.add_cog(Teams(bot))
