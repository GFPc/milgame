from threading import Thread
import os
def start_frontend():
    
    print("gf-point: starting front")
    c = "python3 -m pip freeze"
    os.system(c)
    print("first command finished ---------------------")
    print("PIP FREEZE RESULT:",os.popen(c).read())
    # Run a command using os.system
    command = "cd frontend ; yarn run start"
    os.system(command)
    result = os.popen(command).read()
    print("Output from command:", result)

Thread(target=start_frontend, daemon=True).start()
