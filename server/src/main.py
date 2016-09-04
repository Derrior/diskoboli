import field
import threading
import client

exited = None

def quit_f():
    global exited 
    while True:
        
        input_str = input()
        if (input_str == 'q' or input_str == 'exit'):
            exited = True
        if (exited):
            break
    
F_X, F_Y = 20, 20

Field = field.gen_field(F_X, F_Y)
client.init_net()
quit_thread = threading.Thread(target=quit_f)
quit_thread.start()

while not exited:
    client.update_net()
    quit_thread.join(timeout=0.1)

client.free_net()
