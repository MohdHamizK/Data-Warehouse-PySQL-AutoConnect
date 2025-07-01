import click
from .emailer import send_daily_sales_email
from .db_utils import refresh_materialized_view

@click.group()
def cli():
    pass

@cli.command()
def refresh_mv():
    """Refresh the materialized view"""
    success = refresh_materialized_view()
    if success:
        click.echo("✅ Materialized view refreshed successfully.")
    else:
        click.echo("❌ Failed to refresh materialized view.")

@cli.command()
def send_report():
    """Send today's sales report via email"""
    send_daily_sales_email()

if __name__ == "__main__":
    cli()