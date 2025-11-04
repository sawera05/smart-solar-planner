from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    area = float(request.form.get('area'))  # area in square meters
    energy_need = float(request.form.get('energy_need'))  # kWh per day
    sunlight = float(request.form.get('sunlight'))  # sunlight hours

    # 1 solar panel = 300 watts = 0.3 kW
    # Energy per panel = 0.3 * sunlight hours (kWh/day)
    energy_per_panel = 0.3 * sunlight

    # Total panels needed
    panels_needed = energy_need / energy_per_panel

    # Cost estimate (per panel ~ Rs. 30,000)
    total_cost = panels_needed * 30000

    # Area required per panel = 1.6 m²
    total_area_needed = panels_needed * 1.6

    suggestion = ""
    if total_area_needed > area:
        suggestion = "You need more roof space or use higher efficiency panels."
    else:
        suggestion = "Perfect! Your roof size is enough for installation."

    return render_template(
        'result.html',
        panels=round(panels_needed, 2),
        cost=round(total_cost, 2),
        area_needed=round(total_area_needed, 2),
        suggestion=suggestion
    )

if __name__ == '__main__':
    app.run(debug=True)
