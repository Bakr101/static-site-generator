def extract_title(markdown: str) -> str:
    #find the first line that starts with #
    for line in markdown.split("\n"):
        if line[0] == "#" and line[1] == " ":
            return line[2:].strip()
    raise Exception("No title found")
