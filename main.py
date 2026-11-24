"""Make the AI Judge Laugh: the Office Joke Open — one-line office joke entry.

Writes the joke to /output/entry.txt (UTF-8, 1-200 chars).
"""

JOKE = (
    "The office microwave finishes in two minutes, then beeps every "
    "thirty seconds until you open it \u2014 it's the only manager here "
    "that actually follows up."
)


def load_joke():
    """Return the entry joke text."""
    return JOKE


def validate_joke(joke):
    """Check the gate: UTF-8, 1-200 chars, not only whitespace."""
    if not isinstance(joke, str):
        raise TypeError("joke must be a string")
    if not joke.strip():
        raise ValueError("joke must not be empty or only whitespace")
    if len(joke) > 200:
        raise ValueError("joke exceeds 200 characters: %d" % len(joke))
    joke.encode("utf-8")
    return joke


def write_entry(joke, path="/output/entry.txt"):
    """Write the validated joke to path, creating parent dirs as needed."""
    import os

    validate_joke(joke)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(joke)
    return path


def main():
    joke = load_joke()
    path = write_entry(joke)
    print("Wrote %d chars to %s" % (len(joke), path))


if __name__ == "__main__":
    main()
