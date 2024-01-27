from time import sleep
def text(words,duration = 0.02):
    for i in words:
        print(i,end='',flush=True)
        sleep(duration)
    print()

def __init__():
    print(__init__)