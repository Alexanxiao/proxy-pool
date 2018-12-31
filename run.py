from schedule.scheduler import Scheduler
from core.api import app
from multiprocessing import Process

def par1():
    scheduler = Scheduler()
    scheduler.schedule()

def par2():
    app.run()

def run():
    print('proxy pool is running')
    p1 = Process(target=par1)
    p2 = Process(target=par2)
    p1.start()
    p2.start()
    p1.join()
    p2.join()

if __name__ == '__main__':
    run()