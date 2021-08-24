import datetime
import subprocess
import logging
from pythonjsonlogger import jsonlogger
from datetime import datetime
from datetime import timezone
from typing import Optional
import os
from dotenv import load_dotenv

load_dotenv()

MAX_HOPS = int(os.getenv('MAX_HOPS')) or 5
TIMEOUT_SEC = int(os.getenv('TIMEOUT_SEC')) or 5
HOST = os.getenv('HOST') or 'www.google.com'
LOG_LEVEL = int(os.getenv('LOG_LEVEL')) or logging.INFO
LOG_OUT = os.getenv('LOG_OUT') or '/tmp/netcheck.ndjson'
DEVICE = os.getenv('DEVICE') or os.uname()[1]


logger = logging.getLogger()
logger.setLevel(LOG_LEVEL)
stream_handler = logging.StreamHandler()
formatter = jsonlogger.JsonFormatter("%(created)s %(levelname)s %(message)s")
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

file_handler = logging.FileHandler(LOG_OUT, encoding='utf-8')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def traceroute(host: str, max_hops: int, timeout: int) -> Optional[str]:
    try:
        proc = subprocess.run(['traceroute', '-m', str(max_hops), host],
                              capture_output=True, encoding='utf-8', timeout=timeout)
        return proc.stdout
    except subprocess.TimeoutExpired:
        logger.warning("no response")


def parse_response(output: str, timestamp: float):
    """Transforms traceroute output into a single line of text"""
    nodes = output.split("\n")
    nodes.pop()  # ignore last line feed

    for n in nodes:
        parts = n.split(' ')

        if len(parts) > 1:

            ip = parts[4].replace('(', '').replace(')', '')

            try:
                order = int(parts[1])
            except ValueError:
                logger.debug("Load balanced node detected, skipping node", extra={"ip": ip})
                break

            logging.debug(parts, extra={"request_time": timestamp})
            payload = {
                'host': parts[3],
                'ip': ip,
                'order': order,
                'rtt': parts[6],
                'rtt_unit': parts[7]
            }
            logging.info("hop", extra=payload)


def main():
    ts = datetime.now(tz=timezone.utc).timestamp()
    response = traceroute(HOST, MAX_HOPS, TIMEOUT_SEC)
    if response:
        parse_response(response, ts)


if __name__ == "__main__":
    main()
