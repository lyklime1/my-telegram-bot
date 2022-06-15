# my-telegram-bot
My first pet-project at GitHub

To start this code you need to create .bat:

    @echo off
    call %~dp0venv\Scripts\activate
    cd %~dp0
    set TOKEN=<your telegram-bot token>
    python main.py
    pause
    
