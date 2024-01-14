import pandas as pd
import time

class DummyStock:

    def getHistory(self, code = "dummy"):
        time.sleep(5)
        return pd.read_csv("utility/dummy.csv")