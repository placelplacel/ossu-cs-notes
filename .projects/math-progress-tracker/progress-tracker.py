from datetime import date, timedelta

SAVE_FILE_NAME = "save.txt"

def read_save(filename):
    """
    Assumes that filename is a string.
    Returns a dictionary associating the keys to the values.
    """
    assert type(filename) == str, "Invalid arguments provided."
    result = {}
    try:
        input_file = open(filename, "r")
        for line in input_file:
            tokens = line.split(":")
            if len(tokens) == 2:
                result[tokens[0]] = tokens[1][:-1]
    finally:
        input_file.close()
    return result


def write_save(filename, save_data):
    """
    Assumes that filename is a string and save_data is a dictionary.
    Writes the mappings from save_data to a file with the given filename where
    every mapping is on its own separate line and of format 'key:value'.
    """
    assert type(filename) == str and type(save_data) == dict, "Invalid arguments provided."
    try:
        output_file = open(filename, "w")
        for key in save_data:
            output_file.write(str(key) + ":" + str(save_data[key]) + "\n")
    finally:
        output_file.close()


def analyze_save(filename):
    save_data = read_save(filename)
    date_started = date.fromisoformat(save_data["date_started"])
    date_due = date.fromisoformat(save_data["date_due"])
    date_last_logged = date.fromisoformat(save_data["date_last_logged"])
    date_today = date.today() - timedelta(days=1)
    page_end = int(save_data["page_end"])
    page_current = int(save_data["page_current"])

    days_left = (date_due - date_today).days
    pages_left = page_end - page_current
    
    print("Start Date:", date_started)
    print("Due Date:", date_due)
    print("Pages Left:", pages_left)
    print("Days Left:", days_left)
    print("Required Average: %f" % (pages_left/days_left))
    if date_last_logged == date_today:
        print("You have already logged your progress today!")
    else:
        days_idled = (date_today - date_last_logged).days
        print("You haven't logged your progress in the last %i days." % days_idled)
        while True:
            user_input = input("Enter the page number that you are ending today on or type 'c' to cancel: ")
            if user_input == "c":
                break
            else:
                try:
                    page_new = int(user_input)
                    save_data["page_current"] = page_new
                    save_data["date_last_logged"] = date_today
                    
                    pages_done = page_new - page_current
                    print("Logged %i pages over %i days. Your average was %f pages a day." % (pages_done, days_idled, pages_done/days_idled))
                    print("Your new required average is %f pages for %i days" % ((page_end - page_new)/days_left, days_left))
                    
                    write_save(SAVE_FILE_NAME, save_data)
                    break
                except ValueError:
                    print("Invalid command or input.")
                except:
                    print("Something went wrong.")
                    return


def test_read_save():
    """
    Returns True if the test succeeds, False otherwise.
    """
    print("Testing read_save():", end=" ")
    expected = {"key1":"val1", "":"val2", "key3":"", "":""}
    actual = read_save("read_test.txt")
    if actual != expected:
        print("FAILED")
        print("- Input: 'read_test.txt'")
        print("- Expected Output:", expected)
        print("- Actual Output:", actual)
        return False
    print("SUCCESS")
    return True


def test_write_save():
    """
    Returns True if the test succeeds, False otherwise.
    """
    if not test_read_save():
        print("Testing write_save() requires read_save() to work.")
        return
    print("Testing write_save():", end=" ")
    expected = read_save("read_test.txt")
    write_save("write_test.txt", expected)
    actual = read_save("write_test.txt")
    if actual != expected:
        print("FAILED")
        print("- Input: 'write_test.txt', read_save('read_test.txt')")
        print("- Expected Output:", expected)
        print("- Actual Output:", actual)
        return False
    print("SUCCESS")
    return True


# test_read_save()
# test_write_save()
analyze_save(SAVE_FILE_NAME)
