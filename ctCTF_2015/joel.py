import base64

def b64Mod(x):
    while len(x) % 3 != 0:
        x += "="
    return base64.b64decode(x)

def looper (x):
    answer = x
    while not ("_" in x or "flag" in x):
        answer = answer.decode("rot13")
        answer = b64Mod(answer)
    return answer

f = open("persevere.txt", "r")
text = f.read()
print looper(text)
