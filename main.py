from app import app

if __name__ == "__main__":
    from waitress import serve
    # Change host='0.0.0.0' so it’s accessible on cloud
    serve(app, host="0.0.0.0", port=8080)
