def add(a,b): print(f"{a} + {b} = {a+b}")
def sub(a,b): print(f"{a} - {b} = {a-b}")
def mul(a,b): print(f"{a} × {b} = {a*b}")
def div(a,b): print(f"{a} ÷ {b} = {a/b}")

commands = {
    "add": add,
    "sub": sub,
    "mul": mul,
    "div": div
}

cmd = input("操作を選んでください（add/sub/mul/div）：")
a = int(input("1つ目の数字："))
b = int(input("2つ目の数字："))

if cmd in commands:
    commands[cmd](a,b)

else: print("不正な操作")