import subprocess
from time import sleep

from win10toast import ToastNotifier

from avito import AvitoSearch
from config import QUERY, SLEEP_TIME, BROWSER_DIR, BROWSER_FILENAME
from models import Ad, db
from utils import is_new, add_db_entry
from youla import YoulaSearch

if __name__ == '__main__':
    db.create_tables([Ad], safe=True)

    av = AvitoSearch(QUERY)

    y = YoulaSearch(QUERY)
    y.set_location()

    toaster = ToastNotifier()

    while True:
        items = y.check_new()
        items.extend(av.check_new())

        for x in items:
            ad_url = x['url']
            ad_title = x['title']

            if not is_new(ad_url, ad_title):
                continue
            add_db_entry(ad_url, ad_title)

            toaster.show_toast(
                'New ad posted',
                x['title'],
                icon_path='favicon.ico',
                duration=10,
                threaded=True,
            )

            command = f'{BROWSER_FILENAME} {x["url"]}'
            subprocess.Popen(command, cwd=BROWSER_DIR, shell=True)
        sleep(SLEEP_TIME)
