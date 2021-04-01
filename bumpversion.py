import subprocess
import toml

with open("pyproject.toml") as f:
    k = toml.loads(f.read())

print(f'current version: {k["tool"]["poetry"]["version"]}')
u = input("new version: ").strip().lower()
if not u:
    sys.exit(1)
k["tool"]["poetry"]["version"] = u

with open("pyproject.toml", "w") as f:
    f.write(toml.dumps(k))

subprocess.run(["git", "reset", "."], check=True)
subprocess.run(["git", "add", "pyproject.toml"], check=True)
subprocess.run(["git", "commit", "-m", f"chore: bump to version {u}"], check=True)
subprocess.run(["git", "tag", "-a", f"v{u}", "-m", f"version {u}"], check=True)
