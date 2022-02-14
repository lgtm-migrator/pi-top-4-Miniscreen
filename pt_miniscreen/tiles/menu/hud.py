from ...pages.hud import NetworkMenuPage, OverviewPage, SettingsMenuPage, SystemMenuPage
from ..templates import MenuTile


class HUDMenuTile(MenuTile):
    def __init__(self, size, pos=(0, 0)):
        super().__init__(
            size=size,
            pos=pos,
            pages=[
                Page(size)
                for Page in (
                    OverviewPage,
                    SystemMenuPage,
                    NetworkMenuPage,
                    SettingsMenuPage,
                )
            ],
        )
