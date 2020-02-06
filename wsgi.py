from hello_app.webapp import app

application = app

if __name__ == "__main__":
    app.run(port='5001')