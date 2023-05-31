"""Main module for managing the CLI configuration and execution."""
import argparse
from coffee.manipulation import keep_alive


def run():
    """Run the Coffee application's CLI."""
    arg_parser = _setup_argparser()
    args = arg_parser.parse_args()
    args_dict = vars(args)

    print(args_dict)
    interval_time = int(args_dict.get("interval", 300))

    keep_alive(interval_time)


def _setup_argparser():
    parser = argparse.ArgumentParser(description="Make some motion periodically.")
    parser.add_argument("--interval", type=int, default=9999999999, help="Number of seconds between manipulation actions")
    return parser
