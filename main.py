import flet

from database import Database

db = Database()
FONT_FAMILY = 'Rajdhani'


def main(page: flet.Page):
    page.title = 'To Do | Authentication'
    page.theme_mode = 'dark'
    page.vertical_alignment = flet.MainAxisAlignment.CENTER
    page.fonts = {
        'Rajdhani': 'Rajdhani/Rajdhani-Medium.ttf'
    }
    page.update()

    # auth panel

    def validate(e):
        if all([username_panel.value, password_panel.value]):
            btn_auth.disabled = False
        page.update()

    def auth(e):
        username = username_panel.value
        password = password_panel.value
        if len(username) > 0 and len(password) > 0:
            user_exists = db.auth_user(username=username, password=password)
            if user_exists:
                print(200)
            else:
                print(404)

    def register(e):
        username = username_panel.value
        password = password_panel.value
        if len(username) > 0 and len(password) > 0:
            create_user = db.create_user(username=username, password=password)
            print(create_user)

    def move_to_register(e):
        page.route = '/registration'
        page.title = 'To Do | Registration'

        page.views.clear()
        page.views.append(
            flet.View(
                route='/register',
                controls=[
                    app_label,
                    register_panel,
                    btn_move_to_login
                ],
                vertical_alignment=flet.MainAxisAlignment.CENTER
            )
        )

        page.update()

    def move_to_login(e):
        page.route = '/'
        page.title = 'To Do | Authentication'

        page.views.clear()
        page.views.append(
            flet.View(
                route='/',
                controls=[
                    app_label,
                    auth_panel,
                    btn_move_to_register
                ],
                vertical_alignment=flet.MainAxisAlignment.CENTER
            )
        )

        page.update()

    app_label = flet.Container(
        content=flet.Text(value='To Do app on Flet', size=25, font_family=FONT_FAMILY),
        margin=flet.Margin(bottom=40, top=0, left=0, right=0),
        alignment=flet.Alignment(0, 0)
    )

    username_panel = flet.TextField(
        label='username',
        width=250,
        on_change=validate,
        label_style=flet.TextStyle(font_family=FONT_FAMILY)
    )
    password_panel = flet.TextField(
        label='password',
        width=250,
        on_change=validate,
        label_style=flet.TextStyle(font_family=FONT_FAMILY),
        password=True
    )
    btn_auth = flet.OutlinedButton(
        text='Login',
        width=250,
        on_click=auth,
        disabled=True
    )
    btn_register = flet.OutlinedButton(
        text='Register',
        width=250,
        on_click=register,
        disabled=True
    )

    auth_panel = flet.Row(
        controls=[
            flet.Column(
                [
                    flet.Text(value='Authentication', font_family=FONT_FAMILY),
                    username_panel,
                    password_panel,
                    btn_auth
                ]
            )
        ], alignment=flet.MainAxisAlignment.CENTER
    )
    register_panel = flet.Row(
        controls=[
            flet.Column(
                [
                    flet.Text(value='Registration', font_family=FONT_FAMILY),
                    username_panel,
                    password_panel,
                    btn_register
                ]
            )
        ], alignment=flet.MainAxisAlignment.CENTER
    )

    btn_move_to_register = flet.Container(
        content=flet.TextButton(text='Register now', on_click=move_to_register),
        margin=flet.Margin(top=20, bottom=0, left=0, right=0),
        alignment=flet.Alignment(0, 0),
    )
    btn_move_to_login = flet.Container(
        content=flet.TextButton(text='Already have an account?', on_click=move_to_login),
        margin=flet.Margin(top=20, bottom=0, left=0, right=0),
        alignment=flet.Alignment(0, 0),
    )

    page.add(app_label, auth_panel, btn_move_to_register)


if __name__ == '__main__':
    flet.app(target=main, view=flet.AppView.WEB_BROWSER, port=8734, assets_dir='fonts')
