import keyboard
import time
translate = {
    'א': chr(67840),
    'ב': chr(67841),
    'ג': chr(67842),
    'ד': chr(67843),
    'ה': chr(67844),
    'ו': chr(67845),
    'ז': chr(67846),
    'ח': chr(67847),
    'ט': chr(67848),
    'י': chr(67849),
    'כ': chr(67850),
    'ל': chr(67851),
    'מ': chr(67852),
    'נ': chr(67853),
    'ס': chr(67854),
    'ע': chr(67855),
    'פ': chr(67856),
    'צ': chr(67857),
    'ק': chr(67858),
    'ר': chr(67859),
    'ש': chr(67860),
    'ת': chr(67861),
}
while True:
    if keyboard.is_pressed('ctrl') and keyboard.is_pressed('alt'):
        time.sleep(1)
        print("starting...")
        while True:
            if keyboard.is_pressed('ctrl') and keyboard.is_pressed('alt'):
                time.sleep(1)
                print("Exiting...")
                break
            if keyboard.is_pressed('esc'):
                print('shutdown :)')
                exit()
            event = keyboard.read_event()
            
            if event.event_type == keyboard.KEY_DOWN and event.name.isalpha() and len(event.name) == 1:
                if(event.name in "אבגדהוזחטיכלמנסעפצקרשת"):
                    p = translate[event.name]
                    keyboard.write(p)
                    keyboard.press_and_release('backspace')
                    keyboard.press_and_release('backspace')
                    keyboard.write(p)
    if keyboard.is_pressed('esc'):
        print('shutdown :)')
        exit()