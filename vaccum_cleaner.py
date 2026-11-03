

def vacuum_agent(location, status):
    if status == "Dirty":
        return "SUCK"
    elif location == "A":
        return "RIGHT"
    else:
        return "LEFT"


environment = {
    "A": "Dirty",
    "B": "Dirty"
}

location = "A"

while True:
    status = environment[location]

    action = vacuum_agent(location, status)
    print("Location:", location, "| Status:", status, "| Action:", action)

    if action == "SUCK":
        environment[location] = "Clean"

    elif action == "RIGHT":
        location = "B"

    elif action == "LEFT":
        location = "A"

    if environment["A"] == "Clean" and environment["B"] == "Clean":
        print("Both rooms are clean!")
        break
