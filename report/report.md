# 1. Introduzione

La costruzione di portafoglio costituisce un problema centrale nella finanza, poiché gli investitori raramente valutano i titoli in modo isolato. Essi allocano invece il capitale tra più attività finanziarie al fine di perseguire un obiettivo di investimento, controllando al contempo l'esposizione all'incertezza. Un portafoglio correttamente strutturato offre un criterio sistematico per determinare la quota di ricchezza da destinare a ciascuna attività, evitando di fondare la decisione esclusivamente sulle caratteristiche dei singoli titoli o su valutazioni informali.

Un aspetto essenziale della scelta di portafoglio è il trade-off tra rischio e rendimento. In generale, gli investitori richiedono rendimenti attesi più elevati come compensazione per l'assunzione di una maggiore incertezza sui risultati futuri. Le attività più rischiose possono offrire opportunità di guadagno superiori, ma espongono anche a perdite potenziali più ampie e a una maggiore volatilità della performance. L'analisi di portafoglio richiede pertanto sia una stima del rendimento atteso sia una misura del rischio, così da consentire un confronto coerente tra allocazioni alternative.

La diversificazione svolge un ruolo rilevante nella gestione di tale relazione. Combinando attività i cui rendimenti non si muovono in perfetta sincronia, l'investitore può ridurre il rischio complessivo del portafoglio senza necessariamente diminuire il rendimento atteso nella stessa proporzione. Il beneficio della diversificazione dipende non solo dalla rischiosità delle singole attività, ma anche dalla covarianza e dalla correlazione tra i loro rendimenti. Di conseguenza, la costruzione di portafoglio deve considerare sia le interazioni tra i titoli sia le rispettive prospettive di rendimento atteso.

L'obiettivo di questo progetto è analizzare sei azioni appartenenti a settori differenti e costruire portafogli efficienti mediante il modello media-varianza di Markowitz. Il lavoro applica la teoria di portafoglio a un insieme diversificato di titoli azionari, stima le caratteristiche di rendimento e rischio sulla base di dati storici e fornisce il fondamento teorico per individuare portafogli che presentino combinazioni efficienti di rendimento atteso e rischio.

# 2. Fondamenti teorici

Gli investimenti rischiosi sono attività i cui rendimenti futuri risultano incerti. Le azioni ordinarie sono rischiose perché prezzi e dividendi possono variare in risposta a fattori specifici dell'impresa, condizioni settoriali, variabili macroeconomiche, tassi di interesse, aspettative degli investitori e dinamiche generali di mercato. Poiché il payoff futuro non è noto con certezza, gli investitori devono valutare sia la remunerazione attesa derivante dal possesso dell'attività sia la variabilità dei possibili risultati rispetto a tale aspettativa.

La relazione tra rischio e rendimento rappresenta uno dei principi fondamentali delle decisioni finanziarie. Gli investitori si attendono generalmente rendimenti più elevati quando sopportano livelli di rischio maggiori. Tuttavia, un rischio più alto non garantisce rendimenti realizzati superiori; esso indica soltanto una maggiore incertezza e un intervallo più ampio di esiti possibili. Per questa ragione, l'analisi di portafoglio distingue tra rendimento atteso, che esprime il risultato medio previsto, e rischio, comunemente misurato tramite la varianza o la deviazione standard dei rendimenti.

L'avversione al rischio descrive la preferenza della maggior parte degli investitori a evitare rischi non necessari. Un investitore avverso al rischio sceglierà, tra due investimenti con lo stesso rendimento atteso, quello meno rischioso. Al contrario, accetterà un rischio aggiuntivo solo se il rendimento atteso risulterà sufficientemente più elevato da compensarlo. Questa ipotesi è centrale nell'analisi media-varianza, poiché spiega perché gli investitori ricercano portafogli che minimizzino il rischio per un dato rendimento atteso oppure massimizzino il rendimento atteso per un dato livello di rischio.

L'analisi media-varianza valuta i portafogli mediante due grandezze principali: rendimento atteso e varianza. Il rendimento atteso rappresenta il rendimento medio che l'investitore prevede di ottenere dal portafoglio, mentre la varianza misura la dispersione dei rendimenti attorno a tale valore atteso. In questo quadro, l'investitore confronta i portafogli in base al rendimento atteso e al rischio, assumendo che tali dimensioni sintetizzino in modo efficace la performance dell'investimento.

La diversificazione consiste nell'allocare la ricchezza tra più attività, anziché concentrare l'intero investimento in un solo titolo. Il suo obiettivo è ridurre l'esposizione al rischio specifico delle singole attività. Quando le attività non sono perfettamente correlate positivamente, perdite o rendimenti deboli di un titolo possono essere parzialmente compensati da risultati migliori di un altro. Pertanto, il rischio di un portafoglio diversificato dipende sia dalla volatilità delle singole attività sia dalle relazioni tra i loro rendimenti.

Il rendimento atteso di un portafoglio è la media ponderata dei rendimenti attesi delle attività incluse nel portafoglio. Se un portafoglio contiene \(n\) attività, dove \(w_i\) è il peso assegnato all'attività \(i\) ed \(E(R_i)\) è il rendimento atteso dell'attività \(i\), il rendimento atteso del portafoglio è:

$$
E(R_p) = \sum_{i=1}^{n} w_i E(R_i)
$$

La varianza di portafoglio misura il rischio del portafoglio complessivo. A differenza del rendimento atteso, essa non corrisponde soltanto a una media ponderata delle varianze delle singole attività, ma dipende anche dalle covarianze tra i rendimenti. La covarianza misura la tendenza di due attività a muoversi congiuntamente. Una covarianza positiva indica che le attività tendono spesso a muoversi nella stessa direzione, mentre una covarianza negativa segnala movimenti frequentemente opposti. Una covarianza più bassa tra attività accresce il potenziale beneficio della diversificazione.

Utilizzando la notazione matriciale, la varianza di portafoglio può essere espressa come:

$$
\sigma_p^2 = w^T \Sigma w
$$

dove \(w\) è il vettore dei pesi di portafoglio e \(\Sigma\) è la matrice di covarianza dei rendimenti delle attività. Tale espressione evidenzia che il rischio di portafoglio dipende dall'intera struttura di covarianza delle attività, e non soltanto dal rischio di ciascun titolo considerato separatamente.

In un portafoglio interamente investito, la somma dei pesi deve essere pari a uno. Questa condizione assicura che tutto il capitale disponibile sia allocato tra le attività selezionate:

$$
\sum_{i=1}^{n} w_i = 1
$$

La frontiera efficiente è l'insieme dei portafogli che offrono il rendimento atteso più elevato per ciascun livello di rischio oppure, in modo equivalente, il rischio più basso per ciascun livello di rendimento atteso. I portafogli collocati al di sotto della frontiera efficiente sono inefficienti, poiché esiste un altro portafoglio ammissibile che offre un rendimento atteso maggiore a parità di rischio oppure un rischio inferiore a parità di rendimento atteso. La frontiera efficiente costituisce quindi una rappresentazione visiva e analitica delle migliori combinazioni rischio-rendimento ottenibili dato un insieme di attività.

La teoria di portafoglio di Markowitz, sviluppata da Harry Markowitz, formalizza la selezione di portafoglio attraverso il paradigma media-varianza. Essa sottolinea che gli investitori non dovrebbero selezionare le attività esclusivamente sulla base dei rendimenti attesi o dei rischi individuali. Al contrario, dovrebbero valutare il modo in cui le attività interagiscono all'interno del portafoglio tramite la covarianza. Combinando rendimenti attesi, varianze, covarianze e vincoli sui pesi di portafoglio, il modello di Markowitz individua portafogli efficienti e fornisce una base rigorosa per la moderna costruzione di portafoglio.
