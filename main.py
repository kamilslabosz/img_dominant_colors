from colorthief import ColorThief
from flask import render_template, Flask
from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from werkzeug.utils import secure_filename


app = Flask(__name__)

app.config['SECRET_KEY'] = 'placeholderstringfornowalsosomenumbers123427609898234'


class UploadForm(FlaskForm):
    file = FileField()


@app.route('/', methods=['GET', 'POST'])
def upload_ang_get_palette():
    form = UploadForm()

    if form.validate_on_submit():
        filename = secure_filename(form.file.data.filename)

        color_thief = ColorThief(filename)
        palette = color_thief.get_palette(color_count=10, quality=1)
        hex_palette = ['#%02x%02x%02x' % item for item in palette]

        return render_template('index.html', form=form, palette=hex_palette)

    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)