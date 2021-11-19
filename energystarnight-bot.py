import sys
from lxml import html
import requests
import os
import time

rounds = 0
phoneNumber = os.environ["PHONE_NUMBER"]
print("using " + str(phoneNumber) + " as phone number")
questions = {
    "WIE ALT MUSS MAN SEIN, UM OHNE ERWACHSENE BEGLEITUNG AN DER ENERGY STAR NIGHT TEILZUNEHMEN?":"14",
    "WELCHER ACT WAR NOCH NIE AN DER ENERGY STAR NIGHT DABEI?":"Loredana",
    "WIE HEISST DER OFFIZIELLE INSTAGRAM ACCOUNT DER ENERGY STAR NIGHT?":"@energystarnight",
    "WELCHE ZWEI ACTS LASEN AN DER ESN18 BACKSTAGE MEAN TWEETS?":"Olly Murs und James Arthur",
    "Wen hat Herr Bünzli an seiner ersten Energy Star Night 2017 interviewt?":"Anastacia & Mark Forster ",
    "N WELCHEM JAHR WURDE DAS ENERGY STARS FOR FREE ZUR ENERGY STAR NIGHT?":"2016",
    "WO FINDET DIE ENERGY STAR NIGHT STATT?":"Im Hallenstadion Zürich",
    "WAS WAR DAS BESONDERE AN DER ÜBERGABE DES ENERGY MUSIC AWARD 2020?":"Loco Escrito bekam ihn per Post nach Hause geschickt",
    "WIE HEISST DIE LUSTIGE ASSISTENTIN VON BUSTER MOON?":"Miss Crawly",
    "WELCHER YOUTUBE STAR JAMMTE BEIM ENERGY AIR 2017 2017 BACKSTAGE MIT SAMU VON SUNRISE AVENUE?":"Alex Aiono",
    "WAS FÜR EIN WORT MUSST DU PER SMS SCHICKEN, UM TICKETS ZU GEWINNEN?":"STAR",
    "WIE HEISST DIE FRAU VON HERR BÜNZLI?":"Anegret",
    "WELCHES DJ-DUO RIESS 2016 DAS HALLENSTADION AB?":"Remady & Manu L",
    "WER ÜBERZEUGT DEN GROSSEN STAR CLAY CALLOWAY, AN DER SHOW TEILZUNEHMEN?":"Ash",
    "WELCHER NIEDERLÄNDISCHE DJ TRAT 2016 BEI DER ENERGY STAR NIGHT AUF?":"Martin Garrix",
    "WELCHER ACT ERÖFFNETE DIE ENERGY STAR NIGHT 2019?":"Tom Gregory",
    "WELCHER ACT HAT AN EINER ENERGY STAR NIGHT BACKSTAGE EINEM FAN EIN TATTOO GESTOCHEN?":"Sido",
    "WER HAT DEN ERSTEN ENERGY MUSIC AWARD GEWONNEN?":"Manillio",
    "WANN FAND DER EVENT ZUM ERSTEN MAL STATT?":"2003",
    "WIE LAUTET DER OFFIZIELLE HASHTAG DER ENERGY STAR NIGHT?":"#ESN21",
    "WELCHER ACT WAR AM ERSTEN ENERGY STARS FOR FREE UND SCHON WEITERE SECHS MAL DABEI?":"Stress",
    "WANN BEGINNT DIE ENERGY STAR NIGHT?":"19:00",
    "WAS IST ENERGY ONE?":"Die Membership von Energy",
    "WANN WIRD DIE ENERGY STAR NIGHT STATTFINDEN?":"19. November 2021",
    "WELCHER U2-SONG WIRD IM TRAILER VON SING – DIE SHOW DEINES LEBENS GESPIELT?":"I Still Haven’t Found What I’m Looking For",
    "AN DER ENERGY STAR NIGHT 2019 HABEN WIR DAS GRÖSSTE TIKTOK-VIDEO MIT 13'000 LEUTEN GEMACHT. WAS FÜR EINE CHALLENGE WAR ES?":"MANNEQUINCHALLENGE",
    "WELCHER HERAUSFORDERUNG MUSS SICH ROSITA IN DER SHOW STELLEN?":"An einem Seil in die Tiefe springen",
    "WO FINDET DIE AFTERSHOW PARTY STATT?":"Kaufleuten",
    "WER SPRICHT DIE ROLLE VON ASH AUF DEUTSCH?":"Stefanie Kloss",
    "WAS FÜR EIN INSTRUMENT SPIELT ASH?":"E-Gitarre",
    "WO FINDET DIE NEUE MUSIK-SHOW STATT?":"Redshore City",
    "WER SPRICHT DIE ORIGINALSTIMME VON CLAY CALLOWAY?":"Bono",
    "WELCHER AWARD WIRD IM RAHMEN DER ENERGY STAR NIGHT VERLIEHEN?":"Der Energy Music Award",
    "SEIT WANN IST ENERGY LUZERN LIVE ON AIR?":"August 2021",
    "WIE VIELE BESUCHER MACHEN DIE ENERGY STAR NIGHT ZUM GRÖSSTEN INDOOR-MUSIK-EVENT DER SCHWEIZ?":"13'000"
    "WELCHER SCHWEIZER ACT HAT 2019 DEN ENERGY MUSIC AWARD GEWONNEN?":"Luca Hänni",
    "WIE HEISST DIE TOCHTER DES SHOW MANAGERS?":"Porsha",
    "WIE KOMMT MAN AN TICKETS FÜR DIE ENERGY STAR NIGHT?":"Gewinnen",
    "WAS WAR DAS THEMA DER LETZTEN ENERGY STAR NIGHT?":"WELCOME TO THE CANDY FACTORY"
}

def get_answer(question):
    answer = questions.get(question, 0)
    if answer == 0:
        return 1
    return answer

def next_question(antwort):
    data = {'question': antwort}
    q2 = session.post('https://game.energy.ch/', data)
    tree = html.fromstring(q2.content)
    frage = tree.xpath('//form[@class="question"]/h1/text()')[0]
    return frage

try:
    while True:
        try:
            rounds += 1
            session = requests.session()
            data = {'mobile': phoneNumber}
            q1 = session.post('https://game.energy.ch/', data)
            tree = html.fromstring(q1.content)

            frage = tree.xpath('//form[@class="question"]/h1/text()')[0]
            print("answering questions...")
            for i in range(9):
                time.sleep(0.5)
                antwort = get_answer(frage)
                frage = next_question(antwort)
            antwort = get_answer(frage)

            data = {'question': antwort}
            q2 = session.post('https://game.energy.ch/', data)
            print("all questions answered!")

            tree = html.fromstring(q2.content)
            verloren = tree.xpath('//div[@id="content"]/h2/text()')
            if verloren[0] == "Glückwunsch!":
                data = {'site': 'win'}
                q2 = session.post('https://game.energy.ch/', data)
                q2 = session.get('https://game.energy.ch/?ticket=10')
                tree = html.fromstring(q2.content)
                verloren = tree.xpath('//div[@id="wingame"]/h1/text()')
                if len(verloren) == 1:
                    if verloren[0] != "Das war das falsche Logo, knapp daneben! Versuche es erneut!":
                        f = open('win.txt', 'wb')
                        f.write(q2.content)
                        f.close()
                        print("code 5")
                        print("restart...")
                    else:
                        print("code 4")
                        print("restart...")
                else:
                    print("code 3")
                    print("restart...")
            else:
                print("code 2")
                print("restart...")

        except Exception:
            print("code 1")
            print("restart...")
            pass
finally:
    print("\n\n------see ya------")
    print("Rounds: " + str(rounds))
    print("------------------")
    sys.exit(0)
