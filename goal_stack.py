
on = {
    "A": "TABLE",
    "B": "A",
    "C": "TABLE"
}

goal = {
    "A": "B",
    "B": "C",
    "C": "TABLE"
}

clear = {"B", "C"}
holding = None

goal_stack = [
    ("ON", "A", "B"),
    ("ON", "B", "C"),
    ("ON", "C", "TABLE")
]

plan = []


def unstack(block, below):
    global holding

    print(f"UNSTACK({block}, {below})")
    on[block] = "TABLE"
    clear.add(below)
    clear.remove(block)
    holding = block


def putdown(block):
    global holding

    print(f"PUTDOWN({block})")
    on[block] = "TABLE"
    clear.add(block)
    holding = None


def pickup(block):
    global holding

    print(f"PICKUP({block})")
    on[block] = None
    clear.remove(block)
    holding = block


def stack(block, target):
    global holding

    print(f"STACK({block}, {target})")
    on[block] = target
    clear.add(block)
    clear.remove(target)
    holding = None

while goal_stack:
    current_goal = goal_stack.pop()

    if current_goal == ("ON", "C", "TABLE"):
        print("Goal already satisfied: C is on TABLE")

    elif current_goal == ("ON", "B", "C"):
        if on["B"] == "A":
            unstack("B", "A")
            putdown("B")

        if holding is None and on["B"] == "TABLE":
            pickup("B")

        if holding == "B" and "C" in clear:
            stack("B", "C")

    elif current_goal == ("ON", "A", "B"):
        if on["B"] == "A":
            unstack("B", "A")
            putdown("B")

        if holding is None and on["A"] == "TABLE":
            pickup("A")

        if holding == "A" and "B" in clear:
            stack("A", "B")

print("\nFinal Configuration:")
for block in on:
    print(block, "on", on[block])
