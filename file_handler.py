def load_stories(filename="stories.csv"):
    """ Loads data from specified file. Returns a list of entries with
        their specific field values.
    """
    stories = list()
    id = 1
    try:
        with open(filename, 'r') as workfile:
            for line in workfile:
                line = line.strip('\n')
                stories.append(list(str(id)) + line.split('#'))
                id += 1
    except FileNotFoundError:
        stories = None
    return stories


def save_story(new_entry, filename="stories.csv"):
    try:
        with open(filename, 'a') as workfile:
            workfile.write('#'.join(new_entry) + '\n')
    except FileNotFoundError:
        with open(filename, 'w') as workfile:
            workfile.write('#'.join(new_entry) + '\n')


def delete_story(delete_id, filename="stories.csv"):
    stories = list()
    id = 1
    try:
        with open(filename, 'r') as workfile:
            for line in workfile:
                if id != int(delete_id):
                    stories.append(line)
                id += 1
    except FileNotFoundError:
        stories = None
    else:
        with open(filename, 'w') as workfile:
                for story in stories:
                    workfile.write(story)


def load_story(story_id, filename="stories.csv"):
    id = 1
    try:
        with open(filename, 'r') as workfile:
            for line in workfile:
                if id == int(story_id):
                    line = line.strip('\n')
                    return (list(str(id)) + line.split('#'))
                id += 1
    except FileNotFoundError:
        return


def modify_story(story_id, new_entry, filename="stories.csv"):
    id = 1
    stories = list()
    try:
        with open(filename, 'r') as workfile:
            for line in workfile:
                if id == int(story_id):
                    stories.append('#'.join(new_entry) + '\n')
                else:
                    stories.append(line)
                id += 1
    except FileNotFoundError:
        pass
    else:
        with open(filename, 'w') as workfile:
            for story in stories:
                workfile.write(story)
