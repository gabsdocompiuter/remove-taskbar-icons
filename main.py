import re
import time

from pywinauto import Desktop, WindowSpecification


DESKTOP = Desktop(backend="uia")
TASKBAR = DESKTOP.window(
    class_name="Shell_TrayWnd"
)


def icon_pinned(icon_title: str) -> bool:
    for element in TASKBAR.descendants():
        element_text: str = element.window_text()

        if (icon_title in element_text):
            return True
    else:
        return False


def unpin_icon(icon_title: str) -> None:
    print(fr"Desfixando ícone {icon_title}...")
    time.sleep(1)

    if not icon_pinned(icon_title):
        print(fr"Ícone {icon_title} não fixado")
        return

    icon_title_escaped: str = re.escape(icon_title)

    icon: WindowSpecification = TASKBAR.child_window(
        title_re=fr".*{icon_title_escaped}.*"
    )

    icon.wait("visible", timeout=5)
    icon.right_click_input()

    time.sleep(1)

    menu_list = DESKTOP.window(
        title_re=fr"Lista de Atalhos de {icon_title_escaped}.*",
        class_name="Windows.UI.Core.CoreWindow"
    )

    menu_list.wait("exists visible", timeout=5)

    unpin_button = menu_list.child_window(
        auto_id="TaskbarUnpin",
        control_type="ListItem"
    )

    unpin_button.wait("exists visible enabled", timeout=5)
    unpin_button.click_input()


if __name__ == '__main__':
    unpin_icon("Outlook (classic)")
    unpin_icon("Excel")
    unpin_icon("Word")
