import unittest
from schedule.scheduler import Scheduler

class TestSchedule(unittest.TestCase):

    def setUp(self):
        self.scheduler = Scheduler()

    def test_run(self):
        self.scheduler.schedule()

if __name__ == '__main__':
    unittest.main()