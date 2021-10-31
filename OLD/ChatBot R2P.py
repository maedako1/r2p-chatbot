from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from flask import Flask, render_template, request


app = Flask(__name__)


bot = ChatBot("chatbot", read_only=False, 
              logic_adapters=[ 
                              {"import_path":"chatterbot.logic.BestMatch",
                               "default_response":"Sorry, I don't have an answer",
                               "maximum_similarity_threshold": 0.8
                               }
                              ])

list_to_train = [
                "hi",
                "hi there",
                "what's your name?",
                "I'm a chatbot",
                "How are you?",
                "I am good",
                "What's your job?",
                "I'm here to answer your questions",
                "Where is T&E manual?",
                "Please refer to this site  https://alcon365.sharepoint.com/sites/InSight/SitePages/289/GPO/T%26E/TnE-JAPAN.aspx?cid=529ac87e-d98f-4cf8-afb8-2382fac22ece",
                "When is payment date?",
                "Please refer to this site  https://alcon365.sharepoint.com/:w:/r/sites/InSight/_layouts/15/Doc.aspx?sourcedoc=%7B128634DB-39C4-4E53-84F0-672C95CA4D19%7D&file=%E6%94%AF%E6%89%95%E6%97%A5%E7%A2%BA%E8%AA%8D%E6%96%B9%E6%B3%953.docx&action=default&mobileredirect=true",
                "支払い日はいつですか",
                "Please refer to this site   https://alcon365.sharepoint.com/:w:/r/sites/InSight/_layouts/15/Doc.aspx?sourcedoc=%7B128634DB-39C4-4E53-84F0-672C95CA4D19%7D&file=%E6%94%AF%E6%89%95%E6%97%A5%E7%A2%BA%E8%AA%8D%E6%96%B9%E6%B3%953.docx&action=default&mobileredirect=true",
                 "ベンダー登録",
                 "Please refer to Procurement sharepoint site.",
    ]

list_trainer = ListTrainer(bot)

list_trainer.train(list_to_train)

@app.route("/")
def main():
  return render_template("index.html")

# while True:
#   user_response = input("User: ")
#   print("Chatbot: " + str(bot.get_response(user_response)))


@app.route("/get")
def get_chatbot_response():
  userText = request.args.get("userMessage")
  return str(bot.get_response(userText))


if __name__ == "__main__":
  app.run()