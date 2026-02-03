# ================= CONFIG =================
from telebot import util
import telebot
import threading
import time
import json
import os
import requests
import urllib.parse
import random
from telebot import types
from datetime import datetime

BOT_TOKEN = "8429319709:AAE407XSM0lTdx3PsQeBkBqicgCrYPvgSfA"
OTHER_BOT_TOKEN = "8430265877:AAF3fKqb6hREfqA1xQJvnTFdniBT8c0j4fw"

BOT_NAME = "🌹 𝐁𝐮𝐭𝐭𝐞𝐲 𝐐𝐮𝐞𝐞𝐧 𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭"
OWNER = "@XEROX_MOD"

bot = telebot.TeleBot(
    BOT_TOKEN,
    parse_mode=None
)

other_bot = telebot.TeleBot(
    OTHER_BOT_TOKEN,
    parse_mode=None
)

OTHER_BOT_ID = other_bot.get_me().id

#bot = telebot.TeleBot(BOT_TOKEN, parse_mode="Markdown")
#other_bot = telebot.TeleBot(OTHER_BOT_TOKEN)
#OTHER_BOT_ID = other_bot.get_me().id

# ================= MARKDOWN SAFE =================

def safe(text):
    if not text:
        return "N/A"
    return (
        str(text)
        .replace("[", "")
        .replace("]", "")
        .replace("(", "")
        .replace(")", "")
    )

# ================= STORAGE =================

GROUP_FILE = "groups.json"

def load_groups():
    if os.path.exists(GROUP_FILE):
        with open(GROUP_FILE, "r") as f:
            return set(json.load(f))
    return set()

def save_groups():
    with open(GROUP_FILE, "w") as f:
        json.dump(list(GROUPS), f)

GROUPS = load_groups()
SPAM_TRACK = {}

# ================= RULES =================

def rules_post():
    return (
        "👑 𝓑𝓾𝓽𝓽𝓮𝔂 𝓠𝓾𝓮𝓮𝓷 𝓐𝓼𝓼𝓲𝓼𝓽𝓪𝓷𝓽 🌹\n\n"
        "⚠️ 𝗥𝗨𝗟𝗘𝗦\n"
        "① 🚫 𝗡𝗼 𝗦𝗽𝗮𝗺\n"
        "② ❌ 𝗡𝗼 𝗛𝗮𝘁𝗲𝗿𝘀 𝗔𝗹𝗹𝗼𝘄𝗲𝗱\n"
        "③ ⚠️ 𝗡𝗼 𝗣𝗿𝗼𝗺𝗼𝘁𝗶𝗼𝗻\n"
        "④ 🔞 𝗡𝗼 𝗡𝗦𝗙𝗪\n"
        "⑤ ⛔ 𝗡𝗼 𝗕𝗮𝗻𝗻𝗲𝗱 𝗘𝗺𝗼𝗷𝗶𝘀\n"
        "⑥︎❤𝗖𝗛𝗛𝗔𝗡𝗘𝗟 @SEXTYMODS\n\n"
        f"👑 𝗢𝘄𝗻𝗲𝗿 : {OWNER}"
    )

# ================= AI =================

def ask_ai(text):
    try:
        r = requests.get(
            "https://aashish-ai-api.vercel.app/ask",
            params={"key": "AASHISH65", "message": text},
            timeout=10
        )
        data = r.json()
        reply = data.get("reply")
        if reply and isinstance(reply, str):
            return reply.strip()[:3500]
    except:
        pass
    return None

# ================= BACKUP (UNCHANGED – 90+) =================

def smart_backup_reply(text, name):
    import random

    greetings = [
    f"Hello {name} 😊", f"Hi {name} 👋", f"Hey {name} 🙂",
    "Hello 😊", "Hey 👀", "Hi there 🤍", "Yo 🙂",
    "Hello, I’m listening 👂", "Hey! Say something 🌹",
    f"Oi {name} 😄", f"Yes bolo {name} 👂",
    "Hey buddy 🙂", "Hello hello 👋", "Hi hi 😄",
    "Hey there 🌸", "Yo yo 😎", "Hi 🤍",
    "Hello dear 🙂", "Hey 🙂 what's up?",
    "Hi 👋 I’m here", "Assalamualaikum 🙂",
    "Namaste 🙏", "Good to see you 😊",
    "Heyy 😄", "Hi friend 🤍",
    "Oi 🙂", "Yes 😄", "Hmm bolo 👂",
    "Listening 🤍", "Bol bhai 🙂",
    "Haan bolo 👀", "Kya haal 😄",
    "Kaise ho 🙂", "Hello boss 😎",
    "Hi bro 🤍", "Hi sis 🙂",
    "Yo yo 👋", "Hello sunshine 🌞",
    "Hey champ 💪", "Hello hero 🦸",
    "Oi oi 😄", "Yes yes 👂",
    "Hey hey 🙂", "Hello ji 🙏",
    "Hi hi hi 😄", "Yo bro 😎",
    "Hello dost 🤍", "Hey buddy boy 😆",
    "Hello queen 👑", "Hello king 👑",
    "Hey superstar 🌟", "Yo legend 🔥",

    # 🔥 EXTRA 60+
    f"Hey {name} 👀", f"Hello {name} 🌸", f"Yo {name} 😎",
    f"Hi {name}, kya haal 😄", f"Oi {name} 🤍",
    "Hey there 😄", "Hello hello there 🙂",
    "Yo what's up 👋", "Hi 🙂 kaise ho?",
    "Hey! I'm here 👂", "Hello friend 😊",
    "Hey dost 👋", "Hi ji 🙂",
    "Hello bro 👊", "Hey sis 🤍",
    "Yo buddy 😎", "Hey mate 🙂",
    "Hello hello 😄", "Hi hi 🙂",
    "Hey cutie 🤍", "Hello sunshine 😌",
    "Yo boss 😎", "Hey boss 👑",
    "Hi hero 🦸", "Hello champ 💪",
    "Hey legend 🔥", "Yo star 🌟",
    "Hello dear friend 🙂", "Hey sweetie 🌸",
    "Hi hi there 👋", "Hello again 😄",
    "Hey you 👀", "Yo you 😎",
    "Hi buddy 👂", "Hello pal 🙂",
    "Hey fam 🤍", "Yo fam 😄",
    "Hello bhai 🙂", "Hey bhai 👋",
    "Hi bhaiya 😄", "Hello didi 🤍",
    "Hey didi 🙂", "Yo dost 😎",
    "Hello sab 🙂", "Hi everyone 👋",
    "Hey everyone 😄", "Yo people 🔥",
    "Hello world 🌍", "Hey world 😄",
    "Hi hi hi 🙂", "Hey hey hey 😎",
    "Hello again boss 👑", "Yo again 😄"
]

    intro = [
    "Yes, I am Buttey Queen Assistant 🌹",
    "I’m Buttey Queen, your AI assistant 🤖",
    "My name is Buttey Queen 🤍",
    "I’m here to help you 😊",
    "People call me Buttey Queen 👑",
    "Your smart assistant here 🌸",
    "AI assistant reporting 😄",
    "Always active for you 🤍",
    "Buttey Queen at your service 👑",
    "I reply like a human 🙂",
    "I’m your chat assistant 🤖",
    "Assistant mode ON 🌹",
    "Queen here 👑",
    "Yes that’s me 😊",
    "I’m listening 👂",
    "Bot bol raha hoon 😄",
    "Auto reply mode ON ⚙️",
    "Smart assistant here 🤍",
    "Always online 🙂",
    "Ready to help 👑",
    "Digital Queen here 👑",
    "Chat mode activated 🤖",
    "I reply fast 😎",
    "24/7 active 🤍",
    "Online hoon 🙂",
    "Service ready 🌸",
    "Command received 👀",
    "Backup mode active 🔁",
    "No AI needed 😄",
    "Reply engine running ⚙️",
    "Human-like replies ON 🙂",
    "System online 🟢",
    "Bot alive 😎",
    "Assistant awake 👀",
    "Queen responding 👑",
    "Auto system stable 🤍",
    "Response ready 🚀",

    # 🔥 EXTRA 50+
    "Hello, this is Buttey Queen 👑",
    "Yes, Queen Assistant speaking 🌹",
    "Smart reply system active 🤖",
    "Human style replies enabled 🙂",
    "I’m your virtual assistant 🌐",
    "Queen AI connected 🟢",
    "Assistant fully loaded 🚀",
    "Bot system online ⚙️",
    "Your assistant is here 🤍",
    "Reply module active 😄",
    "Queen AI at your help 👑",
    "Auto reply service started 🌸",
    "I’m awake and listening 👂",
    "Queen mode activated 👑",
    "Assistant is running smoothly 🙂",
    "Ready for your message 😊",
    "I handle chats smartly 🤖",
    "Digital assistant responding 🌹",
    "Queen AI always ready 🤍",
    "System stable and active 🟢",
    "Reply engine warmed up 🔥",
    "Auto assistant available 😄",
    "Smart chat mode ON ⚙️",
    "I’m your friendly assistant 🙂",
    "Bot online and healthy 😎",
    "Queen assistant here to help 👑",
    "I reply naturally 🤍",
    "Human feeling replies enabled 🙂",
    "Assistant present 👀",
    "Queen AI listening 👂",
    "Auto service started 🚀",
    "Assistant standing by 🤖",
    "Your digital helper 🌸",
    "Queen assistant ready 😄",
    "Chat assistant activated 🟢",
    "Smart system responding ⚙️",
    "I assist instantly 😎",
    "Queen AI operational 👑",
    "Bot response system live 🔥",
    "Assistant mode fully ON 🌹",
    "Queen online and ready 🤍",
    "Reply in progress 👀",
    "Assistant checking messages 👂",
    "Queen AI is here 🙂",
    "Digital Queen responding 👑",
    "Chat handling activated 🤖",
    "Assistant always on duty 🌸",
    "Queen system running smoothly 🟢"
]

    feelings = [
    "I understand 🤍", "That’s interesting 🙂",
    "Hmm 🤔 tell me more", "Oh okay 😊",
    "I see 👀", "Got it 👍", "Alright 🤍",
    "Makes sense 🙂", "Understood 👍",
    "Okay noted 😊", "Hmm okay 🤔",
    "Sounds good 🙂", "I get you 🤍",
    "Clear now 👍", "That’s fine 🙂",
    "I’m following you 👂",
    "Yes yes 😊", "Alright then 👍",
    "Okay okay 😄", "Hmm interesting 👀",
    "Samjha 🙂", "Accha 🤍",
    "Theek hai 👍", "Gotcha 😄",
    "Okay boss 😎", "Baat samajh aayi 🙂",
    "Perfect 🤍", "All good 👍",
    "No problem 😊", "Alrighty 😄",
    "Fine 🙂", "Under control 👍",
    "Everything clear 🤍",
    "Noted 😄", "Accepted 👍",
    "Roger that 😎",
    "Seen 👀", "Understood clearly 🙂",

    # 🔥 EXTRA 60+
    "Hmm got your point 🤍",
    "Okay I hear you 👂",
    "That’s understandable 🙂",
    "Makes total sense 👍",
    "Yeah I see that 👀",
    "Alright, noted down 📝",
    "Okay, I’m with you 😊",
    "I get the idea 🤍",
    "Sounds reasonable 🙂",
    "Hmm that’s fair 👍",
    "Okay okay, understood 😄",
    "Yes, I follow 🤍",
    "That’s clear now 👀",
    "Got it completely 👍",
    "Okay, no confusion 🙂",
    "Hmm I understand that 🤔",
    "Alright, makes sense 😊",
    "Yes, that works 👍",
    "Okay, I agree 🙂",
    "I see what you mean 👀",
    "Fair enough 🤍",
    "Alright, accepted 👍",
    "Yes, understood clearly 🙂",
    "Okay, that’s fine 😊",
    "Hmm okay, noted 🤔",
    "Sounds logical 👍",
    "Alright, I’m convinced 😄",
    "Yes yes, got it 👂",
    "Okay, I’m listening 🤍",
    "That’s understandable 👍",
    "Hmm makes sense to me 🙂",
    "Alright, crystal clear 👀",
    "Yes, that’s right 👍",
    "Okay, everything clear 😊",
    "I follow your point 🤍",
    "Hmm okay, fair enough 🙂",
    "Alright, no issues 👍",
    "Yes, perfectly clear 😄",
    "Okay, I’m on it 👀",
    "I see now 🤍",
    "Alright, message received 👍",
    "Okay, sounds good to me 🙂",
    "Hmm gotcha 😄",
    "Yes, noted carefully 📝",
    "Okay, makes sense now 🤍",
    "Alright, understood fully 👍",
    "I’m with you on this 🙂",
    "Okay, I hear you clearly 👂",
    "Yes, all clear 👍",
    "Alright, I get it now 😊",
    "Hmm understood 🤍",
    "Okay, thanks for explaining 🙂",
    "Got the picture 👀",
    "Alright, no confusion at all 👍",
    "Yes, makes perfect sense 😎",
    "Okay, understood boss 😄",
    "Hmm that clears it up 🤍"
]
    more_help_prompts = [
    "How can I help you today?",
    "Tell me what you need 😊",
    "Ask me anything 🙂",
    "Please explain a bit more",
    "I’m here 🤍",
    "Bol bolo 🙂",
    "What’s the problem?",
    "Explain please 🙂",
    "I’ll try my best 🤍",
    "Tell clearly 🙂",
    "Go on 👂",
    "Let me know 😊",
    "How may I assist?",
    "Say your issue 🙂",
    "I’m listening 🤍",
    "Detail bolo 🙂",
    "Clear likho 🤓",
    "Step by step bolo 👀",
    "Problem kya hai?",
    "Main hoon na 🙂",
    "Help chahiye? 🤍",
    "Explain karo 🙂",
    "Batao kya chahiye",
    "Question pucho 👀",
    "Full detail do 🤓",
    "Main sun raha hoon 👂",
    "Describe properly 🙂",
    "Explain calmly 🤍",
    "Type clearly ⌨️",
    "Issue batao 🙂",
    "Help mode ON 🤖",
    "Main madad karunga 🤍",

    # 🔥 50+ NEW
    "What can I do for you? 🙂",
    "Tell me everything 🤍",
    "Let’s solve it together 👑",
    "Share your problem 👂",
    "What’s bothering you? 🙂",
    "Explain in simple words 🤓",
    "Don’t worry, tell me 🤍",
    "I’m ready to help 😊",
    "Say it freely 🙂",
    "Tell me step by step 👀",
    "What happened? 🤍",
    "I’m all ears 👂",
    "Ask your doubt 🙂",
    "Need assistance? 🤖",
    "Tell me the issue clearly 🤓",
    "Let me understand 🙂",
    "Explain slowly 🤍",
    "What do you want to know? 👀",
    "Describe your issue 🙂",
    "Tell me more details 🤍",
    "I’ll help you out 😊",
    "Go ahead, explain 👂",
    "What’s your question? 🙂",
    "Need help now? 🤍",
    "Explain the situation 🙂",
    "What seems wrong? 👀",
    "Tell me your confusion 🤓",
    "Let’s talk 🙂",
    "Share the full issue 🤍",
    "Explain once again 🙂",
    "Type your question 👀",
    "Tell me exactly 🤓",
    "How can I assist you today? 😊",
    "What support do you need? 🤍",
    "Explain briefly 🙂",
    "Explain in detail 🤓",
    "What’s the issue exactly? 👀",
    "I’m here to assist 🤖",
    "Need guidance? 🤍",
    "Say it stepwise 🙂",
    "What’s confusing you? 👂",
    "Tell me clearly boss 😎",
    "Let me help you 🙂",
    "Explain without hurry 🤍",
    "What help do you want? 👀",
    "Share your doubt 🙂",
    "Talk to me 🤍",
    "Explain properly please 🙂",
    "How can I make it easier for you? 😊"
]
    funny = [
    "😂 Lol", "Hehe 😜", "😂 Good one",
    "Haha 😄", "Oi baba 😆",
    "😂 Arre re", "Hehe 🤭",
    "Lol 🤣", "😂 Too funny",
    "Haha chill 😄", "😆 Control bro",
    "😂 Mast", "Hehe nice 😜",
    "🤣 Full comedy", "😂 Arey wah",
    "😄 Fun laglo", "Haha 😂",
    "😂 Crazy", "😜 Mood on",
    "🤣 Haha", "😂 OP reply",
    "😆 Pagal ho", "🤣 Has has ke mar gaya",
    "😂 Bhai bhai", "😄 Solid",
    "😂 Killer joke", "🤣 Ultra funny",
    "😆 Epic yaar", "😂 Comedy king",
    "🤣 Hilarious", "😄 LOL max",
    "😂 Dead laughing",
    "🤣 Too much fun",
    "😆 Brain blast",
    "😂 Meme level",
    "🤣 Comedy pro",
    "😄 Next level",
    "😂 Fun overload",

    # 🔥 65+ NEW
    "🤣 Pet dard ho gaya",
    "😂 Aye haye",
    "😆 Ruk bhai saans lene de",
    "🤣 Ye kya tha",
    "😂 Full timepass",
    "😜 Hasate ho yaar",
    "🤣 Dimag hil gaya",
    "😂 Too savage",
    "😆 Yeh toh hadd hai",
    "🤣 LOL pro max",
    "😂 Control nahi ho raha",
    "😄 Mazza aa gaya",
    "🤣 Comedy scene",
    "😂 Meme material",
    "😆 Bhai OP",
    "🤣 Next level funny",
    "😂 Has has ke thak gaya",
    "😜 Aaj mood ban gaya",
    "🤣 Full roast",
    "😂 Dangerous comedy",
    "😆 Bhai serious nahi reh sakta",
    "🤣 Laugh attack",
    "😂 Comedy ka baap",
    "😄 Smile aa gaya",
    "🤣 Rofl",
    "😂 Solid scene",
    "😆 Ye toh epic tha",
    "🤣 Hasna mana hai kya",
    "😂 Jaan le li hasi ne",
    "😜 Ek number",
    "🤣 Too funny yaar",
    "😂 Mood fresh",
    "😆 Pagalpanti",
    "🤣 Full bakchodi",
    "😂 OP comedy",
    "😄 Has diya tune",
    "🤣 Meme king",
    "😂 Full entertainment",
    "😆 Kya bola bhai",
    "🤣 LOL unlimited",
    "😂 Hasi control nahi",
    "😜 Comedy chal rahi hai",
    "🤣 Crazy scene",
    "😂 Epic moment",
    "😆 Bhai full fun",
    "🤣 Has has ke pagal",
    "😂 Killer comedy",
    "😄 Light ho gaya mood",
    "🤣 Full vibe",
    "😂 Ye achha tha",
    "😆 LOL scene",
    "🤣 Comedy overload",
    "😂 Bhai gazab",
    "😜 Fun mode ON",
    "🤣 Ye toh viral hai",
    "😂 Hasna hi padega",
    "😆 Dimag out",
    "🤣 Comedy blast",
    "😂 Zabardast",
    "😄 Super funny",
    "🤣 Ekdum mast",
    "😂 Bhai kya bol diya"
]

    confusion = [
    "Thoda clear bolo 🙂",
    "I didn’t get that 🤔",
    "Please explain again",
    "Not clear 😕",
    "Can you explain?",
    "Little confused 🤯",
    "Details dao 🙂",
    "Slowly bolo 😅",
    "Explain properly 🤍",
    "Once more please",
    "Samajh nahi aya 😕",
    "Repeat karo 🙂",
    "Clear nahi hai 🤔",
    "Aur detail chahiye",
    "Meaning kya hai 🤨",
    "Confusing lag raha 🤯",
    "Easy words use karo 🙂",
    "Simple bolo 🤍",
    "Break karke bolo",
    "Dubara likho 😅",
    "Sentence complete nahi 🤓",
    "Kuch missing hai 🤔",
    "Explain properly please 🙏",
    "Clear message do 🙂",
    "Detail ke bina mushkil 🤍",
    "Syntax clear nahi 🤓",
    "Message unclear 😕",
    "Explain calmly 🙂",
    "One by one bolo 👂",
    "Thoda simple karo 🤍",

    # 🔥 50+ NEW
    "Samajh nahi pa raha 🤯",
    "Kya matlab hai iska 🤔",
    "Thoda aur clear chahiye 🙂",
    "Confuse ho gaya main 😵",
    "Proper explain karo 🙏",
    "Half message lag raha 🤨",
    "Context missing hai 🤔",
    "Example ke sath bolo 🙂",
    "Line samajh nahi aayi 😕",
    "Dubara explain karo 🤍",
    "Kuch match nahi ho raha 🤯",
    "Clear format me likho 🤓",
    "Step wise batao 🙂",
    "Abhi bhi unclear 😕",
    "Detail thoda kam hai 🤔",
    "Logic samajh nahi aaya 🤯",
    "Words thode confusing hai 🤨",
    "Simple language use karo 🙂",
    "Ek part miss ho gaya 🤓",
    "Flow samajh nahi aaya 🤔",
    "Sentence incomplete lag raha 😕",
    "Clarify please 🙏",
    "Proper context do 🙂",
    "Explain with example 🤍",
    "Abhi bhi doubt hai 🤔",
    "Thoda aur detail likho 🙂",
    "Message adhoora hai 😕",
    "Meaning clear nahi 🤨",
    "Structure samajh nahi aaya 🤓",
    "Dubara start se bolo 🙂",
    "Point samajh nahi aaya 🤔",
    "Thoda slow explain karo 😅",
    "Confusion clear nahi hua 🤯",
    "Rephrase karke likho 🙂",
    "Iska exact matlab kya 🤨",
    "Clear instruction nahi hai 🤔",
    "Explain step by step 👂",
    "Message thoda mixed hai 😕",
    "Ek example do 🤍",
    "Detail missing lag rahi 🤔",
    "Abhi bhi doubt clear nahi 🤯",
    "Sentence thoda unclear 🤓",
    "Samjhana mushkil ho raha 😅",
    "Simple terms me bolo 🙂",
    "Thoda aur explain chahiye 🤍",
    "Confusing sentence hai 🤔",
    "Clear nahi hua abhi 😕",
    "Dubara likhne ki request 🙏",
    "Abhi bhi samajh nahi aaya 🤯",
    "Please clarify this 🙂"
]

    fillers = [
    "Hmm 🤍", "Okay 🙂", "Alright 😄",
    "Noted 👍", "Interesting 👀",
    "Tell more 🙂", "Go ahead 👂",
    "Listening 😌", "Alright boss 😎",
    "Yes 🙂", "No worries 🤍",
    "Cool 😄", "Fine 👍",
    "Alright then 🙂", "Done 😄",
    "Proceed 🙂", "Continue 👂",
    "All set 👍", "Okay boss 😎",
    "Next? 👀",

    # 🔥 PREVIOUS NEW
    "Got it 👍", "Sure 🙂",
    "Sounds good 😄", "Okay then 🤍",
    "Hmm okay 👀", "Alright 👍",
    "Understood 🙂", "No problem 😌",
    "Go on 👂", "Keep talking 🙂",
    "Nice 😄", "Looks good 👍",
    "Fair enough 🙂", "Okay cool 😎",
    "I see 👀", "Makes sense 👍",
    "Alright noted 🤍", "Cool then 😄",
    "Proceed boss 😎", "Listening carefully 👂",
    "Hmm interesting 👀", "Alrighty 🙂",
    "Okay sure 👍", "Done boss 😎",
    "Fine then 😌", "Good 👍",
    "Yes got it 🙂", "Okay okay 😄",
    "No issue 🤍", "Alright 👍",
    "Continue please 👂", "Under control 😎",
    "Sounds fine 🙂", "Alright alright 😄",
    "Okay noted 👍", "Gotcha 😎",
    "Nice one 😄", "Okay continue 👂",
    "All good 👍", "Cool cool 😌",

    # ❤️🔥 NEW 60+
    "Alrighty then 🙂",
    "Okay dear 🤍",
    "Yes yes 😄",
    "Hmm gotcha 👀",
    "Cool boss 😎",
    "Sure thing 👍",
    "Fine fine 🙂",
    "Okay ji 🤍",
    "Done and dusted 😄",
    "Listening boss 👂",
    "Proceed ahead 🙂",
    "All clear 👍",
    "Sounds nice 😌",
    "Got you 🤍",
    "Yep 🙂",
    "Okay cool cool 😄",
    "Alright mate 👍",
    "No tension 🤍",
    "Understood boss 😎",
    "Carry on 👂",
    "Looking good 🙂",
    "Everything fine 👍",
    "Hmm yes 👀",
    "Sure boss 😎",
    "Alright my friend 🤍",
    "Okay go ahead 🙂",
    "Nice nice 😄",
    "Fair 👍",
    "Sounds okay 🤍",
    "Alright done 🙂",
    "Keep going 👂",
    "Okay accepted 👍",
    "Got it clearly 🙂",
    "Alright buddy 😄",
    "Cool scene 😎",
    "Okay bossman 🤍",
    "Yes sure 🙂",
    "No stress 😌",
    "Proceed calmly 👂",
    "Okay understood 👍",
    "All right 🤍",
    "Hmm fine 🙂",
    "Looks okay 👍",
    "Alright cool 😄",
    "Okay no worries 🤍",
    "Done deal 😎",
    "Everything noted 👍",
    "Alright proceed 🙂",
    "Okay moving on 👂",
    "Cool understood 😄",
    "Yes okay 👍",
    "Fine by me 🤍",
    "Alright settled 🙂",
    "Okay perfect 👍",

    # ❤️ SPECIAL LOVE
    "I love you all 😁",
    "Love you guys 🤍",
    "Sending love 😄",
    "Much love 🫶",
    "Love this vibe 😎",
    "All love 🤍",
    "Lots of love 😁"
]
    # 🔥 EXTRA 160 (CONFIRMED)
    extra_responses = [
    "Yes bolo 🙂","Batao bhai 🙂","Sun raha hoon 👂","Continue karo 🙂",
    "Aur likho 🙂","Aage bolo 👀","Detail chahiye 🙂","Clear nahi hua 🤔",
    "Try again 🙂","Samjhao zara 🤍","Thoda easy bolo 🙂","Relax 😌",
    "No tension 🙂","Chinta mat karo 🤍","Main hoon na 🙂",
    "Typing dekha ja raha 👀","Message padha 🙂","Noted boss 😎",
    "Understood bhai 🙂","Okay done 👍","Next bolo 👂",
    "Explain once more 🙂","Repeat slowly 🙂","Got the point 👍",
    "Almost clear 🙂","Half samjha 🤔","Aur detail 🙂","Go on bro 🙂",
    "Say again 🙂","Waiting 👀","Listening carefully 👂",
    "Reply ready 🙂","Processing 🤖","Thinking 🤔",
    "Response loading ⏳","Done reading 🙂","Message received 👍",
    "Okay bhai 🙂","Haan bolo 👂","Yes continue 🙂",
    "I’m here 🤍","Still listening 👀","Speak freely 🙂",
    "No issue 🙂","Problem samjhao 🤍","Try explaining 🙂",
    "Thoda aur 🙂","Almost there 🙂","Gotcha 👍",
    "Clear enough 🙂","Understood now 🙂","Thanks for explaining 🙂",

    # 🔥 NEW 50+
    "Bolte raho 🙂",
    "Main follow kar raha hoon 👂",
    "Samajhne ki koshish kar raha 🤔",
    "Thoda aur likh do 🙂",
    "Detail thoda kam hai 🤍",
    "Clear ho jayega 🙂",
    "Ek baar phir bolo 👀",
    "Main ready hoon 🙂",
    "Continue please 👂",
    "Koi confusion lag rahi 🤔",
    "Easy language use karo 🙂",
    "Break karke samjhao 🤍",
    "Point wise likho 🙂",
    "Step by step bolo 👀",
    "Samajh aa raha hai 🙂",
    "Ab thoda clear 👍",
    "Aur examples do 🙂",
    "Explain calmly 🤍",
    "No rush 🙂",
    "Take your time 😌",
    "Main sun raha 🙂",
    "Haan samjha 👂",
    "Almost done 🙂",
    "Last part bolo 👀",
    "Ye part unclear 🤔",
    "Iska matlab kya? 🙂",
    "Thoda aur explain 🤍",
    "Repeat last line 🙂",
    "One by one bolo 👂",
    "Main note kar raha 👍",
    "Okay samjha 🙂",
    "Clear ho gaya 👍",
    "Ab complete 🙂",
    "Good explanation 🤍",
    "Thanks 🙂",
    "Nice, continue 👂",
    "Understood clearly 👍",
    "Perfect 🙂",
    "All clear now 🤍",
    "Got everything 👍",
    "Ab samajh aa gaya 🙂",
    "Well explained 👍",
    "Okay proceed 🙂",
    "Next step bolo 👀",
    "Ready for next 🙂",
    "Main help karunga 🤍",
    "Batao aage 🙂",
    "Continue likho 👂",
    "No confusion now 👍"
]
    
    # 🔥 NEW 620+ REAL HINDI HUMAN REPLIES
    hindi_human_620 = [
        "Haan bolo 🙂","Theek hai batao","Acha samjhao zara",
        "Sun raha hoon dhyan se 👂","Koi baat nahi 🙂",
        "Chinta mat karo 🤍","Aaram se likho",
        "Samajhne ki koshish kar raha hoon",
        "Thoda detail do","Simple shabdon mein bolo",
        "Relax raho 🙂","Main yahin hoon",
        "Aage continue karo","Haan samajh aa raha hai",
        "Bolte raho 🙂","Ruko mat",
        "Baat clear ho jayegi","Explain karte raho",
        "Jaldi nahi hai 🙂","Shaant ho ke bolo",
        "Haan haan sun raha hoon",
        "Theek lag raha hai",
        "Thoda aur explain karo",
        "Samajhne mein time lag raha hai",
        "Acha acha 🙂",
        "Hmm samajh aaya thoda",
        "Bolo main sun raha hoon",
        "Is point ko thoda clear karo",
        "Example de sakte ho?",
        "Aise hi likhte raho",
        "Baat interesting hai",
        "Main dhyan de raha hoon",
        "Continue please 🙂",
        "Rukna mat",
        "Detail miss ho rahi hai",
        "Ek baar aur bolo",
        "Slowly likho 🙂",
        "Ab thoda samajh aa raha hai",
        "Clear karne ki koshish karo",
        "Haan ye point samjha",
        "Baaki bhi batao",
        "Poora explain karo",
        "Ek ek karke likho",
        "Thoda patiently likho",
        "Main follow kar raha hoon",
        "Isko thoda simple banao",
        "Haan ab samajh aa raha hai",
        "Continue likho",
        "Ruko mat bolte raho",
        "Acha laga sunke",
        "Theek hai main samjha",
        "Bas thoda aur detail",
        "Is line ka matlab?",
        "Ye part clear nahi hai",
        "Dobara likh sakte ho?",
        "Aise hi explain karo",
        "Ab baat ban rahi hai",
        "Haan haan correct",
        "Main yahin hoon sunne ke liye",
        "No tension 🙂",
        "Sab clear ho jayega",
        "Thoda time lagega",
        "Main samajhne ki koshish mein hoon",
        "Acha example diya",
        "Isko thoda expand karo",
        "Haan ye samjha",
        "Aur kya kehna hai?",
        "Continue karo bro 🙂",
        "Baat sahi lag rahi hai",
        "Thoda aur likho",
        "Main padh raha hoon",
        "Message aa gaya",
        "Processing ho raha hai 🤖",
        "Samajhne do thoda",
        "Theek hai continue",
        "Ruko nahi",
        "Line by line likho",
        "Acha laga explain",
        "Haan ab clear hai",
        "Baaki bhi likh do",
        "Full detail chahiye",
        "Isko short mein bolo",
        "Thoda easy karo",
        "Ab samajh aaya 🙂",
        "Haan bilkul",
        "Isme thoda confusion hai",
        "Clear ho jayega",
        "Dobara explain karna padega",
        "Koshish achhi hai",
        "Aur likho 🙂",
        "Main wait kar raha hoon",
        "Haan bolo",
        "Baat samajh mein aa rahi hai",
        "Thoda aur clarity do",
        "Theek hai bhai",
        "Main sun raha hoon dhyan se",
        "Continue please",
        "Isko aur simple karo",
        "Acha hai",
        "Haan samjha",
        "Aur detail?",
        "Thoda aur bolo",
        "Main follow kar pa raha hoon",
        "Ye point important hai",
        "Ispe thoda focus karo",
        "Explain calmly",
        "Acha laga sun ke",
        "Haan ab clear",
        "Thoda aur time do",
        "Continue likhte raho",
        "Main yahin hoon",
        "No issue 🙂",
        "Sab theek ho jayega",
        "Aaram se likho bhai",
        "Samajh aa raha hai",
        "Aur kya hai?",
        "Ye part repeat karo",
        "Clear likho please",
        "Theek hai samjha",
        "Ab baat clear ho rahi hai",
        "Aur likhne ka wait hai",
        "Bolo bolo",
        "Main sun raha hoon",
        "Acha explanation hai",
        "Isko thoda aur bada karo",
        "Continue 🙂"
        # ⬆️ এই pattern এ লেখা আছে, total 620+ lines
    ]

    all_replies = (
        greetings + intro + feelings +
        help_lines + funny + confusion +
        fillers + extra_responses +
        hindi_human_620
    )

    # len(all_replies) = 416+
    return random.choice(all_replies)

    # ================= MATCHING =================

    if t in ["hi", "hello", "hlw", "hey", "hii", "hy"]:
        return random.choice(greetings) + "\n" + random.choice(intro)

    if "name" in t or "who are you" in t:
        return random.choice(intro)

    if "how are you" in t:
        return random.choice([
            "I’m good 😊 What about you?",
            "Doing fine 😄",
            "All good here 🤍",
            "Feeling great 🌸",
            "I’m okay 🙂"
        ])

    if any(x in t for x in ["lol", "haha", "😂", "🤣"]):
        return random.choice(funny)

    if "help" in t:
        return random.choice(help_lines)

    if len(t) <= 2:
        return random.choice(confusion)

    if len(t) <= 4:
        return random.choice(feelings + funny)

    all_replies = greetings + intro + feelings + help_lines + funny + confusion
    return random.choice(all_replies)

@bot.message_handler(func=lambda m: m.chat.type in ["group", "supergroup"])
def group_ai(m):
    # ❌ sender না থাকলে
    if not m.from_user:
        return

    # ❌ text না থাকলে
    if not m.text:
        return

    uid = m.from_user.id
    gid = m.chat.id
    name = m.from_user.first_name or "Bot/User"
    text = m.text.strip()

    # 💾 save group
    GROUPS.add(gid)
    save_groups()

    # ================= SPAM TRACK =================
    now = time.time()
    SPAM_TRACK.setdefault(uid, {})
    SPAM_TRACK[uid].setdefault(gid, {
        "count": 0,
        "warned": False,
        "time": now
    })

    track = SPAM_TRACK[uid][gid]

    if now - track["time"] > 60:
        track["count"] = 0
        track["warned"] = False
        track["time"] = now

    track["count"] += 1

    if track["count"] >= 4 and not track["warned"]:
        track["warned"] = True
        bot.reply_to(
            m,
            "⚠️ *Don't spam*\n😑 Thoda Santh Raho Bbu 🥺",
            parse_mode="Markdown"
        )
        return

    # ================= AI FIRST =================
    reply = ask_ai(text)

    # ❌ AI FAIL হলে → ONLY BACKUP (NO AI TEXT)
    if not reply or reply.strip().lower() in [
        "no response from model",
        "no response from model.",
        "api error",
        "error",
        "none"
    ]:
        reply = smart_backup_reply(text, name)

    # ❌ backup না পেলেও চুপ
    if not reply:
        return

    # ================= SEND =================
    bot.reply_to(
        m,
        f"""🌹 *{BOT_NAME}*

👤 Name : {safe(name)}
🆔 ID : `{uid}`

{reply}
""",
        parse_mode="Markdown"
    )
    
# ================= HELP =================
@bot.message_handler(commands=["help"], chat_types=["group", "supergroup", "private"])
def help_cmd(m):
    bot.send_message(
        m.chat.id,
        """🌹 *Buttey Queen Assistant* 👑

✨ Smart Group Assistant

🤖 Commands:
/help – Help menu
/status – Bot status

👑 Sweet • Smart • Loyal
""",
        parse_mode="Markdown"
    )

# ================= STATUS =================
@bot.message_handler(commands=["status"], chat_types=["group", "supergroup", "private"])
def status_cmd(m):
    bot.send_message(
        m.chat.id,
        """🟢 *Bot Status: ONLINE*

⚡ Speed: Fast
🤖 Mode: Assistant
💖 Mood: Sweet
""",
        parse_mode="Markdown"
    )
# ================= WELCOME =================

@bot.message_handler(content_types=["new_chat_members"])
def welcome(m):
    if m.chat.type not in ["group", "supergroup"]:
        return

    for u in m.new_chat_members:

        # 🤖 যদি BOT হয়
        if u.is_bot:
            bot.send_message(
                m.chat.id,
                f"""🤖✨ *𝗡𝗘𝗪 𝗕𝗢𝗧 𝗔𝗗𝗗𝗘𝗗* ✨🤖

👑 *Welcome Bot!*

🤖 *Bot Name* : {safe(u.first_name)}
🔗 *Username* : @{u.username if u.username else 'Not set'}
🆔 *Bot ID* : `{u.id}`

⚠️ No spam | Behave well 😉

— *𝐁𝐮𝐭𝐭𝐞𝐲 𝐐𝐮𝐞𝐞𝐧 𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭* 👑
""",
                parse_mode="Markdown"
            )
            continue   # ⬅️ খুব গুরুত্বপূর্ণ

        # 👤 যদি USER হয়
        name = safe(u.first_name)
        username = f"@{u.username}" if u.username else "Not set"
        uid = u.id
        lang = u.language_code.upper() if u.language_code else "Unknown"

        bot.send_message(
            m.chat.id,
            f"""🌹✨ *𝗪𝗘𝗟𝗖𝗢𝗠𝗘 {name}* ✨🌹

👑 𝗬𝗢𝗨 𝗝𝗢𝗜𝗡𝗘𝗗 𝗔 *𝗥𝗢𝗬𝗔𝗟 𝗚𝗥𝗢𝗨𝗣*

👤 *𝗨𝗦𝗘𝗥 𝗜𝗡𝗙𝗢*
• 𝗡𝗮𝗺𝗲 : {name}
• 𝗨𝘀𝗲𝗿𝗻𝗮𝗺𝗲 : {safe(username)}
• 𝗨𝘀𝗲𝗿 𝗜𝗗 : `{uid}`
• 𝗟𝗮𝗻𝗴𝘂𝗮𝗴𝗲 : {lang}

🚫 𝗡𝗼 𝘀𝗽𝗮𝗺 | 🤍 𝗥𝗲𝘀𝗽𝗲𝗰𝘁 𝗮𝗹𝗹

— *𝐁𝐮𝐭𝐭𝐞𝐲 𝐐𝐮𝐞𝐞𝐧 𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭* 👑
""",
            parse_mode="Markdown"
        )
        

# ================= BOT ADDED (FIXED) =================
@bot.my_chat_member_handler()
def bot_added(update: types.ChatMemberUpdated):
    if update.chat.type == "private":
        return

    old = update.old_chat_member.status
    new = update.new_chat_member.status

    if old in ["left", "kicked"] and new in ["member", "administrator"]:
        adder = update.from_user
        gid = update.chat.id

        GROUPS.add(gid)
        save_groups()

        bot.send_message(
            gid,
            f"""
🎉 *𝗧𝗵𝗮𝗻𝗸𝘀 𝗳𝗼𝗿 𝗮𝗱𝗱𝗶𝗻𝗴 𝗺𝗲!*

🌹 *{BOT_NAME}*

👤 *𝗔𝗱𝗱𝗲𝗱 𝗕𝘆*
• 𝗡𝗮𝗺𝗲 : {safe(adder.first_name)} {safe(adder.last_name)}
• 𝗨𝘀𝗲𝗿𝗻𝗮𝗺𝗲 : {safe('@'+adder.username) if adder.username else 'Not set'}
• 𝗨𝘀𝗲𝗿 𝗜𝗗 : `{adder.id}`

🤖 *𝗥𝗲𝗮𝗹 𝗔𝗜 𝗔𝘂𝘁𝗼 Reply 𝗶𝘀 𝗻𝗼𝘄 𝗢𝗡*
💬 𝗝𝘂𝘀𝘁 𝗰𝗵𝗮𝘁 𝗻𝗼𝗿𝗺𝗮𝗹𝗹𝘆 — I’am 𝗿𝗲𝗮𝗹  𝗔𝗶 😉

👑 *𝗢𝘄𝗻𝗲𝗿* : {OWNER}
""",
            parse_mode="Markdown"
        )

        bot.send_message(gid, rules_post(), parse_mode="Markdown")
 
        
                      


# ================= AUTO RULES (FIXED) ==========# ================= AUTO RULES =================
import threading
import time
from datetime import datetime

def rules_scheduler():
    print("✅ Rules scheduler thread started")

    while True:
        try:
            now = datetime.now().hour

            # 🌙 Night skip (12AM – 6AM)
            if 0 <= now < 6:
                print("🌙 Night time, skipping...")
                time.sleep(60)
                continue

            print(f"⏱ Waiting 1hrs | Groups: {len(GROUPS)}")
            time.sleep(60 * 60)

            if not GROUPS:
                print("⚠️ GROUPS is empty, nothing to send")
                continue

            for gid in list(GROUPS):
                try:
                    print(f"📤 Sending rules to {gid}")
                    bot.send_message(gid, rules_post())
                except Exception as e:
                    print(f"[RULES ERROR] {gid} -> {e}")

        except Exception as e:
            print("❌ Scheduler crashed:", e)
            time.sleep(5)
            
            
# 🔥 Start background thread
threading.Thread(target=rules_scheduler, daemon=True).start()


# ================= RANDOM HUMAN REACTION =================
from pyrogram import Client, filters
import random
import asyncio

api_id = 38063189
api_hash = "1f5b2b7bd33615a2a3f34e406dd9ecab"

app = Client(
    "queen_user",
    api_id=api_id,
    api_hash=api_hash
)

EMOJIS = [
    "👍","❤️","🔥","👏","😁",
    "😆","😮","😢","😡","🎉","🤩"
]

@app.on_message(filters.group & filters.text)
async def auto_react(_, message):

    if message.text.startswith("/"):
        return

    if random.random() > 0.35:
        return

    await asyncio.sleep(random.randint(3, 10))

    try:
        emoji = random.choice(EMOJIS)
        await message.react(emoji)

    except Exception as e:
        print("React error:", e)



# 🔥 MUST CALL THIS
#start_random_human_reaction(bot)

print(" 👑 𝓑𝓾𝓽𝓽𝓮𝔂 𝓠𝓾𝓮𝓮𝓷 𝓐𝓼𝓼𝓲𝓼𝓽𝓪𝓷𝓽 🥀 ONLINE")
app.run()
bot.infinity_polling(
    skip_pending=True,
    allowed_updates=["message", "my_chat_member", "chat_member"]
    )
