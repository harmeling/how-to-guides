#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python feedback_mail.py "harmeling" "harmeling@hhu.de" "Results of the exam for 'Machine Learning' (2021-02-17)"
# python feedback_mail.py "harmeling" "harmeling@hhu.de" "Results of the exam for 'Programmierung' (2021-02-22)"


import re
import smtplib

from argparse import ArgumentParser, ArgumentTypeError
from email.message import EmailMessage
from getpass import getpass
from os.path import isfile
from glob import glob
from time import sleep

def email_type(email):
    if not re.match(r'[^@]+@[^@]+\.[^@]+', email):
        raise ArgumentTypeError('is not a valid mail address')
    return email


SMTP_SERVER = 'mail.hhu.de'

ADDRESS_PREFIX = '@uni-duesseldorf.de'

HEADER = """\
Hallo!

Diese Nachricht wurde automatisch generiert (do not reply!).

Klausureinsicht (nur bis Freitag 5.3.2021)
* Die Klausureinsicht findet komplett ueber RocketChat statt!
* Bei Fragen zu einzelnen Aufgaben schreiben Sie bitte eine 
  Direktnachricht (in RocketChat) an die jeweilige Korrektorin.
* Die RocketChat-Kennung des Korrektors steht meistens in Klammern
  vor den Punkten ( z.B. "(harmeling) 13/13" )
* Sie muessen Ihre Anfrage bis Freitag 5.3.2021 stellen.
* Danach ist keine Anfrage mehr moeglich!

Hier ist Ihr Feedback fuer die Klausur Programmierung (2021-02-22):

"""

FOOTER = """
Mit freundlichen Gruessen,
Stefan Harmeling

"""

SENT_MSG_FILE = 'already_sent_feedback.txt'
WAIT_SECONDS_BETWEEN_EMAIL = 4


def main():
    parser = ArgumentParser()
    parser.add_argument('sender_name')
    parser.add_argument('sender_address', type=email_type)
    parser.add_argument('subject')
    args = parser.parse_args()
    

    print('Connecting to SMTP server at', SMTP_SERVER)
    username = input('Username: ')
    password = getpass()

    # connect to SMTP server
    try:
        connection = smtplib.SMTP_SSL(SMTP_SERVER)
        connection.set_debuglevel(False)
        connection.login(username, password)
        del username, password
        print('Login successful')
    except Exception as e:
        print('Login failed:', e)
        print('Exiting...')
        exit(1)


    already_sent = []
    if isfile(SENT_MSG_FILE ):
        with open(SENT_MSG_FILE , 'r') as f:
            already_sent = f.read().splitlines()
            
            
    pattern = re.compile(r'(?P<unikennung>[a-zA-Z]+([0-9]{3})?)')
    # the question mark at the end ensure that also Schuelerstudents are found
    # however, there should be any other folders in there
    
    # names + feedback
    all_submissions = {}
    messages = []

    email_from = f'{args.sender_name} <{args.sender_address}>'
    unmatched_files = []

    # iterate over all files in the directory
    for filename in glob('*/'):
        result = pattern.match(filename)
        if result is None:
            unmatched_files.append(filename)
            continue
        
        name = result.groupdict()['unikennung']
        address = f'{name}{ADDRESS_PREFIX}'
        if address in already_sent:
            continue
        
        text = ""
        for feedback in [f'{name}/{name}-e{nr}.txt' for nr in range(1,8+1)]:
            with open(feedback,'r') as f:
                text += f.read()+'\n'
                
        if address not in all_submissions:
            all_submissions[address] = text
        else:
            print('warning, duplicate '+address)

        
    for address,text in all_submissions.items():
        try:
            # create an e-mail message
            msg = EmailMessage()
            msg['Subject'] = args.subject
            msg['From'] = email_from
            msg['To'] = address
            
            
            msg.set_content(f'{HEADER}{text}{FOOTER}{args.sender_name}')
            messages.append(msg)
        except Exception as e:
            print('Error: ', e)


    if len(messages) == 0:
        print('No messages found, exiting...')
        exit(0)

    if len(unmatched_files) > 0:
        print('Found files that do not match the name pattern, exiting...')
        for filename in unmatched_files:
            print(filename)

    # print all messages to the user before sending
    for msg in messages:
        print('===============================================')
        print(f'Subject: {msg["Subject"]}')
        print(f'From:    {msg["From"]}')
        print(f'To:      {msg["To"]}')
        print('-----------------------------------------------')
        print(msg.get_content(), end='')
        print('===============================================')

    print('===============================================')
    if input('Send all mails? (y/N) ') == 'y':
        print('Sending...')

        for msg in messages:
            try:
                connection.send_message(msg)
                print(f'Sent mail to {msg["To"]}')
                with open(SENT_MSG_FILE , 'a') as f:
                    f.write(msg['To']+'\n')
            except Exception as e:
                print(f'Error while sending mail to {msg["To"]}: {e}')
            sleep(WAIT_SECONDS_BETWEEN_EMAIL)

        connection.quit()
    else:
        print('No mails have been sent')


if __name__ == '__main__':
    main()
