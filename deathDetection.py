import time
import os

death_keywords = [
    "was shot by", 
    "was pricked to death", 
    "walked into a cactus while trying to escape",
    "went up in flames", 
    "walked into fire while fighting",
    "was squished too much",
    "was squashed by",
    "was roasted in dragon's breath",
    "drowned",
    "died from dehydration",
    "hit the ground too hard",
    "blew up",
    "was blown up by",
    "was squashed by a falling anvil",
    "was squashed by a falling block",
    "was skewered by a falling stalactite",
    "was fireballed by",
    "went off with a bang",
    "experienced kinetic energy",
    "froze to death",
    "was frozen to death by",
    "died",
    "was killed",
    "discovered the floor was lava",
    "walked into the danger zone due to",
    "went up in flames",
    "suffocated in a wall",
    "using magic",
    "tried to swim in lava",
    "was struck by lightning",
    "was smashed by",
    "was killed by magic",
    "was slain by",
    "burned to death",
    "was burned to a crisp while fighting",
    "fell out of the world",
    "didn't want to live in the same world as",
    "left the confines of this world",
    "was blown up by",
    "was obliterated by a sonically-charged shriek",
    "was impaled on a stalagmite",
    "starved to death",
    "was stung to death",
    "was poked to death by a sweet berry bush",
    "was killed while trying to hurt",
    "was pummeled by",
    "was impaled by",
    "withered away",
    "was shot by a skull from"
    ]

player_name = "PencilLead2"

#LOG_PATH = os.path.expanduser("C:\Users\Tech Lab\AppData\Roaming\.minecraft\logs\latest.log")
LOG_PATH = os.path.expanduser(r"~\AppData\Roaming\.minecraft\logs\latest.log")

def tail_log(log_path):
    """Yields new lines as they are added to the log file."""
    with open(log_path, "r", encoding="utf-8") as f:
        f.seek(0, os.SEEK_END)  # Start at the end of the file
        while True:
            line = f.readline()
            if not line:
                time.sleep(0.1)
                continue
            yield line.strip()

def detect_deaths():
    print(f"👀 Watching for death messages from: {player_name}")
    for line in tail_log(LOG_PATH):
        if (
            line.startswith("[")
            and player_name in line
            and "INFO" in line
            and any(kw in line for kw in death_keywords)
        ):
            print(f"💀 Death Detected: {line}")
            with open("deaths_detected.txt", "a", encoding="utf-8") as log_file:
                log_file.write(line + "\n")

if __name__ == "__main__":
    detect_deaths()
