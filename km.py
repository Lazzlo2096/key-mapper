from pynput import keyboard
from pynput.keyboard._win32 import KeyCode
import time

key_map = [
    (['f', 'j'], 'a'),
    (['f', 'k'], 'o'),
    (['f', 'l'], 'e'),
    (['f', ';'], 'u'),

    (['d', 'j'], 'h'),
    (['d', 'k'], 't'),
    (['d', 'l'], 'n'),
    (['d', ';'], 's'),

    (['s', 'j'], 'hello world!'), # not working yet
    (['s', 'k'], keyboard.Key.up),
    (['s', 'l'], '6'),
    (['s', ';'], '8'),

    (['f','f', 'j'], keyboard.Key.up),
    (['f','f', 'k'], keyboard.Key.down),
    (['f','f', 'l'], keyboard.Key.left),
    (['f','f', ';'], keyboard.Key.right),
]

key_map42 = [
    ([KeyCode.from_char('f'), KeyCode.from_char('j')], 'a'),
    ([KeyCode.from_char('f'), KeyCode.from_char('k')], 'b'),
    ([KeyCode.from_char('f'), KeyCode.from_char('k')], 'b'),
    ([KeyCode.from_char('f'), KeyCode.from_char('k')], 'b'),
]

def modify_key_map(key_map):

    def f(char):
        return chr(ord(char)+1)

    def f(char):
        return KeyCode.from_char(char)

    for i, (keys, value) in enumerate(key_map):
        new_keys = [f(char) for char in keys]
        key_map[i] = (new_keys, value)

    return key_map



key_map = modify_key_map(key_map)

current_pressed_seq = []
#keyboard.Key.esc:
#Key.space

ignore_num = 0

def on_press(key):
    global current_pressed_seq
    global listener
    global ignore_num


    #if listener._suppress == True:
    if ignore_num == 0:

        if key == keyboard.Key.esc:
            #keyboard.Key.
            #keyboard._win32.
            #KeyCode.from_vk(VK.F23)

            current_pressed_seq.clear()

        else:

            current_pressed_seq.append(key)

            for seq, output_key in key_map:
                #print(seq, output_key)
                #print(key, type(key))
                #print(seq[0], type(seq[0]))
                #print(KeyCode.from_char(seq[0][0]), type(KeyCode.from_char(seq[0][0])))
                print("for ", current_pressed_seq, seq, current_pressed_seq == seq, output_key)
                if current_pressed_seq == seq:
                    print("finded ", current_pressed_seq , seq, current_pressed_seq == seq)
                    listener._suppress = False

                    ignore_num += 1 # len of output_key is 1
                    #ignore_num += len(output_key)

                    keyboard.Controller().press(output_key)
                    keyboard.Controller().release(output_key)
                    #keyboard.Controller().type(output_key)

                    # оно помещяет в какую то очередь лол

                    listener._suppress = True
                    current_pressed_seq.clear()

                    break

    else:
        ignore_num -= 1;

    print(current_pressed_seq)



listener = keyboard.Listener(on_press=on_press, suppress = True)
listener.start()
listener.join()
