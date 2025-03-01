import tomllib

with open("pyproject.toml", "rb") as f:
    try:
        data = tomllib.load(f)
        print("✅ TOML file is valid!")
    except Exception as e:
        print("❌ TOML file error:", e)
