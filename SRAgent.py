actions = {
    ("A", "Clean"): "Right",
    ("A", "Dirty"): "Clean",
    ("B", "Clean"): "Left",
    ("B", "Dirty"): "Clean"
}

starting_env = [
    {"Agent": "A", "A": "Clean", "B": "Clean"},
    {"Agent": "A", "A": "Clean", "B": "Dirty"},
    {"Agent": "A", "A": "Dirty", "B": "Clean"},
    {"Agent": "A", "A": "Dirty", "B": "Dirty"},
    {"Agent": "B", "A": "Clean", "B": "Clean"},
    {"Agent": "B", "A": "Clean", "B": "Dirty"},
    {"Agent": "B", "A": "Dirty", "B": "Clean"},
    {"Agent": "B", "A": "Dirty", "B": "Dirty"}
]

def checkIfDone(env):
    return env["A"]== "Clean" and env["B"]=="Clean"

def updateEnv(env):
    position = env["Agent"]
    status = env[position]
    actionToTake = actions[(position, status)]

    if actionToTake == "Right":
        env["Agent"] = "B"
    
    elif actionToTake == "Left":
        env["Agent"] = "A"
    
    elif actionToTake == "Clean":
        env[position] = "Clean"

    return env
MAX_STEPS = 10
outputs = []

for x in range(len(starting_env)):
    env = starting_env[x]
    steps = 0
    while not checkIfDone(env) and steps < MAX_STEPS:
        env = updateEnv(env)
        steps+=1
    outputs.append(steps)

print(outputs)