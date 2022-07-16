from background_task import background
from .models import Auction

@background(schedule=5)
def check_status(pk):
    print('test')