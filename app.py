from flask import Flask, render_template, request
from file_handler import load_stories, save_story, delete_story, load_story, modify_story
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
@app.route('/list', methods=['GET', 'POST'])
def list_stories():
    delete_id = request.args.get('delete', '')
    if delete_id != '':
        delete_story(delete_id, 'stories.csv')
    if request.method == 'POST':
        new_entry = list()
        fields = ['story_title', 'user_story', 'acc_criteria', 'business_value', 'estimation', 'status']
        for field in fields:
            new_entry.append(request.form[field])
        if request.form['story_id'] == '':
            save_story(new_entry, 'stories.csv')
        else:
            modify_story(request.form['story_id'], new_entry, 'stories.csv')
    stories = load_stories('stories.csv')
    table_header = ['ID', 'Story Title', 'User Story', 'Acceptance criteria', 'Business Value', 'Estimation', 'Status']
    return render_template('list.html', stories=stories, table_header=table_header)


@app.route('/story')
@app.route('/story/<story_id>')
def new_story(story_id=None):
    if story_id:
        edited_entry = load_story(story_id, 'stories.csv')
        return render_template('story.html', story_id=story_id, editing=edited_entry)
    return render_template('story.html', story_id='', editing=['' * 7])


if __name__ == '__main__':
    app.run(debug=True)
