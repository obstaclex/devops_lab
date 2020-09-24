import json
import psutil
import time
import datetime
import argparse


# Create Class with 2 methods for create different log type
class Snapshot():
    def __init__(self, n):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.name = 'snapshot{}: {}'.format(n, timestamp)
        self.cpu_usage = psutil.cpu_percent(interval=1)
        self.memory_usage = psutil.disk_usage('/').percent
        self.virtual_memory_usage = psutil.virtual_memory().percent

    def save_as_json(self):
        json_data['{}'.format(self.name)] = []
        json_data['{}'.format(self.name)].append({
            'cpu_usage': self.cpu_usage,
            'memory_usage': self.memory_usage,
            'virtual_memory_usage': self.virtual_memory_usage
        })
        with open('snapshot.json', 'w') as outfile:
            json.dump(json_data, outfile, indent=4)

    def save_as_plain_text(self):
        f = open("snapshot.txt", "a+")
        f.write('{}; cpu_usage is {}; memory_usage is {}; virtual_memory_usage is {}\n'.format(
            self.name, self.cpu_usage, self.memory_usage, self.virtual_memory_usage))


# Add parser for adding input parametr
parser = argparse.ArgumentParser()
parser.add_argument('-i', dest="interval",
                    help="Interval between snapshots", type=int, default=30)
parser.add_argument("-t", dest="type", help="Output file type", default="txt")
args = parser.parse_args()


# Create empty file for reset log counter
json_data = {}
if args.type != "json":
    f = open("snapshot.txt", "w")


# Cycle for permanent running

def main():
    i = 0
    while True:
        i += 1
        a = Snapshot(i)
        if args.type == "json":
            a.save_as_json()
        else:
            a.save_as_plain_text()
        time.sleep(args.interval)


if __name__ == "__main__":
    main()
