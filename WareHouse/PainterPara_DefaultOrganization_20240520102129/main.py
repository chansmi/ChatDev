from app import App
if __name__ == "__main__":
    app = App()
    app.initialize()
    while True:
        input = get_user_input()  # Develop a function to collect user input
        app.handle_input(input)
        app.render()