"""
Main launching script for scraping sites

Usage:
        launcher.py -s scenario

        suitable scenarios:
         move_ru
         greetotdom_ru
         cian_ru
         greetotdom_msg
"""
import argparse
from move_ru.move_ru import move_ru


def _get_parameters():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--scenario", help="Appropriate website for scenario should be specified")
    args = parser.parse_args()

    return {
        'scenario': args.scenario
    }


def _get_scenarios():
    args = _get_parameters()

    if args['scenario'] is None:
        raise Exception('No scenarios specified')

    if args['scenario'] is 'all':
        scenarios = ['move_ru', 'gdeetotdom_ru', 'cian_ru']
    else:
        scenarios = [args['scenario']]

    return scenarios


def main():
    """
    Main calling function which calls whole testing process
    """
    if _get_scenarios().__contains__('move_ru'):
        move_ru()
    # if _get_scenarios().__contains__('cian_ru'):
    #     cian_ru()

if __name__ == '__main__':
    main()




















