import pdfplumber

def leggi_dati_da_pdf(percorso_file_pdf):
    dati_estratti = []
    try:
        with pdfplumber.open(percorso_file_pdf) as pdf:
            # Itera su ogni pagina del PDF
            for pagina in pdf.pages:
                # Esempio: estrai tutto il testo da una pagina
                testo_pagina = pagina.extract_text()
                # print(f"Testo pagina {pagina.page_number}:\n{testo_pagina}\n")

                # Esempio: estrai tabelle se presenti (richiede che le tabelle siano ben formattate)
                tabelle = pagina.extract_tables()
                if tabelle:
                    for tabella in tabelle:
                        # Ogni tabella è una lista di liste (righe e colonne)
                        # Qui potresti voler processare o filtrare la tabella
                        # print(f"Tabella trovata nella pagina {pagina.page_number}:\n{tabella}\n")
                        dati_estratti.extend(tabella) # Aggiungi i dati della tabella
    
    except Exception as e:
        print(f"Errore durante la lettura del PDF: {e}")
        return None
    return dati_estratti

if __name__ == "__main__":
    # Assicurati di avere un file PDF con questo nome nella stessa directory dello script
    nome_file_pdf = "esempio_report.pdf" 
    dati_del_report = leggi_dati_da_pdf(nome_file_pdf)

    if dati_del_report:
        print(f"Dati estratti dal PDF '{nome_file_pdf}':")
        for riga in dati_del_report:
            print(riga)
    else:
        print("Nessun dato estratto o errore nella lettura del PDF.")
