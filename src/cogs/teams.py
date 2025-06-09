import io
import paramiko
import discord
import asyncio
import json
from discord.ext import commands

hostname = 'eu-central-1.sftpcloud.io'
port = 22
username = '695deedd56e04d938ff282a3aa538a82'
password = 'ALacZ2Y2YXOLzO1ni1ILNp2pPBabNxhh'
remote_file_path = '/generated.json'

class Teams(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        
    @discord.slash_command(name='test_sftp', description='Test SFTP Function')
    async def test_sftp(self, ctx: discord.ApplicationContext):
        # Run the SFTP function in a background task to avoid blocking
        json_data = await asyncio.to_thread(self.get_file_sftp, hostname, port, username, password, remote_file_path)
        
        # Ensure the file content is parsed correctly and send it
        if json_data:
            # Convert JSON object back to a pretty-printed string (or compact if preferred)
            json_string = json.dumps(json_data, indent=2)
            
            # Truncate to 2000 characters (Discord's limit)
            truncated_json = json_string[:2000]
            
            await ctx.respond(f"Test SFTP:\n```json\n{truncated_json}\n```")
            
        else:
            await ctx.respond('Failed to retrieve or parse the file.')

    def get_file_sftp(self, hostname, port, username, password, remote_file_path):
        try:
            # Create the SSH client
            ssh_client = paramiko.SSHClient()
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh_client.connect(hostname, port, username, password)

            # Open SFTP session
            sftp = ssh_client.open_sftp()

            # Read the file content (assuming it's a JSON file)
            with sftp.open(remote_file_path, 'r') as remote_file:
                file_content = remote_file.read()

            sftp.close()

            print(f"File content retrieved successfully from {remote_file_path}")
            
            # Decode the content and parse it as JSON (if it's a JSON file)
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
