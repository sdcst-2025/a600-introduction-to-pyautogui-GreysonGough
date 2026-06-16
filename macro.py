import pyautogui as p
import time
import keyboard

running = True

def stop_program():
    global running
    running = False
    print("Stopped.")

keyboard.add_hotkey("\\", stop_program)

def start_macro():
    global running
    
    print("This code is made for someone who has every upgrade available.")
    print("Ensure the game is in fullscreen and is scrolled to the top with adblocker.")
    print("Starting in 3 seconds")
    print("Press \\ to stop.")


    time.sleep(3)

    cookie = (220, 363)

    top_path = [
        (1152, 203),
        (1100, 210),
        (1076, 317),
        (1208, 295),
        (1218, 363),
        (1260, 453),
        (1260, 493),
        (1218, 557),
        (1253, 623),
        (1271, 688),
        (1317, 756),
        (1296, 816),
    ]

    bottom_path = [
        (1272, 136),
        (1260, 234),
        (1243, 297),
        (1268, 358),
        (1243, 427),
        (1244, 486),
        (1248, 545),
        (1245, 608),
        (1249, 682),
        (1245, 749),
        (1274, 780)
    ]

    while running:

        for i in range(50):
            if not running:
                break
            p.click(cookie)
            time.sleep(0.02)


        for x, y in top_path:
            if not running:
                break
            p.click(x, y)
            time.sleep(0.1)

        if not running:
            break


        p.moveTo(1296, 816)
        p.scroll(-1000000)
        time.sleep(0.5)


        for x, y in bottom_path:
            if not running:
                break
            p.click(x, y)
            time.sleep(0.1)

        if not running:
            break


        p.moveTo(1245, 749)
        p.scroll(1000000)
        time.sleep(0.5)

    print("Macro closed.")


start_macro()