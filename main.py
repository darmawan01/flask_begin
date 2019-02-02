from app import app
from api.user import api

app.register_blueprint(api, url_prefix="/api/user")

if __name__ == "__main__":
    app.run(debug=True)