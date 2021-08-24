# Netcheck

Utility for measuring network reliability and TTL in home networks.

## Usage

Prerequisites: host operating system has `traceroute`
utility.

Run `python main.py` to start. Netcheck is intended to 
be executed on a periodic basis, measuring the round
trip time (RTT) between the host computer and a
remote destination. 

Netcheck is configured by a `.env` file, allowing
additional configuration through environment variables:

* `MAX_HOPS` The maximum number of hops before exiting
* `TIMEOUT_SEC` Seconds to wait before giving up
* `HOST` The remote HTTP host to check, like 'www.google.com'
* `LOG_LEVEL` Defaults to `logging.INFO`
* `DEVICE` The device label added to logs
* LOG_OUT=/tmp/netcheck.log
