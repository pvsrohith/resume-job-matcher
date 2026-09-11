from flask import Flask, request, jsonify
from matcher import rank_resumes

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({"status": "ok", "service": "resume-job-matcher"})

@app.route("/match", methods=["POST"])
def match():
    data = request.get_json(force=True)
    job_description = data.get("job_description", "")
    resumes = data.get("resumes", [])

    if not job_description or not resumes:
        return jsonify({"error": "job_description and resumes are required"}), 400

    ranked = rank_resumes(job_description, resumes)
    return jsonify({"results": ranked})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
