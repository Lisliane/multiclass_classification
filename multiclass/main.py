#!/usr/bin/env python

# Authors: Lisliane Zanette de Oliveira <lislianezanetteoliveira@gmail.com>

# Third-party imports
import argparse

# Own imports


def parse_args():
    parser = argparse.ArgumentParser()

    help_msg = 'Options: 1-Treats datas   2-Train    3-Predicts'
    parser.add_argument(
        '--option',
        action='store',
        type=int,
        default=1,
        choices=[1, 2, 3],
        help=help_msg
    )

    help_msg = 'Defines language. Options: PTB (portuguese)  ENG (english)'
    parser.add_argument(
        '--lang',
        action='store',
        type=str,
        default='PTB',
        help=help_msg
    )

    args = parser.parse_args()
    return args


def main():
    """
        Main
    """

    args = parse_args()
    lang = args.lang
    option = args.option


if __name__ == '__main__':
    main()
