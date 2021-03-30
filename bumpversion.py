import toml

with open("pyproject.toml") as f:
    k = toml.loads(f.read())

u = input().strip().lower()
if not u:
    sys.exit(1)
k["tool"]["poetry"]["version"] = u

with open("pyproject.toml", "w") as f:
    f.write(toml.dumps(k))