from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Planning',
  'priority': 'High',
  'duration': '1 hr',
}, {
  'id': 2,
  'title': 'Designing',
  'priority': 'High',
  'duration': '3 hr',
}, {
  'id': 3,
  'title': 'Execution',
  'priority': 'High',
  'duration': '5 hr',
}, {
  'id': 4,
  'title': 'Testing',
  'priority': 'High',
  'duration': '7 hr',
}]


@app.route("/")
def hello_world():
  return render_template('index.html', jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
