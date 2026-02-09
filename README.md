# Projekt: Sales Analyzer

Dieses Projekt analysiert Verkaufsdaten, berechnet wichtige Kennzahlen, erstellt Berichte und visualisiert die Ergebnisse. Es beinhaltet auch eigene Implementierungen von Sortier- und Suchalgorithmen und vergleicht deren Leistung mit den eingebauten Python- und NumPy-Funktionen.

## Funktionen

- **Datenmanagement**
  - Laden und Bereinigen von Verkaufsdaten (`sales_data.csv`)
  - Speichern der bereinigten Daten (`sales_clean.csv`)

- **Analyse**
  - Berechnung von Kennzahlen:
    - Gesamtumsatz
    - Durchschnittlicher Bestellwert
    - Anzahl der Kunden
    - Wiederholungskundenrate
    - Stornorate
  - Top-10 Kunden nach Bestellwert
  - Durchschnittlicher Bestellwert nach Produktkategorie

- **Visualisierung**
  - Umsatz nach Kategorie (Balkendiagramm)
  - Monatliche Umsatzentwicklung (Liniendiagramm)
  - Verteilung der Bestellwerte (Histogramm)

- **Leistungsvergleich**
  - Eigene Implementierung von Bubble Sort und Linear Search
  - Vergleich mit Python eingebauten Funktionen (`sorted()`, `in`) und NumPy

## Projektstruktur

Projekt/
├── data/ # Ursprungs- und bereinigte Daten
├── figures/ # Generierte Diagramme
├── output/ # CSV-Berichte und Textzusammenfassung
├── analyzer.py # SalesAnalyzer-Klasse
├── algorithms.py # Sortier- und Suchalgorithmen
├── main.py # Hauptskript
├── models.py # Datenklassen: Customer, Product, Order
└── utils.py # Hilfsfunktionen (z.B. Währungsformat, Datumsvalidierung)


## Installation

1. Erstelle ein virtuelles Environment:

```bash
python -m venv .venv
Aktiviere das Environment:

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate
Installiere die benötigten Pakete:

pip install -r requirements.txt
Nutzung
Führe das Projekt über die Kommandozeile aus:

python main.py
Alle Berichte werden im Ordner output/ gespeichert, Diagramme im Ordner figures/.