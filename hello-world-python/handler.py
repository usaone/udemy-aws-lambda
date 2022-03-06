import time

def hello(event, context):
    print("Fourth update !")
    time.sleep(4)
    return "hello-world"
