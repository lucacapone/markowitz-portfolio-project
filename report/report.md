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

# 3. Raccolta dati

La base informativa utilizzata per l'analisi è costituita da dati storici di mercato provenienti da Yahoo Finance, una fonte ampiamente impiegata nelle applicazioni empiriche di finanza per l'accesso a serie temporali di prezzi azionari. I dati sono stati raccolti con frequenza giornaliera, in modo da osservare con sufficiente dettaglio la dinamica dei prezzi e dei rendimenti nel tempo. L'orizzonte temporale considerato copre un periodo di osservazione di cinque anni, scelta che consente di includere diverse condizioni di mercato e di ottenere un numero adeguato di osservazioni per le successive elaborazioni statistiche.

Il campione è composto da sei titoli azionari quotati sul mercato statunitense: Apple (AAPL), JPMorgan Chase (JPM), Coca-Cola (KO), Johnson & Johnson (JNJ), Exxon Mobil (XOM) e Boeing (BA). La selezione di tali società risponde all'esigenza di costruire un insieme di attività rappresentativo di settori economici differenti. Apple appartiene al comparto tecnologico, JPMorgan Chase al settore finanziario, Coca-Cola ai beni di consumo difensivi, Johnson & Johnson al settore sanitario, Exxon Mobil all'energia e Boeing all'industria aerospaziale e manifatturiera. Tale eterogeneità settoriale è rilevante perché riduce la concentrazione dell'analisi su un'unica area dell'economia e permette di valutare in modo più appropriato i potenziali benefici della diversificazione.

Per ciascun titolo sono stati utilizzati i prezzi di chiusura rettificati, indicati come *Adjusted Close*. Questa variabile incorpora gli effetti di eventi societari quali dividendi, frazionamenti azionari e altre rettifiche rilevanti, fornendo pertanto una misura più coerente del rendimento effettivamente conseguibile dall'investitore rispetto al semplice prezzo di chiusura non rettificato. L'impiego dei prezzi rettificati è particolarmente importante quando si analizzano serie storiche su un orizzonte pluriennale, poiché consente di evitare distorsioni nella misurazione della performance.

A partire dai prezzi rettificati sono stati calcolati i rendimenti logaritmici giornalieri. Se \(P_t\) rappresenta il prezzo rettificato del titolo al tempo \(t\) e \(P_{t-1}\) il prezzo rettificato nel giorno di negoziazione precedente, il rendimento logaritmico è definito come:

$$
r_t = \ln\left(\frac{P_t}{P_{t-1}}\right)
$$

I rendimenti logaritmici sono preferiti in molte applicazioni finanziarie perché risultano additivi nel tempo e facilitano l'aggregazione dei rendimenti su orizzonti temporali più lunghi. Inoltre, per variazioni di prezzo contenute, essi sono molto vicini ai rendimenti semplici, ma presentano proprietà analitiche più convenienti nell'ambito della modellizzazione statistica e dell'analisi di portafoglio.

# 4. Analisi descrittiva

L'analisi descrittiva costituisce una fase preliminare essenziale nello studio dei dati finanziari, poiché consente di sintetizzare le principali caratteristiche empiriche dei rendimenti prima dell'applicazione di modelli più strutturati di selezione di portafoglio. Le statistiche descrittive permettono di valutare il livello medio dei rendimenti, la dispersione attorno alla media, l'ampiezza degli estremi osservati e la forma della distribuzione. In questo modo è possibile individuare differenze rilevanti tra i titoli in termini di performance storica, volatilità e rischio di eventi estremi.

## 4.1 Statistiche descrittive dei rendimenti

| Titolo | Media | Deviazione Standard | Minimo | Massimo | Skewness | Kurtosis |
|---------|---------|---------|---------|---------|---------|---------|
| AAPL | 0.000660 | 0.017270 | -0.097013 | 0.142617 | 0.245127 | 5.901085 |
| JPM | 0.000667 | 0.015392 | -0.077787 | 0.109254 | -0.050387 | 4.633102 |
| KO | 0.000429 | 0.010202 | -0.072169 | 0.046168 | -0.235207 | 3.741206 |
| JNJ | 0.000412 | 0.010623 | -0.078953 | 0.060090 | -0.009126 | 4.947567 |
| XOM | 0.000834 | 0.016891 | -0.082136 | 0.062142 | -0.307373 | 1.428977 |
| BA | -0.000090 | 0.023065 | -0.110608 | 0.143010 | -0.132429 | 3.426757 |

Le statistiche riportate evidenziano una significativa eterogeneità tra i rendimenti giornalieri dei sei titoli. In termini di rendimento medio, Exxon Mobil presenta il valore più elevato, pari a 0.000834, segnalando la performance media giornaliera più favorevole nel campione considerato. Anche JPMorgan Chase e Apple mostrano rendimenti medi positivi e relativamente elevati, rispettivamente pari a 0.000667 e 0.000660. Coca-Cola e Johnson & Johnson registrano rendimenti medi più contenuti, ma comunque positivi, coerentemente con la natura più difensiva dei rispettivi settori. Boeing, al contrario, presenta un rendimento medio negativo, pari a -0.000090, indicando che nel periodo osservato il titolo ha avuto una performance media giornaliera inferiore rispetto agli altri strumenti analizzati.

La deviazione standard consente di confrontare il grado di volatilità dei rendimenti. Boeing risulta il titolo più volatile, con una deviazione standard pari a 0.023065, segnalando una maggiore instabilità dei rendimenti giornalieri e una più ampia esposizione al rischio specifico. Apple, Exxon Mobil e JPMorgan Chase mostrano livelli di volatilità intermedi, mentre Coca-Cola e Johnson & Johnson presentano le deviazioni standard più basse, rispettivamente pari a 0.010202 e 0.010623. Tale evidenza è coerente con il profilo difensivo dei beni di consumo essenziali e del settore sanitario, che tendono a essere meno sensibili alle oscillazioni cicliche rispetto a comparti più esposti alla congiuntura economica.

I valori minimi e massimi confermano la presenza di oscillazioni giornaliere rilevanti, soprattutto per i titoli caratterizzati da maggiore rischiosità. Boeing mostra sia un minimo molto negativo, pari a -0.110608, sia un massimo elevato, pari a 0.143010, indicando una distribuzione dei rendimenti particolarmente ampia. Anche Apple evidenzia un massimo molto elevato, pari a 0.142617, accompagnato da una volatilità superiore a quella dei titoli difensivi. Exxon Mobil, pur registrando il rendimento medio più alto, presenta una volatilità significativa, ma inferiore a quella di Boeing; ciò suggerisce una performance storica relativamente forte, sebbene accompagnata da un'esposizione non trascurabile al rischio del settore energetico.

La skewness fornisce informazioni sull'asimmetria della distribuzione dei rendimenti. Apple presenta una skewness positiva, indicando una maggiore probabilità relativa di osservare rendimenti estremamente positivi rispetto a rendimenti estremamente negativi. Gli altri titoli mostrano valori negativi o prossimi allo zero. JPMorgan Chase e Johnson & Johnson presentano asimmetrie molto contenute, suggerendo distribuzioni quasi simmetriche. Coca-Cola, Exxon Mobil e Boeing registrano invece skewness negative, che possono essere interpretate come una maggiore incidenza relativa di osservazioni estreme nella coda sinistra della distribuzione, cioè di perdite giornaliere particolarmente marcate.

La kurtosis misura il grado di concentrazione della distribuzione e la rilevanza delle code rispetto a una distribuzione normale. I valori positivi e relativamente elevati osservati per Apple, Johnson & Johnson e JPMorgan Chase indicano distribuzioni leptocurtiche, caratterizzate da code più pesanti e quindi da una maggiore probabilità di rendimenti estremi. Anche Coca-Cola e Boeing presentano valori di kurtosis superiori a zero, confermando che gli eventi estremi non sono trascurabili. Exxon Mobil mostra una kurtosis più contenuta rispetto agli altri titoli, pur mantenendo una distribuzione non perfettamente assimilabile a quella normale.

Nel complesso, i risultati descrittivi hanno implicazioni rilevanti per la costruzione del portafoglio. I titoli con rendimenti medi più elevati, come Exxon Mobil, JPMorgan Chase e Apple, possono contribuire all'incremento del rendimento atteso del portafoglio, ma devono essere valutati congiuntamente alla loro volatilità e alla forma della distribuzione dei rendimenti. I titoli più difensivi, come Coca-Cola e Johnson & Johnson, pur offrendo rendimenti medi inferiori, possono contribuire alla stabilizzazione del portafoglio grazie alla minore volatilità. Boeing, data la combinazione di rendimento medio negativo e volatilità elevata, richiede particolare attenzione nella fase di allocazione, poiché potrebbe aumentare il rischio complessivo senza offrire un adeguato contributo al rendimento atteso. Queste evidenze confermano l'importanza di combinare attività con caratteristiche differenti, affinché la selezione di portafoglio tenga conto non solo della performance media, ma anche della variabilità, dell'asimmetria e della probabilità di eventi estremi.

# 5. Analisi delle correlazioni

L'analisi delle correlazioni rappresenta un passaggio fondamentale nella teoria di portafoglio, poiché consente di valutare in quale misura i rendimenti delle attività finanziarie tendano a muoversi congiuntamente. Nell'ambito della diversificazione, non è sufficiente considerare separatamente il rendimento medio e la volatilità di ciascun titolo: occorre anche esaminare le relazioni statistiche tra le attività incluse nel portafoglio. Due titoli caratterizzati da rischiosità individuale elevata possono infatti generare un portafoglio complessivamente meno rischioso se i loro rendimenti non si muovono in modo perfettamente sincronizzato.

Il coefficiente di correlazione misura l'intensità e la direzione della relazione lineare tra due serie di rendimenti. Esso assume valori compresi tra -1 e +1. Un valore pari a +1 indica una correlazione positiva perfetta, cioè una tendenza dei due rendimenti a variare nella stessa direzione e in proporzione lineare costante. Un valore pari a -1 indica una correlazione negativa perfetta, ossia una tendenza dei rendimenti a muoversi in direzioni opposte. Un valore prossimo a zero segnala invece una relazione lineare debole o assente, pur non escludendo necessariamente altre forme di dipendenza statistica.

La correlazione positiva si verifica quando due attività tendono a registrare rendimenti elevati o bassi nello stesso periodo. In tale situazione, il beneficio di diversificazione è più limitato, poiché eventuali shock sfavorevoli possono colpire simultaneamente entrambe le attività. La correlazione negativa, al contrario, indica che i rendimenti di un'attività tendono ad aumentare quando quelli dell'altra diminuiscono. Questa relazione è particolarmente rilevante per la riduzione del rischio, poiché le perdite di un titolo possono essere compensate, almeno in parte, dai guadagni dell'altro.

Nel quadro di Markowitz, le correlazioni basse o negative sono essenziali perché permettono di ridurre la varianza complessiva del portafoglio a parità di rendimenti attesi individuali. La logica media-varianza mostra infatti che il rischio di portafoglio dipende non solo dalle varianze dei singoli titoli, ma anche dalle covarianze, le quali sono direttamente collegate alle correlazioni. Pertanto, la selezione di attività con correlazioni contenute consente di costruire combinazioni più efficienti, migliorando il profilo rischio-rendimento rispetto a un investimento concentrato in titoli fortemente correlati.

## 5.1 Matrice di correlazione

|      | AAPL | JPM | KO | JNJ | XOM | BA |
|------|------|------|------|------|------|------|
| AAPL | 1.000 | 0.375 | 0.257 | 0.151 | 0.183 | 0.382 |
| JPM  | 0.375 | 1.000 | 0.203 | 0.189 | 0.301 | 0.404 |
| KO   | 0.257 | 0.203 | 1.000 | 0.451 | 0.166 | 0.132 |
| JNJ  | 0.151 | 0.189 | 0.451 | 1.000 | 0.118 | 0.073 |
| XOM  | 0.183 | 0.301 | 0.166 | 0.118 | 1.000 | 0.204 |
| BA   | 0.382 | 0.404 | 0.132 | 0.073 | 0.204 | 1.000 |

La matrice di correlazione evidenzia che tutte le relazioni tra i titoli considerati sono positive, ma generalmente contenute. La correlazione più elevata si osserva tra Coca-Cola (KO) e Johnson & Johnson (JNJ), pari a 0.451. Tale valore indica una relazione positiva moderata tra due titoli appartenenti a settori difensivi, rispettivamente beni di consumo essenziali e sanità. Pur essendo la correlazione più alta del campione, essa rimane lontana da valori prossimi all'unità e non segnala quindi una sovrapposizione quasi perfetta dei movimenti dei rendimenti.

La correlazione più bassa si registra tra Johnson & Johnson (JNJ) e Boeing (BA), pari a 0.073. Questo valore, molto vicino a zero, suggerisce una relazione lineare estremamente debole tra i rendimenti dei due titoli. Dal punto di vista della diversificazione, tale evidenza è rilevante perché indica che le variazioni di Boeing, titolo industriale e aerospaziale caratterizzato da maggiore volatilità, risultano scarsamente associate ai movimenti di Johnson & Johnson, società appartenente a un settore più difensivo.

Un elemento particolarmente significativo è l'assenza di correlazioni molto elevate tra le attività selezionate. Nessuna coppia di titoli presenta valori prossimi a 0.80 o 0.90, soglie che indicherebbero una forte dipendenza lineare e una conseguente riduzione dei benefici di diversificazione. Anche le correlazioni relativamente più alte, come JPMorgan Chase (JPM) con Boeing (BA), pari a 0.404, e Apple (AAPL) con Boeing (BA), pari a 0.382, rimangono su livelli moderati.

Questi risultati confermano la presenza di benefici di diversificazione all'interno dell'universo di titoli considerato. La combinazione di imprese appartenenti a settori differenti consente infatti di ridurre l'esposizione a shock specifici di singole società o comparti economici. Le correlazioni contenute indicano che i rendimenti non si muovono in modo perfettamente coordinato, rendendo possibile una riduzione del rischio complessivo attraverso un'adeguata scelta dei pesi di portafoglio.

Nel complesso, la struttura delle correlazioni suggerisce che i titoli selezionati siano appropriati per la successiva costruzione di portafogli secondo l'approccio di Markowitz. L'eterogeneità settoriale e l'assenza di relazioni lineari eccessivamente elevate offrono una base empirica favorevole per l'analisi media-varianza. La matrice è inoltre rappresentata graficamente nella heatmap delle correlazioni generata durante l'analisi, salvata nel file `figures/correlation_heatmap.png`, che consente di visualizzare in modo immediato l'intensità relativa delle relazioni tra i rendimenti dei titoli.
