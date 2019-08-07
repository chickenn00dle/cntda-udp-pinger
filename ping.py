#!/usr/bin/env python3

import argparse
import signal
import socket
import time

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--server-port', '-p', default=2081, type=int, help='Server_Port to use')
    parser.add_argument('--run-server', '-s', action='store_true', help='Run a ping server')
    parser.add_argument('--server_address', default='localhost', help='Server to ping, no effect if running as a server.')
    args = parser.parse_args()
    if args.run_server:
        return run_server(args.server_port)
    else:
        return run_client(args.server_address, args.server_port,)


def run_server(port):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.bind(('', port))
        print("Ping server ready on port", port)
        while True:
            _, client_address = sock.recvfrom(1024)
            sock.sendto("".encode(), client_address)
    return 0


def run_client(address, port):
    message = 'ping'
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.connect((address, port))
        signal.signal(signal.SIGALRM, timeout_handler)
        pings = 1
        while pings <= 10:
            print('Ping %d RTT:' % (pings))
            time.sleep(1) # Pause between pings
            signal.alarm(1) # Initialize 1 second alarm
            try:
                start = get_current_time_in_nanoseconds()
                sock.send(bytes(message, 'utf-8'))
                reply = sock.recvfrom(1024)
                if reply:
                    end = get_current_time_in_nanoseconds()
                    rtt = end - start
                    print('%d nanoseconds\n' % (rtt))
            except Exception as exc:
                if str(exc) == 'Timeout': 
                    print('Exception raised: Ping timeout\n')
                else:
                    print('Undetermined. Ping lost to the ether...\n')
            finally:
                signal.alarm(0)
            pings += 1
    return 0


'''
Helper function to convert time() to nanoseconds
'''
def get_current_time_in_nanoseconds():
    return int(round(time.time() * 1000000000))


'''
Timeout handler for signal alarm. Raises Timeout exception
'''
def timeout_handler(num, stack):
    raise Exception("Timeout")


if __name__ == "__main__":
    main()
