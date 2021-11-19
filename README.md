# energstarnight-bot

https://github.com/mirioeggmann/energyair-bot


The energstarnight-bot should only be used for educational purposes. Otherwise it is unfair for the other persons that play the game for real. You can try the bot **but at your own risk!**

## Codes
- **code 1:** Error occured
- **code 2:** Not enough answers right
- **code 3:** Something went wrong
- **code 4:** Wrong logo chosen
- **code 5:** Won!

### Docker
##### Setup
1. Install git
```bash
RUN apt update
RUN apt install -y git
```
2. Enter the following commands:
```bash
git clone "https://github.com/rohano420/energstarnight-bot.git"
cd energstarnight-bot
docker build energstarnight-bot --no-cache -t energstarnight-bot
```
---

##### Usage
- Enter the following commands in the powershell: **(don't forget to replace 0793332211 with your own phone number!)**
```bash
docker run -e PHONE_NUMBER=0793332211 -it energstarnight-bot bash
```
- Now you are in the docker container... to start the bot, just type the following command and press enter:
```bash
start
```
- To stop the bot press *CTRL+C*
- To exit the docker container type the following command and press enter:
```bash
exit
```
---
