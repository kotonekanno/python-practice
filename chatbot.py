from datetime import datetime

def hello():
    print("\nこんにちは！")
def time():
    now = datetime.now()
    print("\n",now)
def bye():
    print("\nさよなら")
    return None

commands = {
    "greet": hello,
    "time": time,
    "end": bye
}

def enter():
    cmd = input("\n操作を選んでください（greet / time / end）：")

    if cmd in commands:
        result = commands[cmd]()
        return result

    else: print("\n不正な操作")

while True:
    if enter() is None:
        break