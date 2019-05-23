from settings import http

if __name__ == "__main__":
    app = http.create_app()
    app.run( port = 5000, debug=True)
