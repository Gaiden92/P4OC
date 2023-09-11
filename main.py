from views.main_view import MainView


def main():
    launch = MainView("database/db.json")
    launch.display_main_programm_view()


if __name__ == "__main__":
    main()
