import sys
from datetime import datetime, timedelta

sys.path.append("./")

from utils import log
from v2.etl.user import ETLUser
from v2.etl.session import ETLSession
from v2.etl.lead import ETLLead
from v2.etl.progress import ETLProgress
from v2.etl.pageview import ETLPageView
from v2.etl.transaction import ETLTransaction
from v2.etl.campaign import ETLCampaign

date_until = datetime.now() - timedelta(days=1)
if "--full" in sys.argv:
    date_until = datetime(2010, 12, 1)

user = ETLUser(date_until)
session = ETLSession(date_until)
lead = ETLLead(date_until)
progress = ETLProgress(date_until)
pageview = ETLPageView(date_until)
transaction = ETLTransaction(date_until)
campaign = ETLCampaign(date_until)

log.info(f"Iniciando carga. Data limite: {date_until}...")

user.run()
session.run()
pageview.run()
transaction.run()
lead.run()
progress.run()
campaign.run()
