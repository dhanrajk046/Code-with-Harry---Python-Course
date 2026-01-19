import os

def generateTable(n):
    # Ensure the "tables" folder exists
    os.makedirs("tables", exist_ok=True)

    table = ""
    for i in range(1, 11):
        table += f"{n} x {i} = {n*i}\n"

    # Save each table in its own file
    with open(f"tables/table_{n}.txt", "w") as f:
        f.write(table)

# Generate tables from 2 to 20
for i in range(2, 21):
    generateTable(i)