import subprocess


def main():
    # run "python generate-manifest.py deps.txt"
    subprocess.run(["python", "generate-manifest.py", "deps.txt"])

    # run "package.py"
    subprocess.run(["python", "package.py"])


if __name__ == "__main__":
    main()