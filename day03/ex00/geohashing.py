import sys
import antigravity


def starto():
    if len(sys.argv) != 4:
        print("Usage: python geohashing.py [latitude] [longitude] [date]")
        sys.exit(1)
    stt = sys.argv[3].encode('utf-8')
    antigravity.geohash(float(sys.argv[1]), float(sys.argv[2]), stt)



if __name__ == '__main__':
    try:
        starto()
    except ValueError:
        print("Invalid input")
