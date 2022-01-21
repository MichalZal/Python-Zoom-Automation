from re import match
from pywinauto import Application
import time
import pyautogui

aktywne = True
#ipsoktania = input("Podaj id sptokania: ")
#imie = input("Podaj imie: ")

#while aktywne:


zoom_okno = Application(backend='uia').start(r"C:\Users\User\AppData\Roaming\Zoom\bin\Zoom.exe").connect(title="Zoom",timeout=10)
#zoomWin.Zoom.print_control_identifiers()

#zakładka dom
homeTab = zoom_okno.Zoom.child_window(title='Dom', control_type="TabItem").wrapper_object()
homeTab.click_input()

#przycisk dołącz
joinBtn = zoom_okno.Zoom.child_window(title='Dołącz', control_type="Button").wrapper_object()
joinBtn.click_input()

#Nowe okno = Dołącz do spotkania
joinWindow = Application(backend='uia').connect(title='Dołącz do spotkania', timeout=10)

#joinWindow.Dołączdospotkania.print_control_identifiers()
#podawanie id spotkania
poleID = joinWindow.Dołączdospotkania.child_window(title="Wprowadź identyfikator spotkania lub nazwę osobistego linku", control_type="Edit").wrapper_object()
poleID.type_keys("556 461 0917")

#wpisywanie imienia
poleImie = joinWindow.Dołączdospotkania.child_window(title="Wprowadź nazwę", control_type="Edit").wrapper_object()
poleImie.click_input()
poleImie.type_keys("^a{BACKSPACE}")
poleImie.type_keys("Michał Zalewski", with_spaces=True)

#klikanie dołąćz
przycisk_dołącz = joinWindow.Dołączdospotkania.child_window(title="Dołącz", control_type="Button")
przycisk_dołącz.click_input()

#Wporwadzanie hasła = Wporowadź kod spotkania
codewindow = Application(backend='uia').connect(title="Wprowadź kod spotkania", timeout=10)
#Codewindow.Wpiszkodspotkania.print_control_identifiers()
kod = codewindow.Wprowadźkodspotkania.child_window(title="Wprowadź kod dostępu do spotkania", control_type="Edit")
kod.click_input()
kod.type_keys("123")
dolacz_kod = codewindow.Wprowadźkodspotkania.child_window(title="Dołącz do spotkania", control_type="Button")
dolacz_kod.click_input()

time.sleep(10) #30 sekund kiedy do spotkania prawdziwego dołąćzacie

#====================================================================================================================

Spotkanie = Application(backend='uia').connect(title='Zoom Spotkanie', timeout=10)
Spotkanie.Zoomspotkanie.click_input()
Spotkanie.ZoomSpotkanie.print_control_identifiers()


def udostepnij_ekran_z_dziwekiem():
    # #Okno spotkania
    Spotkanie = Application(backend='uia').connect(title='Zoom Spotkanie', timeout=10)
    Spotkanie.Zoomspotkanie.click_input()
    #Spotkanie.ZoomSpotkanie.print_control_identifiers()


    udostepnij_ekran = Spotkanie.ZoomSpotkanie.child_window(title='Udostępnij ekran, Alt+S').wrapper_object()
    udostepnij_ekran.click_input()

    udostepnij_ekran_okno = Application(backend='uia').connect(title='Wybierz okno lub aplikację, którą chcesz udostępnić', timeout=5)
    #udostepnij_ekran_okno.Wybierzoknolubaplikacjęktórąchceszudostępnić.print_control_identifiers()

    z_dwiekiem = udostepnij_ekran_okno.Wybierzoknolubaplikacjęktórąchceszudostępnić.child_window(title="Udostępnij dźwięk", control_type="CheckBox")
    z_dwiekiem.click_input()

    udostepnij_ekran_przycisk = udostepnij_ekran_okno.Wybierzoknolubaplikacjęktórąchceszudostępnić.child_window(title='Udostępnij Ekran')
    udostepnij_ekran_przycisk.click_input()



def udostepnij_ekran_bez_dzwieku():
    # #Okno spotkania
    Spotkanie = Application(backend='uia').connect(title='Zoom Spotkanie', timeout=10)
    Spotkanie.Zoomspotkanie.click_input()
    #Spotkanie.ZoomSpotkanie.print_control_identifiers()


    udostepnij_ekran = Spotkanie.ZoomSpotkanie.child_window(title='Udostępnij ekran, Alt+S').wrapper_object()
    udostepnij_ekran.click_input()

    udostepnij_ekran_okno = Application(backend='uia').connect(title='Wybierz okno lub aplikację, którą chcesz udostępnić', timeout=5)
    #udostepnij_ekran_okno.Wybierzoknolubaplikacjęktórąchceszudostępnić.print_control_identifiers()

    udostepnij_ekran_przycisk = udostepnij_ekran_okno.Wybierzoknolubaplikacjęktórąchceszudostępnić.child_window(title='Udostępnij Ekran')
    udostepnij_ekran_przycisk.click_input()

def wycisz_wszystkich_z_mozliwoscia_odciszenia():
    # #Okno spotkania
    Spotkanie = Application(backend='uia').connect(title='Zoom Spotkanie', timeout=10)
    Spotkanie.Zoomspotkanie.click_input()
      
    uczestnicy = Spotkanie.ZoomSpotkanie.child_window(title="Zamknięto, otwórz panel z uczestnikami, uczestników: 2, Alt+U", control_type="Button")
    uczestnicy.click_input()

def wycisz_wszystkich_bez_mozliwosci_odciszenia():
    # #Okno spotkania
    Spotkanie = Application(backend='uia').connect(title='Zoom Spotkanie', timeout=10)
    Spotkanie.Zoomspotkanie.click_input()

    uczestnicy = Spotkanie.ZoomSpotkanie.child_window(title="Zamknięto, otwórz panel z uczestnikami, uczestników: 2, Alt+U", control_type="Button")
    uczestnicy.click_input()

def podziel_na_pokoje_automatycznie():
    pass



okej = True
while okej:
    dzialanie = input(
        "Co chcesz zrobic?: \n"
        "1.udostepnij ekran z dziwekiem \n"
        "2.udostepnij ekran bez dzwieku \n"
        "3.Wycisz wszystkich z możliwością odciszenia \n"
        "4.Wycisz wszystkich bez możliwości odciszenia \n"
        "Wybieraj: "
        )

    if dzialanie == '1':
        udostepnij_ekran_z_dziwekiem()
    elif dzialanie == '2':
        udostepnij_ekran_bez_dzwieku()
    elif dzialanie == '3':
        wycisz_wszystkich_z_mozliwoscia_odciszenia()
    elif dzialanie == '5':
        okej = False