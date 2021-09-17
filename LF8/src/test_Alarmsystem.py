import unittest
import tempfile
import logging
from Alarmsystem import Alarmsystem


class TestAlarmsystem(unittest.TestCase):
    def test_debug_logmessage(self):
        tmp = tempfile.NamedTemporaryFile()
        logging.basicConfig(
            format='%(asctime)s - %(levelname)s - %(message)s',
            filename=tmp.name,
            level=logging.DEBUG
        )
        logger = logging.getLogger()
        Alarmsystem.examine('Testparameter', 2, 3, 4, 'debug', logger)
        with open(tmp.name) as f:
            for line in f:
                self.assertTrue('Testparameter = 2' in line)

    def test_softlimit_logmessage(self):
        tmp = tempfile.NamedTemporaryFile()
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)
        logging.basicConfig(
            format='%(asctime)s - %(levelname)s - %(message)s',
            filename=tmp.name,
            level=logging.DEBUG
        )
        logger = logging.getLogger()
        Alarmsystem.examine('Testparameter', 3.5, 3, 4, 'debug', logger)
        with open(tmp.name) as f:
            for line in f:
                self.assertTrue('WARNING - TESTPARAMETER EXCEEDS SOFT LIMIT OF 3: Testparameter = 3.5' in line)

    def test_hardlimit_logmessage(self):
        tmp = tempfile.NamedTemporaryFile()
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)
        logging.basicConfig(
            format='%(asctime)s - %(levelname)s - %(message)s',
            filename=tmp.name,
            level=logging.DEBUG
        )
        logger = logging.getLogger()
        Alarmsystem.examine('Testparameter', 5, 3, 4, 'warning', logger)
        with open(tmp.name) as f:
            for line in f:
                self.assertTrue('WARNING - TESTPARAMETER EXCEEDS HARD LIMIT OF 4: Testparameter = 5' in line)


if __name__ == '__main__':
    unittest.main()
