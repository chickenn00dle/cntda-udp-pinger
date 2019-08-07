# Simple UDP Ping implementation for Computer Networking: A Top Down Approach

A simple ping app built with python (Chapter 2 assignment for Computer Networking: A Top Down Approach). The pinger will run as both server and client depending on supplied arguments.

## Getting Started

### Prerequisites

The project runs on Python 3+ so you'll need to make sure this is installed.

```
python3 --version
```

Should result in something like:

```
Python 3.7.4
```

If not, you can get set up with the latest version of Python here: https://www.python.org/downloads/

### Installing

Clone the project and give it a name

```
git clone phttps://github.com/chickenn00dle/cntda-udp-pinger.git [project-name]
cd [project-name]
```

And that's it. You have everything you need to get started.

## Running the tests

After getting the project cloned, you can test it using localhost. By default, server.py will run localhost so simply running:

```
./ping.py --run-server
```

will get the ping server running.

You can then issue pings by running

```
./ping.py
```

Note that there are two additional options: `--server-address` and `--server-port`

## Authors

* **Rasmy Nguyen** - [@chickenn00dle](https://twitter.com/ChickenN00dle)

## License

This project is licensed under the MIT License - see the [Open Source Initiative](https://opensource.org/licenses/MIT) for details

## Acknowledgments

Big shout out to @davidshepherd7 for providing some templates for the Computer Networking: A Top Down Approach projects here: https://github.com/davidshepherd7/Kurose-and-Ross-socket-programming-exercises

