import thingSpeak as ts
import thread, time

#Using a separate thread to update data at ThingSpeak server

def update():
    from random import randint
    t = ts.Channels('192.168.88.195:3000')
    print 'Channel keys:' + str(t.keys)
    for i in range(len(t.keys)):
        t.updateChannel(i,[randint(0,100), randint(0,100), randint(0,100), randint(0,100), randint(0,100)])
        print 'Updated channel ' + str(i)

for i in range(50):
    print i
    if i == 10:
        thread.start_new_thread(update, ())
    time.sleep(0.2)