import datetime


def fomat_date(date):
    return datetime.datetime.strptime(str(date), '%Y-%m-%d').strftime('%b-%Y')
