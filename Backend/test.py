from rich.progress import Progress
import time

with Progress() as p:

    a = p.add_task("[cyan]Test",total=10)

    for i in range(10):
        p.update(a,advance=1)
        time.sleep(0.1)

print("BEGIN")