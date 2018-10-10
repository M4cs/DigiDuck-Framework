import os, sys, time, os.path, subprocess, glob
from core import header
from core import help
from core import platformdetection

os.system('clear')
header.head()
help.help()
platform = platformdetection.platform()
print("Platform Detected: "+platform)
if platform == 'win32':
    existswin = os.path.exists('resources\micronucleus.exe')
    if existswin == True:
        micronucleus = 'resources\micronucleus.exe'
        pass
    else:
        microlink = 'https://github.com/micronucleus/micronucleus/blob/v1.11/commandline/builds/Windows/micronucleus.exe'
        print('Please grab the micronucleus.exe from %d and place it in resources/!' % (microlink))
        exit()
elif platform == 'posix':
    existsmac = os.path.exists('resources\micronucleus')
    if existsmac == True:
        micronucleus = 'resources\micronucleus'
        pass
    else:
        micromaclink = 'https://github.com/micronucleus/micronucleus/blob/v1.11/commandline/builds/OSX/micronucleus'
        print('Please grab the micronucleus.exe from %d and place it in resources/!' % (micromaclink))
        exit()
else:
    print('OS Not Supported At The Moment. Please Run This On Windows Or MacOS')

print("")
intname = '[digiduck]> '
def main():
    try:
        line_1 = intname
        terminal = input(line_1)
        if terminal[0:4] == 'help':
            help.help()
            main()
        elif terminal[0:4] == 'show':
            print("\nAvailable Payloads: \n")
            for d in glob.iglob('payloads/*'):
                f = d.replace("payloads\\", "")
                print(f)
            main()
        elif terminal[0:7] == 'execute':
            setpayload = setpl()
            os.system("%s --run payloads\%s" % (micronucleus,setpayload))
            print("Completed Installation!")
            main()

    except KeyboardInterrupt:
        exit()

def setpl():
    try:
        print("\nAvailable Payloads: \n")
        for d in glob.iglob('payloads/*'):
            f = d.replace("payloads\\", "")
            print(f)
        print("")
        print("Enter A Payload From Above (include .hex)")
        setpayload = []
        payload = input("[set payload]> ")
        payload_exists = os.path.exists('payloads/%s' % (payload))
        if payload_exists == True:
            setpayload = payload
            print("Successfully Set Payload As: %s" % (setpayload))
            return setpayload
            main()
        else:
            print("Sorry That Isn't A Payload!")
            setpl()
    except:
        pass

main()
