import argparse
import datetime
import threading
import time
import webbrowser


class stopWatcher:

    def trackTimes():
        print('Press ENTER to begin. Afterwards, press ENTER to "click" the \
                stopwatch.  Press Ctrl-C to quit.')
        print('Started.')
        startTime = time.time()
        lastTime = startTime
        lapNum = 1

        try:
            while True:
                input()
                lapTime = round(time.time() - lastTime, 2)
                totalTime = round(time.time() - startTime, 2)
                print('Lap #{}: {} ({})'.format(lapNum, str(totalTime).center(20), lapTime))
                lapNum += 1
                lastTime = time.time()
        except KeyboardInterrupt:
            print('\nDone.')


class timeHandler:

    def __init__(self):
        self.timeNow = datetime.datetime.now()
        self.timeSpan = int(parse_args("dictionary")["minutes"])
        self.endTime = None
        self.minutes = self.timeSpan * 60

    def nap(self):
        print('See you in {} minutes'.format(self.timeSpan))
        time.sleep(self.minutes)
        print('Done.')
        webbrowser.open('https://duckduckgo.com', new=2, autoraise=True)

    def timeAction(self):
        nap = timeHandler()
        nap = nap.nap()
        threadObj = threading.Thread(target=nap)
        threadObj.start()



def parse_args(value):
    parser = argparse.ArgumentParser(description="Clock and CLI utilities")

    subparsers = parser.add_subparsers(help='Types of actions.')

    stopWatcher_parser = subparsers.add_parser("stopw")
    stopWatcher_parser.set_defaults(func=stopWatcher.trackTimes)

    timer_parser = subparsers.add_parser("timer")
    timer_parser.add_argument("minutes", type=int, help='An integer \
            representing the number of minutes the times will run.')
    timer_parser.set_defaults(func=timeHandler.timeAction)

    if value == "functions":
        return parser.parse_args()
    elif value == "dictionary":
        return vars(parser.parse_args())


def main():

    args = parse_args("functions")
    argsDict = parse_args("dictionary")
    instantiate = argsDict["func"]

    try:
        args.func()

    except TypeError:
        args.func(instantiate)

if __name__ == '__main__':
    main()
