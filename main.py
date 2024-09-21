from pymino import Bot
from pymino.ext import *
import json

with open("config.json", "r") as file:
    config = json.load(file)

senha = config["senha"]
usuario = config["usuario"]
service_key = config["service_key"]

bot = Bot(
    service_key=service_key,
    device_key="E7309ECC0953C6FA60005B2765F99DBBC965C8E9",
    signature_key="DFA5ED192DDA6E88A12FE12130DC6206B1251E44",
    command_prefix="!",
    community_id="80694489",
    device_id="1742abc8bba56719fdbcde9283d7e7467d1540cba05c1817104e9e83c7b8e108c49d81bbc89f18f428",
)


@bot.on_ready()
def ready():
    print(f"{bot.profile.username} está logada!")


@bot.command(
    name="ping", description="This will reply with Pong!", aliases=["p"], cooldown=0
)
def ping(ctx: Context):
    ctx.reply("Pong!")


@bot.command("say")
def say(ctx: Context, message: str):
    ctx.reply(message)


@bot.on_error()
def error(error: Exception):
    print(f"An error has occurred: {error}")


bot.run(usuario, senha)
