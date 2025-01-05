import pandas as pd
import csv

class Test_READ():
    def test_read_csv(self):
        with open('userdata.csv') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                print(row[0],[1])


def test_read_pandas():
    df = pd.read_csv('userdata.csv')
    print(df)