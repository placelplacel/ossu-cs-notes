def extract_chat(input_filename, output_filename):
    """
    Assumes input_filename and output_filename are both strings.
    Writes the chat messages into an output file at 'output_filename' if everything goes as expected.
    """
    assert type(input_filename) == str and type(output_filename) == str, "Invalid arguments provided."
    try:
        input_file = open(input_filename, 'r')
        output_file = open(output_filename, 'w')
    except FileNotFoundError:
        print("Could not open file:", input_filename)
    except Exception as e:
        print("Something went wrong:", e)
    else:
        for line in input_file:
            if "[Render thread/INFO]: [CHAT]" in line and "into the lobby!" not in line:
                output_file.write(line)
    finally:
        input_file.close()
        output_file.close()

extract_chat("latest.log", "latest-filtered.log")
