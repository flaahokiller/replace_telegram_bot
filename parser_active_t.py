from instrument_for_parser import InstrumentForParser as ifs #parsing active topic url
import time
import schedule

def main(args):

    url='https://replace.org.ua/search/recent/'
    print(ifs.active_temes(url))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
