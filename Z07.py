import csv

def quiz_from_file(filename):
    try:
        # Wczytywanie pytań i odpowiedzi z pliku CSV
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            questions = [row for row in reader]

        correct_answers = 0
        print("Rozpoczynamy quiz! Odpowiadaj 'tak' lub 'nie', wpisz 'skip', aby pominąć pytanie, lub 'exit', aby zakończyć quiz.")

        for question, correct_answer in questions:
            while True:
                user_input = input(f"{question} (tak/nie): ").strip().lower()

                match user_input:
                    case 'exit':
                        print("Kończymy quiz!")
                        print(f"Liczba poprawnych odpowiedzi: {correct_answers}")
                        return
                    case 'skip':
                        print("Pytanie pominięte.")
                        break
                    case 'tak' | 'nie':
                        if user_input == correct_answer:
                            print("Poprawna odpowiedź!")
                            correct_answers += 1
                        else:
                            print("Niepoprawna odpowiedź.")
                        break
                    case _:
                        print("Niepoprawny wybór, spróbuj ponownie.")

        print("Quiz zakończony!")
        print(f"Liczba poprawnych odpowiedzi: {correct_answers}")

    except FileNotFoundError:
        print(f"Plik {filename} nie został znaleziony.")
    except Exception as e:
        print(f"Wystąpił błąd: {e}")

# Uruchomienie quizu z pliku questions.csv
quiz_from_file('questions.csv')
