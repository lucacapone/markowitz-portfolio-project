# Slide 1 – Titolo

## Costruzione di portafogli efficienti mediante il modello media-varianza di Markowitz

### Corso di Finanza

Progetto finale

Studente: Luca Capone

Anno Accademico 2025/2026

---

# Slide 2 – Obiettivo del progetto

## Obiettivo

Applicare il modello media-varianza di Markowitz utilizzando dati reali di mercato per:

* analizzare rischio e rendimento di un insieme di titoli azionari;
* studiare le relazioni tra gli asset;
* evidenziare i benefici della diversificazione;
* individuare portafogli efficienti.

## Titoli analizzati

* Apple (AAPL)
* JPMorgan Chase (JPM)
* Coca-Cola (KO)
* Johnson & Johnson (JNJ)
* Exxon Mobil (XOM)
* Boeing (BA)

---

# Slide 3 – Richiami teorici

## Concetti principali

* Rendimento atteso
* Rischio (varianza e volatilità)
* Diversificazione
* Frontiera efficiente
* Modello di Markowitz

### Rendimento atteso del portafoglio

E(Rp) = Σ wi E(Ri)

### Varianza del portafoglio

σ²p = wᵀΣw

### Vincolo sui pesi

Σ wi = 1

---

# Slide 4 – Raccolta dati

## Dataset

Fonte dati:

Yahoo Finance

Caratteristiche:

* Frequenza giornaliera
* Orizzonte temporale: ultimi 5 anni
* Prezzi Adjusted Close
* Rendimenti logaritmici

### Formula utilizzata

rt = ln(Pt / Pt−1)

## Settori rappresentati

* Technology
* Financials
* Consumer Defensive
* Healthcare
* Energy
* Industrials

---

# Slide 5 – Analisi descrittiva

## Principali risultati

| Titolo | Rendimento medio | Volatilità |
| ------ | ---------------- | ---------- |
| AAPL   | 0.000660         | 0.017270   |
| JPM    | 0.000667         | 0.015392   |
| KO     | 0.000429         | 0.010202   |
| JNJ    | 0.000412         | 0.010623   |
| XOM    | 0.000834         | 0.016891   |
| BA     | -0.000090        | 0.023065   |

### Osservazioni

* Exxon Mobil presenta il rendimento medio più elevato.
* Boeing presenta rendimento medio negativo.
* Coca-Cola e Johnson & Johnson risultano i titoli meno volatili.

![Prezzi normalizzati](../figures/normalized_prices.png)

*Figura. Andamento dei prezzi normalizzati dei titoli analizzati.*

---

# Slide 6 – Analisi delle correlazioni

## Matrice di correlazione

Principali evidenze:

* Correlazione massima:
  KO – JNJ = 0.451

* Correlazione minima:
  JNJ – BA = 0.073

## Interpretazione

Le correlazioni risultano positive ma moderate.

Nessuna coppia di titoli presenta correlazioni prossime all’unità.

⇒ Benefici significativi di diversificazione.

![Heatmap delle correlazioni](../figures/correlation_heatmap.png)

*Figura. Heatmap della matrice di correlazione dei rendimenti.*

---

# Slide 7 – Applicazione del modello di Markowitz

## Metodologia

1. Calcolo dei rendimenti medi storici
2. Stima della matrice di covarianza
3. Simulazione di 10.000 portafogli casuali
4. Calcolo di:

   * rendimento atteso
   * volatilità
   * Sharpe Ratio
5. Costruzione della frontiera efficiente

## Vincoli

* Somma dei pesi pari a 1
* No short selling
* Pesi compresi tra 0 e 1

---

# Slide 8 – Portafogli ottimali

| Portafoglio     | Rendimento | Volatilità | Sharpe Ratio |
| --------------- | ---------- | ---------- | ------------ |
| Minima varianza | 11.83%     | 12.75%     | 0.928        |
| Massimo Sharpe  | 15.28%     | 14.00%     | 1.092        |

## Interpretazione

Portafoglio a minima varianza:

* forte presenza di KO e JNJ

Portafoglio a massimo Sharpe:

* maggiore peso di XOM
* Boeing quasi esclusa

---

# Slide 9 – Frontiera efficiente

## Risultati dell’ottimizzazione

La frontiera efficiente rappresenta l’insieme dei portafogli che:

* massimizzano il rendimento per ogni livello di rischio;
* minimizzano il rischio per ogni livello di rendimento.

## Evidenze

* chiaro trade-off rischio/rendimento;
* benefici concreti della diversificazione;
* presenza di portafogli efficienti superiori alle combinazioni casuali.

![Frontiera efficiente](../figures/efficient_frontier.png)

*Figura. Frontiera efficiente nel piano rischio-rendimento.*

---

# Slide 10 – Conclusioni

## Conclusioni principali

* La diversificazione riduce il rischio complessivo del portafoglio.
* Il modello di Markowitz consente di individuare portafogli efficienti.
* I risultati mostrano vantaggi rispetto all’investimento in singoli titoli.
* Il portafoglio a massimo Sharpe offre il miglior compromesso rischio-rendimento.

## Possibili sviluppi futuri

* Estensione al CAPM
* Diversificazione internazionale
* Introduzione di ETF settoriali

# Grazie per l’attenzione
