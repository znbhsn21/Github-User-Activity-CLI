import os 
import json
import argparse
import requests
from rich.console import Console
from rich import print
from rich.table import Table
from requests.exceptions import RequestException, Timeout
from datetime import datetime, timezone

from datetime import datetime, timezone

def time_ago(date_str):
    event_time = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%SZ")
    event_time = event_time.replace(tzinfo=timezone.utc)
    now = datetime.now(timezone.utc)
    diff = now - event_time

    seconds = diff.total_seconds()
    minutes = seconds // 60
    hours = minutes // 60
    days = hours // 24
    weeks = days // 7

    if seconds < 60:
        return f"{int(seconds)} seconds ago"
    elif minutes < 60:
        return f"{int(minutes)} minute{'s' if minutes != 1 else ''} ago"
    elif hours < 24:
        return f"{int(hours)} hour{'s' if hours != 1 else ''} ago"
    elif days == 1:
        return "yesterday"
    elif days < 7:
        return f"{int(days)} days ago"
    elif weeks == 1:
        return "last week"
    else:
        return f"{int(weeks)} weeks ago"


def user_activity():
    username = input("Enter Username : ")
    url = f'https://api.github.com/users/{username}/events'
    console = Console()

    try:
        response = requests.get(url)

        if response.status_code != 200:
            console.print(f"[red]Error {response.status_code}:[/red] {response.reason}")
            try:
                err_json = response.json()
                console.print(f"[yellow]{err_json.get('status_message', 'Unknown error')}[/yellow]")
            except ValueError:
                pass
            return

        try:
            events = response.json()
            table = Table(title="User Activity Summary")
            table.add_column("Event Type", justify="right", style="cyan", no_wrap=True)
            table.add_column("Repository", style="magenta")
            table.add_column("Date", style = "green")

            for event in events:
                table.add_row(event['type'], event['repo']['name'], time_ago(event['created_at']))

            console.print(table)
        except ValueError:
            console.print("[red]Failed to parse JSON response.[/red]")
            return
    except Timeout:
        console.print("[red]Request timed out. Please try again later.[/red]")
    except RequestException as e:
        console.print(f"[red]Network error:[/red] {e}")
    except Exception as e:
        console.print(f"[red]Unexpected error:[/red] {e}")

user_activity()