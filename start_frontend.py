from threading import Thread

def start_frontend():
    print("gf-point: starting front")
    # Run a command using os.system
    command = "cd frontend ; yarn run start"
    os.system(command)
    result = os.popen(command).read()
    print("Output from command:", result)

Thread(target=start_frontend, daemon=True).start()
