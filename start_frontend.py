from threading import Thread
import os
def start_frontend():
    print("PIP FREEZE RESULT:",os.popen('freeze').read())
    print("gf-point: starting front")
    # Run a command using os.system
    command = "cd frontend ; yarn run start"
    os.system(command)
    result = os.popen(command).read()
    print("Output from command:", result)

Thread(target=start_frontend, daemon=True).start()
