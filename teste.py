import schedule
import time

#import psycopg2.extras
#import sys, os
from Naked.toolshed.shell import execute_rb, muterun_rb

#connection = psycopg2.connect("dbname=dados user=postgres password=123 host=localhost")
#c = connection.cursor()


def validarIPPaises():
    """arq = open('./DIY-Firewall/flags/paises.flag', 'w')

    c.execute("SELECT * FROM validarIPPaises")

    c.copy_to(arq, "validarippaises", sep=' ', columns=("flag",))
    arq.close()
    print("Arquivo TXT gerado")"""

    execute_rb('./DIY-Firewall/lib/paises.rb')
    print("Rodou o RB")
    print("Felippe fez uma alteração")
    print("Bengalinho fez uma alteração")

schedule.every(10).seconds.do(validarIPPaises)


while 1:
    schedule.run_pending()
    time.sleep(1)