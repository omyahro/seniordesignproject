import re
import sys
from re import search

from cis301.project2.phonebill import PhoneBill
from cis301.project2.phonecall import PhoneCall


def main(args=None):
    """
        This program that parses the command line, creates a
        Student, and prints a description of the student to
        standard out by invoking its toString method.
    """
    if args is None:
        args = sys.argv[1:]

    print (args)
    print(f"Missing command line arguments")
    parse_cli_argv(args)


def parse_cli_argv(argv):
    if "-README" in argv:
        print(usage())
        exit()

    indx = 0
    printflag = False

    if "-print" in argv and len(argv) == 8:
        if argv[0] == "-print":
            indx += 1
            printflag = True
        else:
            print(usage())
            return
    elif len(argv) != 7:
        print(usage())
        return

    owner = argv[indx]
    caller = argv[indx+1]


    if not isvalid_phonenumber(caller):
        print(usage ())
        return
    callee = argv[indx+2]
    if not isvalid_phonenumber(callee):
        print (usage())
        return
    start_date = argv[indx+3]
    start_time = argv[indx+4]
    start_datetime= start_date + " " + start_time
    if(not isvalid_datetime(start_datetime)):
        print("Invalid start date format!")
        print (usage())
        sys.exit(1)

    end_date = argv[indx+5]
    end_time = argv[indx+6]
    end_datetime= end_date + " " + end_time
    if(not isvalid_datetime(end_datetime)):
        print("Invalid end date format!")
        print (usage())
        sys.exit(1)

    phonecall = PhoneCall(caller, callee, start_datetime, end_datetime)
    phonebill = PhoneBill(owner)
    phonebill.add_phonecall()

    if(printflag):
        print(phonecall)

def isvalid_phonenumber(phone):
    phone_pattern = r"[1-9][0-9] {2} - [0-9] {3} - [0-9] {4}"
    if (re.match(phone_pattern, phone)):
        return True
    else:
        return False

def isvalid_datetime(date_time):
    datetime_format = "%m/%d/%Y %H:%M"
    try:
        date_time.strptime(date_time, datetime_format)
        return True
    except:
        return False


def usage():
    README = '\nproject2 [options] <args> args are (have to be in order): ' \
                  '\n\tcustomer\tPerson whose phone bill' \
                  '\n\tcallerNumber\tPhone number of caller' \
                  '\n\tcalleeNumber\tPhone number of person who was called' \
                  '\n\tstartTime\tDate and time call began (24-hour time)' \
                  '\n\tendTime\tDate and time call ended (24-hour time)' \
                  '\noptions are... and the options dont have to be in order:' \
                  '\n\t-print\tPrints a description of the new phone call' \
                  '\n\t-README\tPrints a README for this project and exits' \
                  '\nDate and time should be in the format: mm/dd/yyyy hh:mm'
    return README


if __name__ == "__main__":
    main()
