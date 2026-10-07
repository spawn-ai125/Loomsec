import requests
import rich.console
import rich.table
from rich.console import Console
import os

banner = r"""
.____                                               
|    |    ____   ____   _____   ______ ____   ____  
|    |   /  _ \ /  _ \ /     \ /  ___// __ \_/ ___\ 
|    |__(  <_> |  <_> )  Y Y  \\___ \\  ___/\  \___ 
|_______ \____/ \____/|__|_|  /____  >\___  >\___  >
        \/                  \/     \/     \/     \/ 
                !coded by 4B2A!        

"""
hedef = input("Enter the target-file: ")
dependencies = {}
with open(hedef, "r") as file:
    for line in file:
        line = line.strip()
        if "==" in line:
            package, version = line.split("==")
            dependencies[package] = version
table = rich.table.Table(title="LoomSec Scan Results")
table.add_column("Package", style="cyan", no_wrap=True)
table.add_column("Version", style="cyan", no_wrap=True)
table.add_column("status", style="cyan", no_wrap=True)


for pkg, ver in dependencies.items():
    payload = {"version": ver, "package": {"name": pkg, "ecosystem": "PyPI"}}
    response = requests.post("https://api.osv.dev/v1/query", json=payload)
    data = response.json()
    if "vulns" in data:
        table.add_row(pkg, ver, "[red]Vulnerable[/red]")
    else:
        table.add_row(pkg, ver, "[green]Safe[/green]")


console = Console()
console.print(banner)
console.print(table)
