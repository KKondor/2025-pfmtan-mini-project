from flask import Flask, jsonify, request, render_template
from services import JokeService
from repository import JokeRepository

app = Flask(
    __name__,
    template_folder="../src/pages",
    static_folder="../src/pages/"
)

repo = JokeRepository()
service = JokeService(repo)

@app.route('/')
def main_page():
    return render_template('main-page/main-page.html')

@app.route('/leaderboard-page')
def leaderboard_page():
    return render_template('leaderboard-page/leaderboard-page.html')

@app.route('/joke', methods=['GET'])
def get_joke():
    joke = service.generate_joke()
    return jsonify({"id": joke.id, "text": joke.text, "rating": joke.rating})

@app.route('/leaderboard', methods=['GET'])
def get_leaderboard():
    jokes = service.get_leaderboard()
    return jsonify([{"id": joke.id, 
                     "text": joke.text, 
                     "rating": joke.rating} for joke in jokes])

@app.route('/joke/<int:id>/rate', methods=['POST'])
def rate_joke(id):
    data = request.get_json()
    value = data.get("value")
    try:
        service.rate_joke(id, value)
        return jsonify({"success": True}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except RuntimeError as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)