import threading,time
t = 1
def call(text):
    global t
    time.sleep(t)
    t+=1
    print(t)
    
    print(text)

te= threading.Thread(target=call,args=("text1",))
te.start()

ts= threading.Thread(target=call,args=("text2",))
ts.start()


