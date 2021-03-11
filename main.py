from pypresence import Presence
import random
import time
import sys
import psutil


if sys.argv[1] == "story":
    client_id = "816294087845347358"
    RPC = Presence(client_id)
    RPC.connect()

    images = [
        "crimson",
        "blue",
        "emerald"
    ]

    texts = [
        "Grimoire of Crimson",
        "Grimoire of Blue",
        "Grimoire of Emerald"
    ]

    firstLines = [
        "His colour.",
        "Her colour.",
        "Another's colour."
    ]

    secondLines = [
        "A crimson red... like the fury within.",
        "A soft blue... like the tranquility within.",
        "A bright emerald... like the caringness within."
    ]

    urls = [
        "https://muxiv.net/album/3171532",
        "https://muxiv.net/album/3358118",
        "https://muxiv.net/album/3390074"
    ]

    while True:

        indexes = [0, 1, 2]
        i = random.choice(indexes)
        image = images[i]
        firstLine = firstLines[i]
        secondLine = secondLines[i]
        text = texts[i]
        url = urls[i]

        buttons = [
            {
                "label": "Current Project",
                "url": "https://github.com/NovaGM"
            },
            {
                "label": text,
                "url": url
            }
        ]

        print(image)
        print(firstLine)
        print(secondLine)
        print(text)
        print(url)
        print("\n")

        RPC.update(details=firstLine, state=secondLine,
                   large_image=image, large_text=text, buttons=buttons)

        time.sleep(15)

if sys.argv[1] == "fragments":
    client_id = "817484578213593121"
    RPC = Presence(client_id)
    RPC.connect()

    firstLines = [
        "The world falling into fragments, slowly.",
        "These fragments, shattered pieces of what once was...",
        "Until one day... man will unravel the long lost secrets.",
        "The pieces will be put together to form a whole.",
        "At long last, it will be put to rest.",
        "Collectively, the story will be waved goodbye."
    ]

    secondLines = [
        "Reality collapsing at the seams.",
        "are now spread around. Never to be found again.",
        "Man will find a way to put the pieces back together.",
        "And as such, the story will be complete.",
        "Complete. Never to be spoken of again.",
        "Or perhaps, it will be just the individual who happily waves."
    ]

    while True:
        indexes = [0, 1, 2, 3, 4, 5]
        for i in range(len(indexes)):
            # print(i)
            # time.sleep(1)
            firstLine = firstLines[i]
            secondLine = secondLines[i]

            print(firstLine)
            print(secondLine)
            print("\n")

            RPC.update(details=firstLine, state=secondLine)

            time.sleep(15)

if sys.argv[1] == "sys":
    client_id = "817487250153144320"
    RPC = Presence(client_id, pipe=0)
    RPC.connect()

    while True:
        cpu_per = round(psutil.cpu_percent(), 1)
        mem = psutil.virtual_memory()
        mem_per = round(psutil.virtual_memory().percent, 1)
        print(RPC.update(details="RAM: " + str(mem_per) +
                         "%", state="CPU: " + str(cpu_per) + "%"))
        time.sleep(15)
