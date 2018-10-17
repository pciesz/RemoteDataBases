# Uniwersalna aplikacja przechowująca dane klienta, umożliwiająca ich udostępnianie klientom.

## Opis pomysłu

Celem projektu jest stworzenie aplikacji internetowej która będzie pozwalała na udostępnianie oraz pobieranie danych z bazy (Remote File System), co pozwoli firmom przechowywać pewne informacje w bezpiecznym zamkniiętym systemie.
Dostęp będzie przyznawany według potrzeb klienta (odbiorcy), będzie miał opcje udostępniać różne pliki - w wypadku tego zadania celem będą faktury, dostępne do pobrania, przypisane do klientów (jeden klient będzie miał dostęp do swoich danych po logowaniu, gdzie dostęp do logowania jest przyznawany od górnie - o tym niżej).
W projekcie będziemy chcieli zrealizować dostęp do serwera, poprzez webow interfejs (strona internetowa) oraz systemu plików powiązanych linkiem do systemu plików.

## Przewidywane technologie

Po stornie serwera:
- Django 
- Linux x86_64
- PostgreSQL

Po stornie klienta:
- HTML
- CSS 

Technologie opcjonalne:
- RESt api
- JSON impl.

## Motywacja

Projekt jest prosty w założeniach, ponieważ ma być jak najbardziej uniewrsalny - czyli kazdy klient będzie mógł zamówić własne udogodnienia do strony (rejestracja, forum, etc.). Dzieki temu nie tyle klient zostanie zalany ilością opcji, a dostanie zalew możliwości, które może wykorzystać na swojej stronie.
Dzięki temu klient dostanie wmiare tani produkt bazowy, a dodatkowe funkcjonalności będzie mógł dokupić (w dowolnym momecnie), a my będziemy mieli dobrą bazę do rozbudowy aplikajci, za sensowną ilość pieniedzy

## Potencjalne porblemy przy wdrażaniu

- Brak


## Analiza SWOT

Strenghts
- Prosta implementacja
- Solidna baza do dalszego rozwoju
- Łatwe do zrozumienia, noew osoby będą mogły równolegle realizować inne projekty
- Popularne technologie
- Wysoki zarobek na godzinie pracy
- Łatwa testowalność
- Nie wymaga specjalnego sprzętu
- Niewielki koszt wykonania

Weaknesses

- Nastąpi rozrost gałęzi - Każda sprzedaż to osobny produkt.
- Brak doświadczenia w web dev'ie
- Brak funduszy

Opportunities

- Tani produkt
- Szybka dostępność
- Błyskawiczny czas działania (prostota == prędkość)
- Możliwość customizacji
- Proste tanie aplikacje, są preferowane na rynku
- Nie ma żadnych zagrożeń ze strony prawa - nie łamiemy żadnych praw
- Ciągłość zlecenia

Threats

- Nasycony rynek
- Wyspecjalizowana funkcjonlaność
- Klient może sam zrobić sobie krzywdę, udostępniając ważne dane złej osobie
- Ciągły support aplikacji