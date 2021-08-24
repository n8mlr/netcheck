# Netcheck

Utility for measuring network reliability and TTL in home networks.

## Usage

**Prerequisites:** host operating system has `traceroute`
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
* `LOG_OUT`=/tmp/netcheck.ndjson

## Output example

```
{"created": 1629780220.046032, "levelname": "INFO", "message": "hop", "host": "192.168.200.1", "ip": "192.168.200.1", "order": 1, "rtt": "2.098", "rtt_unit": "ms"}
{"created": 1629780220.0468218, "levelname": "INFO", "message": "hop", "host": "tukw-dsl-gw67.tukw.qwest.net", "ip": "63.231.10.67", "order": 2, "rtt": "3.861", "rtt_unit": "ms"}
{"created": 1629780220.047107, "levelname": "INFO", "message": "hop", "host": "63-226-198-17.tukw.qwest.net", "ip": "63.226.198.17", "order": 3, "rtt": "3.916", "rtt_unit": "ms"}
{"created": 1629780220.047327, "levelname": "INFO", "message": "hop", "host": "sea-edge-15.inet.qwest.net", "ip": "67.14.41.158", "order": 4, "rtt": "4.455", "rtt_unit": "ms"}
{"created": 1629780220.047539, "levelname": "INFO", "message": "hop", "host": "72.14.221.108", "ip": "72.14.221.108", "order": 5, "rtt": "6.155", "rtt_unit": "ms"}
```



