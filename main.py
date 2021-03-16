from pypresence import Presence
import random
import time
import sys
import psutil

client_id = "816294087845347358"
RPC = Presence(client_id)
RPC.connect()


if sys.argv[1] == "story":
    data = [
        {
            "image": "crimson",
            "text": "Grimoire of Crimson",
            "first": "His colour.",
            "second": "A crimson red... like the fury within.",
            "url": "https://muxiv.net/album/3171532"
        },
        {
            "image": "blue",
            "text": "Grimoire of Blue",
            "first": "Her colour.",
            "second": "A soft blue... like the tranquility within.",
            "url": "https://muxiv.net/album/3358118"
        },
        {
            "image": "emerald",
            "text": "Grimoire of Emerald",
            "first": "Another's colour.",
            "second": "A bright emerald... like the caringness within.",
            "url": "https://muxiv.net/album/3390074"
        },
    ]

    while True:
        c = random.choice(data)

        buttons = [
            {
                "label": "Current Project | LoggerTS",
                "url": "https://github.com/keanuplayz/LoggerTS"
            },
            {
                "label": c["text"],
                "url": c["url"]
            }
        ]

        print(c["image"])
        print(c["first"])
        print(c["second"])
        print(c["text"])
        print(c["url"])
        print("\n")

        RPC.update(details=c["first"], state=c["second"],
                   large_image=c["image"], large_text=c["text"], buttons=buttons)

        time.sleep(15)

if sys.argv[1] == "fragments":
    data = [
        {
            "first": "The world falling into fragments, slowly.",
            "second": "Reality collapsing at the seams."
        },
        {
            "first": "These fragments, shattered pieces of what once was...",
            "second": "are now spread around. Never to be found again."
        },
        {
            "first": "Until one day... man will unravel the long lost secrets.",
            "second": "Man will find a way to put the pieces back together."
        },
        {
            "first": "The pieces will be put together to form a whole.",
            "second": "And as such, the story will be complete."
        },
        {
            "first": "At long last, it will be put to rest.",
            "second": "Complete. Never to be spoken of again."
        },
        {
            "first": "Collectively, the story will be waved goodbye.",
            "second": "Or perhaps, it will be just the individual who happily waves."
        }
    ]

    while True:
        for i in data:
            firstLine = i["first"]
            secondLine = i["second"]
            print(firstLine)
            print(secondLine)
            print("\n")
            RPC.update(details=firstLine, state=secondLine)
            time.sleep(15)

if sys.argv[1] == "sys":
    while True:
        cpu_per = round(psutil.cpu_percent(), 1)
        mem = psutil.virtual_memory()
        mem_per = round(psutil.virtual_memory().percent, 1)
        print(RPC.update(details="RAM: " + str(mem_per) +
                         "%", state="CPU: " + str(cpu_per) + "%"))
        time.sleep(15)
