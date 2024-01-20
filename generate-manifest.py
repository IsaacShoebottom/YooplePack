import sys
import json

def main():
    # Parse first arg for path to dependencies
    deps_file = sys.argv[1]
    
    NAME = "YooplePack"
    VERSION = "1.0.0"
    WEBSITE = "https://git.shoebottom.ca/IsaacShoebottom/YooplePack"
    DESCRIPTION = "Modpack for the Yoople server"

    # Read dependencies file
    # Each line is a dependency, simply parse line and put in array
    deps = []
    with open(deps_file, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                deps.append(line)

    # Create manifest
    manifest = {
        "name": NAME,
        "version_number": VERSION,
        "website_url": WEBSITE,
        "description": DESCRIPTION,
        "dependencies": deps
    }

    # Write manifest to file
    with open("manifest.json", "w") as f:
        json.dump(manifest, f, indent=4)

if __name__ == "__main__":
    main()