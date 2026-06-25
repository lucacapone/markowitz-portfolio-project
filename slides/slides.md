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
* Campione completo: 22/06/2021--22/06/2026
* Training: 22/06/2021--29/05/2026
* Test fuori campione: 01/06/2026--22/06/2026
* Prezzi Adjusted Close e rendimenti logaritmici

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
| AAPL   | 0.000703         | 0.017276   |
| JPM    | 0.000658         | 0.015378   |
| KO     | 0.000413         | 0.010108   |
| JNJ    | 0.000372         | 0.010613   |
| XOM    | 0.000813         | 0.016823   |
| BA     | -0.000043        | 0.023039   |

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
  JNJ – BA ≈ 0.071

## Interpretazione

Le correlazioni risultano positive ma moderate.

Nessuna coppia di titoli presenta correlazioni prossime all’unità.

I p-value sono quasi tutti < 0.001; JNJ–BA ha p-value = 0.012, quindi è significativa al 5% ma economicamente debole.

⇒ Benefici significativi di diversificazione.

![Heatmap delle correlazioni](../figures/correlation_heatmap.png)

*Figura. Heatmap della matrice di correlazione dei rendimenti.*

---

# Slide 7 – Matrice dei p-value formattati

## Significatività statistica delle correlazioni

|      | AAPL | JPM | KO | JNJ | XOM | BA |
|------|------|------|------|------|------|------|
| AAPL | <0.001 | <0.001 | <0.001 | <0.001 | <0.001 | <0.001 |
| JPM  | <0.001 | <0.001 | <0.001 | <0.001 | <0.001 | <0.001 |
| KO   | <0.001 | <0.001 | <0.001 | <0.001 | <0.001 | <0.001 |
| JNJ  | <0.001 | <0.001 | <0.001 | <0.001 | <0.001 | 0.012 |
| XOM  | <0.001 | <0.001 | <0.001 | <0.001 | <0.001 | <0.001 |
| BA   | <0.001 | <0.001 | <0.001 | 0.012 | <0.001 | <0.001 |

## Lettura della tabella

* Valori molto piccoli indicano evidenza contro H₀: ρ = 0.
* Tutte le correlazioni sono statisticamente significative al 5%.
* La coppia JNJ–BA resta economicamente debole nonostante la significatività.

---

# Slide 8 – Applicazione del modello di Markowitz

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

# Slide 9 – Portafogli ottimali

| Portafoglio     | Rendimento | Volatilità | Sharpe Ratio |
| --------------- | ---------- | ---------- | ------------ |
| Minima varianza | 11.38%     | 12.73%     | 0.894        |
| Massimo Sharpe  | 14.97%     | 14.00%     | 1.069        |

## Interpretazione

Portafoglio a minima varianza:

* forte presenza di KO e JNJ

Portafoglio a massimo Sharpe:

* maggiore peso di XOM
* Boeing quasi esclusa

---

# Slide 10 – Frontiera efficiente

## Risultati dell’ottimizzazione

La frontiera efficiente rappresenta l’insieme dei portafogli che:

* massimizzano il rendimento per ogni livello di rischio;
* minimizzano il rischio per ogni livello di rendimento.

## Evidenze

* chiaro trade-off rischio/rendimento;
* benefici concreti della diversificazione;
* linea orizzontale dal portafoglio a minima varianza;
* separazione visiva tra regione efficiente e inefficiente.

![Frontiera efficiente](../figures/efficient_frontier.png)

*Figura. Frontiera efficiente nel piano rischio-rendimento.*

---

# Slide 11 – Verifica fuori campione

## Ultimo mese escluso dalla stima

Periodo di test: 01/06/2026--22/06/2026<br>
Giorni di test: 14

| Portafoglio | Atteso mensile | Realizzato mensile |
| ----------- | -------------- | ------------------ |
| Minima varianza | 0.6341% | 0.4448% |
| Massimo Sharpe | 0.8350% | -0.2115% |

## Interpretazione

* Minima varianza: risultato leggermente inferiore alle attese, ma vicino.
* Massimo Sharpe: sottoperformance e rendimento realizzato negativo.
* L'ottimalità in-sample non garantisce performance fuori campione.

---

# Slide 12 – Conclusioni

## Conclusioni principali

* La diversificazione riduce il rischio complessivo del portafoglio.
* Il modello di Markowitz consente di individuare portafogli efficienti.
* Le correlazioni sono statisticamente significative, ma non sempre economicamente forti.
* Il test fuori campione rende la valutazione più realistica.
* Nell'ultimo mese il portafoglio a minima varianza è stato più stabile del massimo Sharpe.

## Possibili sviluppi futuri

* Estensione al CAPM
* Diversificazione internazionale
* Introduzione di ETF settoriali

# Grazie per l’attenzione
