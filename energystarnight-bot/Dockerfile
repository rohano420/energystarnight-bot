FROM python:3.6
USER root

RUN python3 -m pip install lxml
RUN python3 -m pip install requests
RUN git clone https://github.com/rohano420/energystarnight-bot.git /work/energystarnight-bot
RUN echo 'alias start="python3 /work/energystarnight-bot/energystarnight-bot.py"' >> ~/.bashrc
