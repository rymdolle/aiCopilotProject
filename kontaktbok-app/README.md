# Kontaktbok App

## Beskrivning
Detta projekt är en kontaktbokapplikation som låter användare lägga till, spara och söka efter kontakter. Kontakter kan innehålla multipla e-postadresser och telefonnummer. Applikationen använder SQLite som databasback-end och erbjuder en användarvänlig gränssnitt.

## Projektstruktur
```
kontaktbok-app
├── src
│   ├── main.py
│   ├── models
│   │   └── contact.py
│   ├── controllers
│   │   └── contact_controller.py
│   ├── views
│       └── contact_view.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation
1. Klona detta repository:
   ```
   git clone <repository-url>
   ```
2. Navigera till projektmappen:
   ```
   cd kontaktbok-app
   ```
3. Installera nödvändiga beroenden:
   ```
   pip install -r requirements.txt
   ```

## Användning
1. Starta applikationen:
   ```
   python src/main.py
   ```
2. Följ instruktionerna i användargränssnittet för att lägga till, söka eller ta bort kontakter.

## Bidrag
Bidrag är välkomna! Vänligen skapa en ny gren för dina ändringar och skicka en pull request.

## Licens
Detta projekt är licensierat under MIT-licensen. Se LICENSE-filen för mer information.