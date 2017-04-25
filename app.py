from flask import Flask, render_template, request
from file_handler import load_stories, save_stories
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
@app.route('/list', methods=['GET', 'POST'])
def list_stories():
    if request.method == 'POST':
        new_entry = list()
        new_entries = list()
        fields = ['story_title', 'user_story', 'acc_criteria', 'business_value', 'estimation', 'status']
        for field in fields:
            new_entry.append(request.form[field])
        new_entries.append(new_entry)
        save_stories(new_entries, 'stories.csv')
    stories = load_stories('stories.csv')
    table_header = ['ID', 'Story Title', 'User Story', 'Acceptance criteria', 'Business Value', 'Estimation', 'Status']
    return render_template('list.html', stories=stories, table_header=table_header)


@app.route('/story')
@app.route('/story/<story_id>')
def new_story(story_id=None):
    if story_id:
        edited_entry = load_stories('stories.csv')[int(story_id)-1]
        return render_template('story.html', story_id=story_id, editing=edited_entry)
    return render_template('story.html', story_id=story_id)


if __name__ == '__main__':
    app.run(debug=True)