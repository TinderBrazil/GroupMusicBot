from asyncio.queues import QueueEmpty

from pyrogram import Client
from pyrogram.types import Message
from callsmusic import callsmusic

from config import BOT_NAME as BN
from helpers.filters import command, other_filters
from helpers.decorators import errors, authorized_users_only


@Client.on_message(command(["pause", "pause@TioMortyBot"]) & other_filters)
@errors
@authorized_users_only
async def pause(_, message: Message):
    if (
            message.chat.id not in callsmusic.pytgcalls.active_calls
    ) or (
            callsmusic.pytgcalls.active_calls[message.chat.id] == 'pausado'
    ):
        await message.reply_text("🌟| {}❗ Não está jogando nada!".format(message.from_user.mention))
    else:
        callsmusic.pytgcalls.pause_stream(message.chat.id)
        await message.reply_text("🌟| {} ▶️ Em pausa!".format(message.from_user.mention))


@Client.on_message(command(["resume","resume@TioMortyBot"]) & other_filters)
@errors
@authorized_users_only
async def resume(_, message: Message):
    if (
            message.chat.id not in callsmusic.pytgcalls.active_calls
    ) or (
            callsmusic.pytgcalls.active_calls[message.chat.id] == 'Tocando'
    ):
        await message.reply_text("🌟| {}❗ Nada está em pausa!".format(message.from_user.mention))
    else:
        callsmusic.pytgcalls.resume_stream(message.chat.id)
        await message.reply_text("🌟| {} ⏸ Retomado!".format(message.from_user.mention))


@Client.on_message(command(["stop","stop@TioMorty"]) & other_filters)
@errors
@authorized_users_only
async def stop(_, message: Message):
    if message.chat.id not in callsmusic.pytgcalls.active_calls:
        await message.reply_text("🌟| {}❗ Nada está transmitindo! ".format(message.from_user.mention))
    else:
        try:
            callsmusic.queues.clear(message.chat.id)
        except QueueEmpty:
            pass

        callsmusic.pytgcalls.leave_group_call(message.chat.id)
        await message.reply_text("🌟| {}❌ Stream interrompido!".format(message.from_user.mention))


@Client.on_message(command(["skip","skip@TioMorty"]) & other_filters)
@errors
@authorized_users_only
async def skip(_, message: Message):
    if message.chat.id not in callsmusic.pytgcalls.active_calls:
        await message.reply_text("🌟| {}❗ Nada está tocando para Skip!".format(message.from_user.mention))
    else:
        callsmusic.queues.task_done(message.chat.id)

        if callsmusic.queues.is_empty(message.chat.id):
            callsmusic.pytgcalls.leave_group_call(message.chat.id)
        else:
            callsmusic.pytgcalls.change_stream(
                message.chat.id,
                callsmusic.queues.get(message.chat.id)["file"]
            )

        await message.reply_text("🌟| {} ➡️ Pulou a música atual!".format(message.from_user.mention))