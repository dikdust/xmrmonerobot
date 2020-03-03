# xmrmonerobot
A minor fork of https://github.com/91DarioDev/CryptoTrackerBot 
check cryptocurrencies prices on telegram (with xmr improvements)

## SUPPORTED COMMANDS:
```
/price - return price of crypto
/help - return help message
/rank - return coins rank
/graph - return coins graph
/hashrate - return coins (atm only xmr) hashrate

```
_Note: If this bot is added in groups as admin, in order to keep the chat clean of spam, after few seconds it deletes both the command issued by the user and the message sent by the bot._

## Screenshots:
<p align="left">
<img src="../master/resources/screenshots/screenshot1.jpg" width="250">
<img src="../master/resources/screenshots/screenshot2.jpg" width="250">
</p>

## How to install:

### On Linux:

- Move to the path where you want to create the virtualenv directory
```
cd path
```
- Create a folder containing the env named `xmenv`
```
virtualenv -p python3 xmenv
```
- Install the bot from the zip
```
xmenv/bin/pip install https://github.com/dikdust/xmrmonerobot/archive/master.zip
```
- Run the bot. The first parameter of the command is the token.
```
xmenv/bin/cryptotrackerbot token
```
- To upgrade the bot:
```
xmenv/bin/pip install --upgrade https://github.com/dikdust/xmrmonerobot/archive/master.zip
```
- To delete everything:
```
rm -rf xmenv
```
