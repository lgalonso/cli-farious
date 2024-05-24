import click

from app.src.log_parser import get_ips_from_log, get_events_per_second, get_total_bytes_exchanged
from app.src.utils import least_repeated_item, most_repeated_item

@click.command(help="CLI-farious is a clever wordplay that combines CLI and various to suggest a versatile and comprehensive log analysis tool")
@click.version_option("1.0.0", prog_name="CLI-farious")
@click.argument('path', default = "")
@click.option('--mfip', help = "Returns most frequent IP from log file.")
@click.option('--lfip', help = "Returns least frequent IP from log file.")
@click.option('--eps', help = "Returns Events Per Second from log file.")
@click.option('--bytes', help = "Returns total amount of bytes exchanged from log file.")
def cli(path, mfip, lfip, eps, bytes):
    if mfip:
        print(most_repeated_item(get_ips_from_log(path)))

    if lfip:
        print(least_repeated_item(get_ips_from_log(path)))

    if eps:
        print(get_events_per_second(path))

    if bytes:
        print(path)
        print(get_total_bytes_exchanged(path))

if __name__ == '__main__':
    cli()