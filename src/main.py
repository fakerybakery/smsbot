from flask import Flask, request
import argparse
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, Conversation, ConversationalPipeline
import torch
from twilio.twiml.messaging_response import MessagingResponse
import sys
from termcolor import colored, cprint
serverlog = colored('[SYSTEM LOG] - ', 'red', attrs=['bold'])
incoming = colored('[INCOMING MESSAGE] - ', 'green', attrs=['bold'])
outgoing = colored('[OUTGOING MESSAGE] - ', 'blue', attrs=['bold'])
print(serverlog + 'Server Started!', file=sys.stderr)


parser = argparse.ArgumentParser(
    description="Process chatbot variables. for help run python bot.py -h"
)
parser.add_argument(
    "-s",
    "--steps",
    type=int,
    default=30,
    help="Number of steps to run the Dialogue System for",
)

args = parser.parse_args()
#tokenizer = AutoTokenizer.from_pretrained("facebook/blenderbot-400M-distill")
tokenizer = AutoTokenizer.from_pretrained("facebook/blenderbot-3B")
#model = AutoModelForSeq2SeqLM.from_pretrained("facebook/blenderbot-400M-distill")
model = AutoModelForSeq2SeqLM.from_pretrained("facebook/blenderbot-3B")

app = Flask(__name__)


@app.route("/bot", methods=["POST"])
def bot():
    for step in range(args.steps):
        incoming_msg = request.values.get("Body", "").lower()
        
        new_user_input_ids = tokenizer.encode(
            incoming_msg + tokenizer.eos_token, return_tensors="pt"
        )
        bot_input_ids = (
            torch.cat([chat_history_ids, new_user_input_ids], dim=-1)
            if step > 0
            else new_user_input_ids
        )
        chat_history_ids = model.generate(
            bot_input_ids, max_length=3000, pad_token_id=tokenizer.eos_token_id
        )

        resp = MessagingResponse()
        msg = resp.message()
        answ = (
            f"{tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-2]:][0], skip_special_tokens=True)}"
        )
        if (incoming_msg.lower() == "goodbye") or ("goodbye" in incoming_msg.lower()):
            answ = "[Your session has been ended.] You can reinitiate your session at any time by texting 'Hello' or calling us to reallocate resources and reinitiate your session. This free session was sponsered by A.I. Chatbot."
        msg.body(answ)
        #answ = str(
        #    f"{tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-2]:][0], skip_special_tokens=True)}"
        #)
        #print(answ)
        #return answ
        print(incoming + '"' + incoming_msg + '"', file=sys.stderr)
        print(outgoing + '"' + str(answ) + '"', file=sys.stderr)

        if (request.values.get("StringAnsw", "").lower() == "yes"):
            return answ
        return str(resp)
@app.after_request
def add_header(response):
    response.cache_control.max_age = 1
    return response


if __name__ == "__main__":
    #app.run()
    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)
