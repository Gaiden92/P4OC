from views.main_view import MainView


def main():
    main_menu = MainView("database/db.json")
    main_menu.display_main_menu()


if __name__ == "__main__":
    main()
