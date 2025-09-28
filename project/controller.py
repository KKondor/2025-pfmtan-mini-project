from flask import jsonify, request, render_template

class FlaskController:
    def __init__(self, app, service):
        self.app = app
        self.service = service
        self.register_routes()

        @app.errorhandler(Exception)
        def handle_exception(e):
            if isinstance(e, ValueError):
                return jsonify({"error": str(e)}), 400
            elif isinstance(e, RuntimeError):
                return jsonify({"error": str(e)}), 500
            else:
                return jsonify({"error": "Unexpected server error"}), 500

    def register_routes(self):
        app = self.app
        service = self.service

        @app.route("/")
        def main_page():
            return render_template("main-page.html")

        @app.route("/leaderboard-page")
        def leaderboard_page():
            return render_template("leaderboard-page.html")

        @app.route("/joke", methods=["GET"])
        def get_joke():
            joke = service.generate_joke()
            return jsonify({
                "id": joke.id,
                "setup": joke.setup,
                "punchline": joke.punchline,
                "rating": joke.rating
            }), 200

        @app.route("/leaderboard", methods=["GET"])
        def get_leaderboard():
            jokes = service.get_leaderboard()
            return jsonify([{
                "id": joke.id,
                "setup": joke.setup,
                "punchline": joke.punchline,
                "rating": joke.rating
            } for joke in jokes]), 200

        @app.route("/joke/<int:id>/rate", methods=["POST"])
        def rate_joke(id):
            data = request.get_json()
            value = data.get("value")
            service.rate_joke(id, value)
            return jsonify({"success": True}), 200
