from pprint import pprint

from database import Database

import flet

db = Database()


def main(page: flet.Page):
    page.title = ''
    page.theme_mode = 'dark'
    page.vertical_alignment = flet.MainAxisAlignment.CENTER
    page.update()

    # auth panel

    def validate(e):
        if all([auth_username_panel.value, auth_password_panel.value]):
            btn_auth.disabled = False
        page.update()

    def auth(e):
        username = auth_username_panel.value
        password = auth_password_panel.value
        if len(username) > 0 and len(password) > 0:
            user_exists = db.auth_user(username=username, password=password)
            if user_exists:
                print(dir(page))
        page.remove(auth_panel)

    auth_username_panel = flet.TextField(label='username', width=250, on_change=validate)
    auth_password_panel = flet.TextField(label='password', width=250, on_change=validate, password=True)
    btn_auth = flet.OutlinedButton(text='Login', width=250, on_click=auth, disabled=True)

    auth_panel = flet.Row(
        [
            flet.Column(
                [
                    flet.Text('Authentication'),
                    auth_username_panel,
                    auth_password_panel,
                    btn_auth
                ]
            )
        ], alignment=flet.MainAxisAlignment.CENTER
    )

    page.add(auth_panel)


if __name__ == '__main__':
    flet.app(target=main, view=flet.AppView.WEB_BROWSER, port=8000)
