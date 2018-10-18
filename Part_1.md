# Uniwersalna aplikacja przechowująca dane klienta, umożliwiająca ich udostępnianie użytkownikom systemu.

## Opis pomysłu

Celem projektu jest stworzenie aplikacji internetowej która będzie pozwalała na udostępnianie oraz pobieranie danych z bazy (Remote File System), co pozwoli firmom przechowywać pewne informacje w bezpiecznym zamkniętym systemie.
Dostęp będzie przyznawany według potrzeb klienta (odbiorcy produktu). Pracownicy klienta będą mieli opcje udostępniania różnych plików - w wypadku tego zadania celem będą faktury, dostępne do pobrania, przypisane do klientów (naszego klienta). Dostęp do własnych danych użytkownik będzie miał po zalogowaniu do systemu.
W projekcie będziemy chcieli zrealizować dostęp do serwera, poprzez webowy interfejs (strona internetowa) oraz systemu zarządzania plikami, powiązanych linkiem do systemu plików.

## Przewidywane technologie
Po stronie serwera:

- Django
- Linux x86_64
- PostgreSQL

Po stornie klienta:

- HTML
- CSS

Technologie opcjonalne:

- REST api
- JSON impl.

## Motywacja

Projekt jest prosty w założeniach, aby mógł być jak najbardziej uniwersalny - kazdy klient będzie mógł zamówić własne udogodnienia do strony (forma rejestracji, forum, obsługa zgłoszeń, etc.). Dzieki temu nie tyle klient zostanie zalany ilością opcji, a dostanie zalew możliwości, które może wykorzystać na swojej stronie.
Dzięki temu klient dostanie tani, łatwo konfigurowalny produkt bazowy, a dodatkowe funkcjonalności będzie mógł dokupić (w dowolnym momencie), a my będziemy mieli dobrą bazę do rozbudowy aplikacji, możliwie małym kosztem.

## Potencjalne problemy przy wdrażaniu

- Potencjalna możliwość zmniejszenia elasteczności aplikacji przez dostosowanie podstawowego produktu do określonej kunkcjonalności (w tym przypadku obsługa faktur)

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
- Błyskawiczny czas działania
- Możliwość customizacji
- Proste tanie aplikacje są preferowane na rynku
- Nie ma żadnych zagrożeń ze strony prawa - nie łamiemy żadnych praw
- Ciągłość zlecenia

Threats

- Nasycony rynek
- Wyspecjalizowana funkcjonalność
- Klient może sam zrobić sobie krzywdę, udostępniając ważne dane złej osobie
- Ciągły support aplikacji

## Harmonogram prac
- 18.10.2018 - Przygotowanie i uzasadnienie potrzeby realizacji. Analiza problemu.
- 29.10.2018 - Faza projektowa
- 15.11.2018 - Implementacja i walidacja, „wdrożenie u klienta”, czyli w pracowni komputerowej.
- 29.11.2018 - Prezentacja na forum publicznym i zaliczenie całości.

## Kosztorys

Rzeczywisty koszt realizowanego projektu, przy nieuwzględnieniu poświęconego na niego czasu, będzie zerowy. Przy realnym wdrożeniu należy uwzględnić czas poświęcony na implementację produktu, koszty związane z obsługą klienta oraz zakup/utrzymanie serwera. 

