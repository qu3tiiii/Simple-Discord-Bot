import discord
from discord.ext import commands
import datetime
#Bot de discord simple en 12 lineas<3
from urllib import parse, request
import re
                               #Prefijo del bot
bot = commands.Bot(command_prefix='!', description="Tutorial Bot/Undead")
#1
@bot.command()
         #Mensaje a responder
async def Hola(ctx):
                    #Respuesta
    await ctx.send('Hola ')
#2

#Desde 1 hasta 2 pueden copiar y pegar cambiando los mensajes de respuesta etc
#Actividad del bot
@bot.event
async def on_ready():
   print('Estoy listo!:)')
           #Token del bot
bot.run('Token aca')
