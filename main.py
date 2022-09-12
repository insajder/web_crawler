from application import create_app

def start_ngrok():
    from pyngrok import ngrok
    url = ngrok.connect(5000)
    print(url)

if __name__ == '__main__':
    app = create_app()
    start_ngrok()
    app.run()
