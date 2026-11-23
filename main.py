"""One Line, Zero Use: write a single hilariously useless superpower line."""

LINE = "I can turn invisible, but only when I'm alone in a locked room with the lights off."

def main() -> None:
    import os

    os.makedirs("/output", exist_ok=True)
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
