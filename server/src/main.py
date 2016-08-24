import field
import client

F_X, F_Y = 20, 20

Field = field.gen_field(F_X, F_Y)
client.init_net()

while not client.exited:
    client.update_net()

client.free_net()
