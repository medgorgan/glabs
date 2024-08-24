from flask import Flask, render_template
import folium

map = folium.Map(location = [40.769361, -73.977655], zoom_start = 10)

# Grid DD Coordinates 
folium.Marker(location = [40.769361, -73.977655],
radius = 100, popup = "Central Park").add_to(map)

# Save HTML in the templates directory.
map.save("\\templates\\map.html")

app = Flask(__name__)

@app.route("/map")
def map():
    return render_template('map.html')


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
