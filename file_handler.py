def load_stories(filename):
    """ Loads data from specified file. Returns a list of entries with
        their specific field values.
    """
    stories = list()
    id = 1
    try:
        with open(filename, 'r') as workfile:
            for line in workfile:
                stories.append(list(str(id)) + line.split('#'))
                id += 1
    except FileNotFoundError:
        stories = None
    return stories


def save_stories(new_entries, filename="stories.csv"):
    try:
        with open(filename, 'a') as workfile:
            for new_entry in new_entries:
                workfile.write('#'.join(new_entry) + '\n')
    except FileNotFoundError:
        with open(filename, 'w') as workfile:
            for new_entry in new_entries:
                workfile.write('#'.join(new_entry) + '\n')
