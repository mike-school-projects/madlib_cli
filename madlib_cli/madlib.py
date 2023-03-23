def main():
    # print intro
    intro()

    # Read template file
    template_content = read_template("../assets/dark_and_stormy_night_template.txt")

    # Read number of inputs, store to dict
    stripped, parts = parse_template(template_content)

    # Prompt for user input
    words = user_input(parts)

    # Generate new file with user input
    new_story = merge(stripped, words)

    save_to_file(new_story)

def intro():
    print("*"*32)
    print("Welcome to the Mad Lib Game!")
    print("You will be prompted to enter in some random words")
    print("When complete, a story will be generated based on your input")
    print("*"*32)
    print("")

def read_template(filename):
    try:
        with open(filename, "r") as template_file:
            template_content = template_file.read()
            template_content = template_content.strip()
            return template_content
    except FileNotFoundError:
        raise FileNotFoundError

def parse_template(template):
    count = template.count("{")

    if count == 0:
        return "no prompts!"

    temp_template = template
    parts = []
    stripped = ""

    for bracket in range(count):
        # Find index of 1st { and }
        start = temp_template.index("{")
        end = temp_template.index("}")

        stripped = stripped + temp_template[0:start+1] + "}"
        parts.append(temp_template[(start+1):end])

        # delete words up to first }
        temp_template = temp_template[(end+1):]

    # add in last part of template after last }
    stripped = stripped + temp_template

    parts = tuple(parts)

    return stripped, parts

def user_input(prompt):
    # Given a tuple with a list of prompts, return a list with user generated words
    inputs = []

    for word_prompt in prompt:
        inputs.append(input(f"{word_prompt}: "))

    return inputs

def merge(stripped, words):
    new_story = stripped

    for word in words:
        index = new_story.index("{")

        # remove {}, add in word
        new_story = new_story[0:index] + word + new_story[index+2:]

    # Make output format prettier
    print("")
    print(new_story)
    print("")

    return new_story

def save_to_file(story):
    with open("story.txt", 'w') as new_file:
        new_file.write(story)

if __name__ == "__main__":
    main()