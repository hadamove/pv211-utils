import datetime
import pkg_resources
from typing import Optional

from ..leaderboard import GoogleSpreadsheetLeaderboardBase


class CranfieldLeaderboard(GoogleSpreadsheetLeaderboardBase):
    def get_competition_start(self) -> datetime.date:
        return datetime.date(2021, 3, 1)

    def get_competition_end(self) -> datetime.date:
        return datetime.date(2021, 4, 18)

    def _get_key_path(self) -> str:
        key_path = pkg_resources.resource_filename('pv211_utils', 'data/pv211-leaderboard-b8e892e3e8bb.json')
        return key_path

    def _get_spreadsheet_key(self) -> str:
        spreadsheet_key = '1CNeZESOrPxBs3U0FeGtaDPLJQkb2Ubsr0aCvyNIwdtM'
        return spreadsheet_key

    def get_public_url(self) -> Optional[str]:
        return (
            'https://docs.google.com/spreadsheets/d/e/'
            '2PACX-1vRRR4eDkQIWx5FSU08Uj5DciWwxNfHJeLruNR1T0WW9xmSsYl457Zqv5SlA1jfvsYHpsaUw_8P3z1OF/pubhtml'
        )
