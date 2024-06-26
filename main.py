import flet
from flet_core import ControlEvent

from database import Database

db = Database()


async def main(page: flet.Page) -> None:
    """
    Auth panel.
    """

    page.title = 'Authentication'
    page.theme_mode = 'dark'
    page.vertical_alignment = flet.MainAxisAlignment.CENTER
    page.fonts = {
        'Rajdhani': 'fonts/Rajdhani/Rajdhani-Medium.ttf'
    }
    page.theme = flet.Theme(font_family='Rajdhani')
    await page.update_async()

    async def validate(e: ControlEvent) -> None:
        """
        Validates inputs filling.
        """

        username = username_panel.value
        password = password_panel.value
        if all([username, password]):
            btn_auth.disabled = False
            btn_register.disabled = False
        elif not username or not password:
            btn_auth.disabled = True
            btn_register.disabled = True
        username_panel.border_color = None
        password_panel.border_color = None
        btn_auth.text = 'Login'
        btn_register.text = 'Register'
        await page.update_async()

    async def auth(e: ControlEvent) -> None:
        """
        Authenticates user if given credentials are valid.
        """

        username = username_panel.value
        password = password_panel.value
        if len(username) > 0 and len(password) > 0:
            user_exists = db.auth_user(username=username, password=password)
            if user_exists:
                btn_auth.text = 'Logged in successfully!'
                await page.update_async()
            else:
                username_panel.border_color = 'red'
                password_panel.border_color = 'red'
        await page.update_async()

    async def register(e: ControlEvent) -> None:
        """
        Registers user.
        """

        username = username_panel.value
        password = password_panel.value
        if len(username) > 0 and len(password) > 0:
            create_user = db.create_user(username=username, password=password)
            if create_user:
                btn_register.text = 'Registered successfully!'
                await page.update_async()

    async def move_to_register(e: ControlEvent) -> None:
        """
        Updates page for registration.
        """

        page.route = '/registration'
        page.title = 'Registration'

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

        await page.update_async()

    async def move_to_login(e: ControlEvent) -> None:
        """
        Updates page for authentication.
        """

        page.route = '/'
        page.title = 'Authentication'

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

        await page.update_async()

    app_label = flet.Container(
        content=flet.Text(value='Authentication/registration app on Flet', size=25),
        margin=flet.Margin(bottom=40, top=0, left=0, right=0),
        alignment=flet.Alignment(0, 0)
    )

    username_panel = flet.TextField(
        label='username',
        width=250,
        on_change=validate
    )
    password_panel = flet.TextField(
        label='password',
        width=250,
        on_change=validate,
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
                    flet.Text(value='Authentication'),
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
                    flet.Text(value='Registration'),
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

    await page.add_async(app_label, auth_panel, btn_move_to_register)


if __name__ == '__main__':
    flet.app(target=main, view=flet.AppView.WEB_BROWSER, port=8734)
