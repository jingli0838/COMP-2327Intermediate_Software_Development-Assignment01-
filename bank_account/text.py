
from datetime import date, timedelta


TEN_YEARS_AGO = date.today()- timedelta(days = 10 * 365.25)
print(TEN_YEARS_AGO)