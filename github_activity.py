import requests

def GetData(name):
    url = f"https://api.github.com/users/{name}/events"    
    response = requests.get(url)
    if response.status_code == 200:
        event = response.json()
        print("Output :")
        for e in event:
            if e["type"] == "WatchEvent":
                print(f"- Starred {e['repo']['name']}")
            elif e["type"] == "CreateEvent":
                if e["payload"]["ref_type"] == "repository":
                    print(f"- Created a {e['payload']['ref_type']} in {e['repo']['name']} ")
                else:
                    print(f"- Created a {e['payload']['ref_type']} called {e['payload']['ref']} in {e['repo']['name']} ")
            elif e["type"] == "DeleteEvent":
                print(f"- Deleted a {e['payload']['ref_type']} called {e['payload']['ref']}")
            elif e["type"] == "ForkEvent":
                print(f"- {name} forked the {e['repo']['name']} ")
            elif e["type"] == "IssuesEvent":
                print(f"- {e['payload']['action']} a new issue in {e['repo']['name']}")
            elif e["type"] == "PushEvent":
                print(f"- Pushed a commit to {e['repo']['name']}")
    elif response.status_code == 404:
        print("Invalid Username!")

if __name__ == "__main__":
    GetData(input("GitHub Username : "))


