# my-telegram-bot
My first pet-project at GitHub

To run this code, you need to create .bat in the project directory:

    @echo off
    call %~dp0venv\Scripts\activate
    cd %~dp0
    set TOKEN=<your telegram-bot token>
    python main.py
    pause
    
