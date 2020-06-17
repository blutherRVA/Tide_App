
import time

james = 1592399416 #Low Tide morning of 6/13/2020 in Cape Charles Harbor
piank = 1592378296
mobjack = 1592370976


def time_keeper(time_stamp):
    time_since_stamp = time.time() - time_stamp
    time_since_last_low = time_since_stamp % 44700
    return time_since_last_low


if __name__ ==('__main__'):
    print(int(time_keeper(james)))
    print(int(time_keeper(piank)))
    print(int(time_keeper(mobjack)))