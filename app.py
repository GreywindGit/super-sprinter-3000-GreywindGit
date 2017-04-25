from flask import Flask, render_template, request
from file_handler import load_stories, save_stories
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
@app.route('/list', methods=['GET', 'POST'])
def lists():
    if request.method == 'POST':
        new_entry = []
        fields = ['story_title', 'user_story', 'acc_criteria', 'business_value', 'estimation', 'status']
        for field in fields:
            new_entry.append(request.form[field])
        save_stories(new_entry, 'stories.csv')
    stories = load_stories('stories.csv')
    table_header = ['ID', 'Story Title', 'User Story', 'Acceptance criteria', 'Business Value', 'Estimation', 'Status']
    return render_template('list.html', stories=stories, table_header=table_header)


@app.route('/story')
@app.route('/story/<story_id>')
def new_story(story_id=None):
    return render_template('story.html', story_id=story_id)


if __name__ == '__main__':
    app.run(debug=True)