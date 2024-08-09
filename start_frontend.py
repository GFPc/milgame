from threading import Thread

def start_frontend():
    print("gf-point: starting front")
    os.system("cd frontend ; yarn run start")
    

Thread(target=start_frontend, daemon=True).start()
