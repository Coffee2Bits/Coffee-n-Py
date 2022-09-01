import argparse
from coffee.coffee import keep_alive


def run():
    arg_parser = setup_argparser()
    args = arg_parser.parse_args()
    args_dict = vars(args)

    print(args_dict)
    interval_time = args_dict.get("interval") or 300

    keep_alive(interval_time)


def setup_argparser():

    parser = argparse.ArgumentParser(description="Make some motion periodically.")
    parser.add_argument("--interval", type=int, default=max, help="Number of seconds between manipulation actions")
    args = parser.parse_args()

    return parser
