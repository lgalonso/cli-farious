import click

from app.src.log_parser import get_ips_from_log, get_events_per_second, get_total_bytes_exchanged
from app.src.utils import least_repeated_item, most_repeated_item

@click.command(help="CLI-farious is a clever wordplay that combines CLI and various to suggest a versatile and comprehensive log analysis tool.")
@click.option('--input', '-i', help="Input: Path to the log file to analyze.", required=True)
@click.option('--output', '-o', help="Output: Path to output file to write the log analysis results.")
@click.option('--mfip', help="Returns most frequent IP from log file.", is_flag=True)
@click.option('--lfip', help="Returns least frequent IP from log file.", is_flag=True)
@click.option('--eps', help="Returns Events Per Second from log file.", is_flag=True)
@click.option('--bytes', help="Returns total amount of bytes exchanged from log file.", is_flag=True)
@click.version_option("1.0.0", prog_name="CLI-farious")
def cli(i, mfip, lfip, eps, bytes, o):
    path = i
    if mfip:
        print(most_repeated_item(get_ips_from_log(path)))

    if lfip:
        print(least_repeated_item(get_ips_from_log(path)))

    if eps:
        print(get_events_per_second(path))

    if bytes:
        print(get_total_bytes_exchanged(path))

if __name__ == '__main__':
    cli()