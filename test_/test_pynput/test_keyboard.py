from pynput import keyboard
import sys, os


def on_press(key):
    try:
        print('alphanumeric key  {0} pressed'.format(key.char))
    except AttributeError:
        print('special key {0} pressed'.format(key))


def on_release(key):
    print('{0} released'.format(key))
    if key == keyboard.Key.esc:
        return False


def on_press_(key):
    # print(key)
    # return key
    pass


def on_release_(key):
    print(key)
    if key == keyboard.Key.esc:
        os._exit(0)
        # sys.exit(0)
        # return False
    return key


while True:
    with keyboard.Listener(on_press=on_press_, on_release=on_release_) as listener:
        listener.join()
