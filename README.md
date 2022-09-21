# SMSBot

## Introduction

This is a very simple bot powered by BlenderBot 3 and Twilio. Send an SMS message to it!

## Installation

1. Download Source: Run in Terminal:
```
git clone https://github.com/fakerybakery/smsbot.git
```
2. Run Server: Run in Terminal:
macOS Version:
```
python3 main.py
```
Unix/Linux/Windows Version:
```
python main.py
```
3. Use ngrok or localtunnel
```
ngrok http 5000
```
or
```
lt --port 5000 --subdomain my-twilio-ai-chat
```
4. Test it out! Visit your ngrok/localtunnel website! Append "/bot" to the end of it. For example:
ngrok:
```
my-twilio-ai-chat.ngrok.io/bot
```
localtunnel:
```
my-twilio-ai-chat.loca.lt/bot
```
5. Test it out! Send a POST request to the server!

If all is working well, it should take a minute (at most 3 or 4 minutes) to respond. If it takes too long, change the model to a smaller model, replace `blenderbot-3b` with `blenderbot-400m` or `blenderbot-small-90m`. These models are smaller and will not be as accurate (it will seem faker when you're chatting later on.)
6. Set up Twilio!

  a. Sign up for a Twilio account. Would you like to support me? Use [this](https://www.twilio.com/referral/ZdVrTn) affiliate link and get $10 off when you purchase a premium Twilio plan!
  
  b. Purchase a Twilio phone number in the Phone Numbers section (it's free on the free trial, no credit card required). **Twilio _DOES_ offer toll-free numbers (833, 844, 855, 866, 877, 888) but not 800 due to a shortage.**
  
  c. On the left sidebar, click `Phone Numbers`, then `Manage`, then `Active numbers`. Click the one you purchased.
  
  d. Under the `Voice & Fax` section, find `A CALL COMES IN`. Set the dropdown to `Webhook` and the input field to blank.
  
  e. Under `Messaging`, find `A MESSAGE COMES IN`. Select `Webhook` and type in the input field the URL you got from ngrok or localtunnel (remember the `/bot` at the end and the `https://`!)
  
  For example: `https://my-twilio-ai-chat.loca.lt/bot`
  
  d. Click `Save` at the bottom left.
  
  e. Text your phone number! (Don't call it, it won't work!)
  
Does it work? If not, make sure to leave an issue, otherwise, please leave a `Star`, `Watch`, and maybe even `Fork`!

## Heroku? Google Cloud? AWS? What next?
I tried uploading to Heroku, but it was larger than 0.5 GB (in fact, 1.3 GB!)

I didn't want to pay for Google Cloud and I've already used up my AWS free trial :(. Maybe later I'll figure out how to do this! Please, make an issue if you have advice on how to do this!
## Credits/Keywords
Some code is from: [abdallah197/Whatsapp-HuggingFace-Chatbot](https://github.com/abdallah197/Whatsapp-HuggingFace-Chatbot)
Uses: HuggingFace Transformers, ParlAI (BlenderBot 2.0 3B)
