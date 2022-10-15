# how-we-did-written-online-exams
created and copyright 2021-03-05 by Stefan Harmeling

In the following we describe our setup and lessons-learned from our two online exams for lecture "Machine Learning" (2021-02-17, about 80 students) and lecture "Programmierung" (2021-02-22, about 350 students).

## Conclusion (TLDR)
* interesting experiment!
* for Corona times ok
* in presence exams are better since
* cheating via communication channels can not be avoided
* cool idea for future offline exams: 
  - the student should scan their exam and 
  - let them submit their papers and PDF version
  - this can greatly simplify correction and Klausureinsicht

## Tools:
* Zoom: for video conference during the exam
* Sciebo: for exam download / upload and exam correction
* RocketChat: for Klausureinsicht

## Steps

### two weeks before: 
* send out the rules (email text see below)
* include test session for zoom video conference and 
* include test link to folder to practice upload of files (text see below)
* (missing) let them practice zipping a folder!
* set up exam meetings in zoom
  - set chat to host-only (in chat options)
  - switch-off renaming (participant options)

### a day before the exam: 
* split the registered students into groups up to 100 students for the zoom sessions by lastname (maybe next time better by unikennung), 
* post the conference links onto ILIAS with assignments (e.g. A-D, E-G, etc)

### on the day of the exam: 
* start early (7:45) to meet with all tutors (per session about three people)
* in zoom: make tutors "co-host"
* admit students one-by-one by name that are registered (listed on the Anmeldeliste)
* let students with strange names in at the very end and tell them to rename and login again
* timing for exam: "programmierung":
```
08:00 start of video conference
08:05 / 08:10 / 08:15 / 08:20 short greetings of the prof
08:25 send sciebo link to exam-pdf and upload link to the zoom chat
08:30 start to work on the exam
10:20 end of exam writing (100 min + 10 extra minutes)
10:30 Deadline for submitting the files
11:00 put link to `ls * > submitted-files.txt` on sciebo for students to check whether their file was uploaded
```
* we were giving in total 20 extra minutes and were quite generous with accepting late files

* some people asked to submit early, while we didn't object, this of course makes cheating by submitting to other people really easy

## Problems

* since students can register just before the exam, it is almost impossible to reach some students and send them information, if they had an Altzulassung and are not a member of the ILIAS lecture for the current year

* Identity check:  we randomly selected people during the exam for identity check using break-out rooms, however, the was quite cumbersome and didn't work very well

* Submission:  people had problems scanning their handwritten pages into a single PDF-file and they were unable to store that file into a folder and to zip it.  This made the correction more tedious than necessary.

* Cheating: next section

## Cheating

* the main problem of online exam is cheating by communicating via Discord or Whatsapp or other services.  I don't think there is anything we can do against it.  The problem is we do not have a real honor code and can not really penalize cheating, so the risk for the students is quite low.
* in the Machine Learning we didn't observe cheating, neither during the exam, nor finding similar solutions in the submissions
* in the Programmiung exam there was obvious cheating by copying single PDF pages from someone else (in total eight people).  Both source and sink failed the exam (the former for communicating, the latter for submitting someone else' solution).  Structure of the cheating:
```
A <--- B ---> C  # B send solution by accident to whatsapp group
                 # B wanted instead send it to himself, to transfer PDF
                 # to the computer, A and C copied PDF pages
D ---> E         # D and E share a flat, D didn't know that E scanned also
                 # some of the handwritten pages
F ---> G         # several pages of handwritten copies
```
* how did we find out?
  - the correctors are assigned to questions, so they see many solutions of the
    same exercise
  - go twice through all PDFs by hand and (i) look for inconsistencies (changed paper, changed handwriting style), (ii) find possible sources
* what checks were not successful
  - check for file sizes (to find super obvious copies)
```ls -l */*.pdf | cut -c 31-40 | sort | uniq -c | grep "   2  "```
  - transform all PDFs into single page PNGs and run image dupes detection, e.g. `findimagedupes`


## Correction
The correction and Klausureinsicht using online tools was a pleasure!

* right after submission (before unzipping), all uploaded files are zipped and stored to keep the original submission (this was important to check, if someone claims to submit something but didn't appear among the submissions)
* run scripts to unzip all files, e.g.
```aunpack -eD *.zip  # using atools```
* transform by hand everyones submission who didn't follow format
* some will be missed, and we only found out after sending out the results, because students were expecting a result where we missed their file
* some student zip their PDF by renaming it!
* for every student there is a folder name with unikennung:
```
~/programmierung/submission ls test101
test101-e1.txt test101-e3.txt test101-e5.txt test101-e7.txt test101.pdf
test101-e2.txt test101-e4.txt test101-e6.txt test101-e8.txt
```
* inside for each questions the corrector will create a text file with the correction, e.g. `test101-e4.txt` for question 4
* the first line contains the exercise number, name of korrector in brackets and number of points:
```
Exercise 6: Binärer Suchbaum (harmeling) 13/13
(a) (b) ok 2/2
(c) ok 3/3
(d) 8/8
```
* all points are put in a big spreadsheet that is edited simulateously via the sciebo webpage
* once corrections are completed use spreadsheet tricks or copy-paste to copy results to the official spreadsheet and create the grades
* upload the official spreadsheet
* automatically send out emails using the script `feedback_mail.py` (see below), which combines the txt files into a mail and sends it out

## Klausureinsicht

* only via RocketChat (one week long), the student send direct messages to the corrector and discuss about points
* the corrector can adjust the points in the spreadsheet using sciebo webpage
* finally, the official spreadsheet is updated and uploaded

## Email (send out two weeks before the exam)
```
Dear <vorname> <nachname>, 

this email contains important information about the online
exam for the lecture "machine learning". If you didn't
register in the exam, you can ignore this message. Other
read everything!

DATE AND TIME:

* 17. March 2021
11:45 start of the video conference
please bring enough time!
conference will end around 14:30.

YOUR TODOS:

* test your zoom setup! For this you can enter until Friday
the following zoom session:
https://us02web.zoom.us/j/....

* learn to scan handwritten pages with your computer or cell
phone to create a multi-page PDF-file and try to upload it
to the for-testing-only sciebo folder at
https://uni-duesseldorf.sciebo.de/s/....

* read and understand all the rules!

RULES:

* Identity: please have your student id and your photo id,
like in a usual exam, so we can check your identity.

* Exam: at the beginning of the zoom session, you get a link
to the PDF file of the exam and a link for the sciebo folder
for uploading your scanned handwritten pages.

* Sources: "open book", your books, your notes, slides, and
also other sources on the internet (but no communication
with other people!!!)

* Communication: you must only communicate with us and under
no circumstances with someone else. Violating this rule will
lead to the grade "fail" in the exam and you will be
excluded from other online exams at HHU. You can ask
questions to us via the zoom chat (chat to host) or you can
use the microphone or if nothing else works via email (see
below).

* Video conference: during the whole exam you are in a zoom
conference with us. You will first reach a waiting room and
will only be admitted to the conference, if the chosen name
is on our lists of registered students. You have to switch
on your camera, switch on your speaker and switch off your
microphone.

* Problems: if your internet connection drops, you have to
try immediately to get it running again. If you are out of
the zoom session for longer than five minutes, your exam is
over and you have to write the exam again (the running video
conference is a requirement for taking the online exam). 
However, note that such technical failure wont count as a
failed exam (for the counting of attempts).

* Submission: the exam is handwritten on paper. At the end
you have extra time to scan the exam with your computer or
cell phone (try this before the exam!) and upload to a
sciebo folder.

* Emergency contact: please send us an email
(<prof-email>, <tutor-email>)

We hope this will work for everyone! 

Best regards
```

## another info email (regarding jupyter notebook)
```
* YET ANOTHER INFO:
There will be a PDF with all exam questions and a Jupyter
Notebook file for the programming questions. For submission
please create a ZIP file named with your unikennung, i.e.
harmeling.zip that contains both files: the multi-page PDF
of your scanned handwritten solutions harmeling.pdf and also
the jupyter notebook with your code.

* PROGRAMMING TASK:
We will give you a JuPyter notebook with some missing lines
of code that you are asked to complete. Please make sure
that you have a running Python 3 distribution on your
computer (including JuPyter and NumPy) before taking the
exam. You should test your local installation with the
tutorial notebooks which are available in the Sciebo public
folder.
```

## Email in German for lecture "Programmierung"

```
Sehr geehrte/geehrter Frau/Herr <vorname> <nachname>,

diese Email enthält wichtige Informationen über die
Onlineklausur der Vorlesung "Programmierung". Falls Sie
sich nicht zur Klausur angemeldet haben, können Sie diese
Nachricht ignorieren. Andernfalls, bitte alles genau
durchlesen.

DATUM UND UHRZEIT:

* Montag 22. Februar 2021
08:00 Start der Videokonferenz
Bitte bringen Sie genug Zeit mit!
Die Videokonferenz endet um ca. 10:45.

IHRE TODOS:

* testen Sie Ihr Zoom Setup! Hierfür können Sie bis
Freitag in folgende Zoom Testsession hereingehen:
https://us02web.zoom.us/j/....

* lernen Sie, wie Sie handgeschriebenen Papierseiten mit
Ihrem Computer oder mit Ihrem Handy einscannen können und
daraus eine mehr-seitige PDF Datei erzeugen können. Testen
Sie auch, ob Sie diese Datei dann in den "for-testing-only"
sciebo Ordner unter
https://uni-duesseldorf.sciebo.de/s/....
hochladen können.

* es wird vier Zoom-Konferenzen geben. Zu welcher Sie
zugeordnet wurden, können Sie vor der Klausur (nach
Anmeldeschluss) auf der ILIAS Seite zur Vorlesung ablesen. 
Dort sind dann auch die Links dahin gelistet.

* lesen und verstehen Sie alle folgende Regeln!

REGELN:

* Identität: Bitte haben Sie Ihren Studierendenausweis und
ein Foto-ID Griff bereit, damit wir Ihre Identität wie in
einer vor-Ort Klausur überprüfen können.

* Klausur: Zu Beginn der Zoom-Session schicken wir Ihnen
einen Link zur PDF Datei der Klausur sowie einen Link auf
einen Sciebo Ordner, wo Sie am Ende Ihre handgeschriebene
Klausur hochladen können.

* Quellen: "open book", Bücher, Ihre Notizen, die Folien
zur Vorlesung und auch andere Quellen im Internet sind
erlaubt. Jedoch dürfen Sie nicht mit anderen Leuten
kommunizieren!

* Kommunikation: Sie dürfen nur mit uns und auf gar keinen
Fall mit anderen kommunizieren. Wenn Sie gegen diese Regel
verstoßen, sind Sie direkt durchgefallen und können an der
HHU auch keine weitere Online Klausur mehr schreiben. 
Während der Klausur können Sie uns per Zoom Chat (Chat to
Host) oder per Mikrophone (für alle hörbar) Fragen
stellen. Falls nichts anderes klappt, schicken Sie uns
bitte eine Email (siehe unten).

* Videokonferenz: Während der ganzen Klausur sind Sie mit
uns in einer Zoom Konferenz. Nach Einwählen sind Sie
zunächst in einem Wartezimmer und werden dann
hereingelassen, sofern der gewählte Name auf unserer Liste
der angemeldeten Studierenden steht. Sie müssen Ihre
Kamera und Ihren Lautsprecher einschalten, und Ihr Mikrofon
aus.

* Bei Problemen: Falls Ihre Internetverbindung unterbrochen
wird, versuchen Sie umgehend, die Verbindung wieder ans
Laufen zu bringen. Falls Sie länger als fünf Minuten
nicht mehr in der Zoom Session sind, ist für Sie die
Klausur vorbei und Sie müssen beim nächsten Mal
mitschreiben. Die Teilnahme an der Videokonferenz mit
Kamera ist Voraussetzung für die Teilnahme an der Klausur. 
Dennoch, falls Sie wegen technischer Probleme nicht mehr
weiterschreiben können, zählt das diesmal nicht als
Fehlversuch.

* Abgabe: Die Klausur wird handschriftlich auf Papier
geschrieben. Am Ende bekommen Sie extra Zeit, um Ihre
Notizen einzuscannen (mit Computer oder Handy, probieren Sie
das vorher einmal aus!) und dann in einen Sciebo Ordner
hochzuladen. Der Dateiname muss Ihre Unikennung sein, d.h.
"<unikennung>.pdf".

* Falls nichts mehr klappt, senden Sie uns bitte einen Email
(<prof-email>, <tutor-emails>).

Wir hoffen, dass uns allen und auch Ihnen die Klausur
gelingt!

Mit freundlichen Grüßen
```

## Instructions of the first page of the exam

Lesen Sie die folgenden Regeln bitte aufmerksam durch:

* Erlaubte Hilfsmittel: Folien, Bücher, Notizen, Übungsaufgaben, auch
  Internetsuche.
* Jede Form von Kommunikation mit anderen (außer mit uns) führt zum
  sofortigen Nicht-Bestehen der Klausur.
* Bleiben Sie während der ganzen Klausur in der Zoom-Konferenz. Lassen
  Sie immer ihre Webcam eingeschaltet, so dass wir Ihr Gesicht sehen
  können, und stellen Sie Ihr Mikro auf stumm.  Wir empfehlen die
  Lautsprecher eingeschaltet zu lassen, damit Sie eventuelle Ansagen
  mitbekommen.
* Nach der Bearbeitung:
  - Scannen Sie bitte Ihre handgeschriebenen Lösungen mit einer
    Scanner-App (wir empfehlen Notes für iOS bzw. Simple Scan für
    Android, zur Not auch per Scanner), und erzeugen sie eine einzige
    mehrseitige PDF-Datei.
  - Erzeugen Sie einen Ordner mit Ihrer Unikennung als Name und
    kopieren Sie die PDF-Datei hinein.
  - Komprimieren Sie den Ordner zu einem ZIP-Archiv, welches Sie über
    den sciebo-Link hochladen. Den entsprechenden Link finden Sie im
    Chat Ihrer Zoom-Session. Achten Sie bitte darauf, dass Ihre Abgabe
    insgesamt nicht größer als 30MB ist.
* Der Name Ihrer ZIP-Datei muss Ihre Unikennung sein,
  z.B. `<unikennung>.zip`. Bitte achten Sie genau darauf, dass sie
  sich an dieses Namensschema halten und verwenden Sie keine anderen
  Formate als ZIP, da wir ansonsten Ihre Abgabe nicht korrigieren
  können.
* Abgaben per Tablet sind aus Gründen der Fairness nicht erlaubt.
* Bei Fragen wenden Sie sich bitte an den Host der Ihnen zugeteilten
  Zoom-Session. Falls Sie technische Schwierigkeiten haben,
  benachrichtigen Sie Ihren Host umgehend per E-Mail <prof-email>,
  <tutor-email>
* Alternativ können Sie jederzeit Ihr Mikro benutzen, um Ihre Frage
  öffentlich zu stellen.
* Technische Störungen, die länger als 5 Minuten dauern, führen zum
  Abbruch der Klausur. In diesem Fall wird Ihnen aber kein Fehlversuch
  angerechnet.
* Alle Aufgaben beziehen sich auf die in der Vorlesung vorgestellte
  Java-Version 8. Programmcode muss in Java geschrieben werden.
* Viel Erfolg!

## Scripts to check whether all are corrected

The following script checks whether all files are corrected
```
#!/usr/bin/python3
from sys import argv
from os import walk
from os.path import isfile, join
all  = next(walk('.'))[1]    # get list of all directory in '.'
lall = len(all)

def usage():
    print('USAGE')
    print('kstat.py      # summary')
    print('kstat.py 2    # show folders with missing 2')
    print('kstat.py 2 4  # show folders with missing 2 or 4')
    exit(0)

argv = argv[1:]
argc = len(argv)
if argc == 0:
    # show all summary for all
    argv = [str(i) for i in range(1,9)]
else:
    if argv[0] == '-h':
        usage()
showmissing = argc>0
d = 0  # global counter
for e in argv:
    c = 0   # counter
    
    for user in all:
        fname = join(user, user + '-e%s.txt'%e)
        if (isfile(fname)):
            c += 1
        else:
            if showmissing:
                print(user)
    if not(showmissing):
        print('exercise %s done: %3d / %3d  %3.0f%%' % (e, c, lall, 100*c/lall))
    d += c
# overall summary
print('--------------------------------')
print('ALL done:       %3d /%3d  %3.0f%%' % (d, len(argv)*lall, 100*d/(len(argv)*lall)))
```

## The following scripts (written by students) automatically sends out emails after correction
However, the ZIM allows only 20 emails per minute, so we wait after each email for four seconds.
```
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
```
