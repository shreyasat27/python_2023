
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/index.html')
def home():
    return render_template('index.html')


@app.route('/generate_cool_name.py', methods=['POST'])
def generate_a_cool_name():
    city_name = request.form['city_name']
    pet_name = request.form['pet_name']
    cool_name = generate_a_cool_name(city_name, pet_name)
    return render_template('result.html', city_name=city_name, pet_name=pet_name, cool_name=cool_name)


def generate_a_cool_name(pet_name, city_name):
    cool_name = city_name[0] + pet_name[-1]+city_name[0] + pet_name[-1]
    return cool_name


#pet_name = input("Write your prt name:")
#city_name = input("write your city name:")
#cool_name = generate_a_cool_name(pet_name, city_name)

#print("Cool Name:", cool_name)


if __name__ == '__main__':
    app.run()
