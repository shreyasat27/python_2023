from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/convert_time.py', methods=['POST'])
def convert_time():
    time = request.form['time']
    converted_time = convert_to_12_hour_format(time)
    return render_template('result.html', time=time, converted_time=converted_time)


def convert_to_12_hour_format(time):
    # Splitting the time into hours and minutes
    hours, minutes = time.split(':')

    # Converting hours to integer
    hours = int(hours)

    # Determining AM/PM
    if hours >= 12:
        period = 'PM'
        hours -= 12
    else:
        period = 'AM'

    # Handling special cases
    if hours == 0:
        hours = 12

    # Formatting the converted time
    converted_time = f'{hours}:{minutes} {period}'
    return converted_time


if __name__ == '__main__':
    app.run()
