"""
JSON Example
By: Jass Fox
Date: 3/17/21
Update: 2/10/23
"""

import json


def get_name():
    """Get a name for the crew"""
    return input("Who be ye? ")


def call_for_crew(_name):
    """Attract propmpt"""
    print(f"{_name}: Lookin for brave souls to join me crew!")
    return input("")


def greet_minion(_captain_name, _name):
    """Greeting prompt"""
    return print(f"{_captain_name}: Yarrr {_name}! Welcome to me crew!\n")


def rumage_for_crew(_crew):
    """Main application loop"""
    _cmd = call_for_crew(_crew["captain"])  # wait for any response
    if check_exit(_cmd):
        return _cmd

    _new_memeber = get_name()
    if check_exit(_new_memeber):
        return _cmd  # only exit up one level

    greet_minion(_crew["captain"], _new_memeber)
    _crew["crew"].append(_new_memeber)
    return _cmd


def check_exit(_input):
    """Check for exit"""
    if _input == "q" or _input == "quit":
        return True
    else:
        return False


def set_sail(_crew):
    """Start your adventure"""
    print(f"\n {_crew['captain']}: Set sail me hearties!!!")
    for _c in _crew["crew"]:
        print(f"{_c}: Yoho! Yoho! Off to sea we go!")


def save_crew(_crew):
    """Save crew JSON on disk"""
    _file = open(SAVE_FILE, "w", encoding="utf-8")
    _file.write(json.dumps(_crew))
    _file.close()


def load_crew():
    """Load crew from JSON on disk, on failure load default dictionary"""
    try:
        _file = open(SAVE_FILE, "r", encoding="utf-8")
        _dict = json.loads(_file.read())
        _file.close()
    except FileNotFoundError:
        _dict = {"captain": "Captain Dan", "crew": []}
    except OSError:
        _dict = {"captain": "Captain Dan", "crew": []}

    return _dict


# vars
SAVE_FILE = "crew.txt"
CREW = load_crew()  # {"captain":"Captain Dan", "crew":[]} #Crew List
CMD = ""

# Exit instructions
print("q || quit\n\n")

# Rummage for crew
while check_exit(CMD) is not True:
    CMD = rumage_for_crew(CREW)

set_sail(CREW)
save_crew(CREW)
