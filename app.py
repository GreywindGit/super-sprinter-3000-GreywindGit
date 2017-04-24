from flask import Flask, render_template
from file_handler import load_stories
app = Flask(__name__)


@app.route('/')
@app.route('/list')
def lists():
    stories = load_stories('stories.csv')
    table_header = ['ID', 'Story Title', 'User Story', 'Acceptance criteria', 'Business Value', 'Estimation', 'Status']
    return render_template('list.html', stories=stories, table_header=table_header)


@app.route('/story')
@app.route('/story/<story_id>')
def new_story(story_id=None):
    return render_template('story.html', story_id=story_id)


if __name__ == '__main__':
    app.run(debug=True)