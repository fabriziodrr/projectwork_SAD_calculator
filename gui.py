import customtkinter as ctk
from tkinter import messagebox
import math
import re

# Import dei moduli (mantenuti dalla tua struttura)
from src.addizione import calcola_somma_utente
from src.sottrazione import sottrazione_vettore
from src.moltiplicazione import moltiplicazione
from src.divisione import calcola_divisione_utente
from src.seno import calcola_seno
from src.coseno import calcola_coseno_utente
from src.tangente import calcola_tangente_utente
from src.cotangente import calcola_cotangente_utente
from src.arcoseno import calcola_arcoseno
from src.arcocoseno import calcola_arcocoseno_utente

# Imposta il tema moderno
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class CalcolatriceGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("SAD Calculator - Calcolatrice Modulare")
        self.root.geometry("800x650")
        self.root.minsize(700, 600)
        
        # Variabili di stato
        self.cronologia = []
        self.ultimo_risultato = 0

        # --- TITOLO ---
        self.title_label = ctk.CTkLabel(root, text="SAD Calculator", font=ctk.CTkFont(size=28, weight="bold"))
        self.title_label.pack(pady=(20, 5))
        self.subtitle_label = ctk.CTkLabel(root, text="Ingegneria del Software", font=ctk.CTkFont(size=14, slant="italic"), text_color="gray")
        self.subtitle_label.pack(pady=(0, 20))

        # --- DISPLAY (Input e Output combinati) ---
        self.display_frame = ctk.CTkFrame(root, corner_radius=15, fg_color="#2B2B2B")
        self.display_frame.pack(pady=10, padx=30, fill="x")

        # Campo di Input
        self.input_entry = ctk.CTkEntry(self.display_frame, font=ctk.CTkFont(size=24), 
                                        placeholder_text="Inserisci numeri (es: 10 5) o 'ans'...",
                                        border_width=0, corner_radius=10, fg_color="#1E1E1E", height=50)
        self.input_entry.pack(pady=(15, 5), padx=20, fill="x")

        # Etichetta di Output
        self.output_label = ctk.CTkLabel(self.display_frame, text="Risultato: --", 
                                         font=ctk.CTkFont(size=22, weight="bold"), text_color="#00FFCC")
        self.output_label.pack(pady=(5, 15), padx=20, anchor="e")

        # --- GRIGLIA PULSANTI (Sezioni divise) ---
        self.grid_frame = ctk.CTkFrame(root, fg_color="transparent")
        self.grid_frame.pack(pady=10, padx=30, fill="both", expand=True)

        self.grid_frame.columnconfigure(0, weight=1)
        self.grid_frame.columnconfigure(1, weight=1)

        # SEZIONE 1: Operazioni Base (Sinistra)
        self.base_frame = ctk.CTkFrame(self.grid_frame, corner_radius=15)
        self.base_frame.grid(row=0, column=0, padx=(0, 10), sticky="nsew")
        
        ctk.CTkLabel(self.base_frame, text="Operazioni Base", font=ctk.CTkFont(size=16, weight="bold")).pack(pady=10)

        base_ops = [
            ("➕ Addizione", self.operazione_addizione),
            ("➖ Sottrazione", self.operazione_sottrazione),
            ("✖️ Moltiplicazione", self.operazione_moltiplicazione),
            ("➗ Divisione", self.operazione_divisione)
        ]
        
        for text, command in base_ops:
            ctk.CTkButton(self.base_frame, text=text, command=command, height=45, 
                          font=ctk.CTkFont(size=15)).pack(pady=8, padx=20, fill="x")

        # SEZIONE 2: Trigonometria (Destra)
        self.trig_frame = ctk.CTkFrame(self.grid_frame, corner_radius=15)
        self.trig_frame.grid(row=0, column=1, padx=(10, 0), sticky="nsew")
        
        ctk.CTkLabel(self.trig_frame, text="Trigonometria", font=ctk.CTkFont(size=16, weight="bold")).pack(pady=10)

        trig_ops = [
            ("sin Seno", self.operazione_seno),
            ("cos Coseno", self.operazione_coseno),
            ("tan Tangente", self.operazione_tangente),
            ("arcsin Arcoseno", self.operazione_arcoseno),
            ("arccos Arcocoseno", self.operazione_arcocoseno),
            ("cot Cotangente", self.operazione_cotangente)
        ]

        # Creiamo una griglia 2 colonne per la trigonometria
        self.trig_inner = ctk.CTkFrame(self.trig_frame, fg_color="transparent")
        self.trig_inner.pack(fill="both", expand=True, padx=10, pady=5)
        self.trig_inner.columnconfigure((0,1), weight=1)

        for i, (text, command) in enumerate(trig_ops):
            # Usiamo un colore viola per distinguere le funzioni scientifiche
            btn = ctk.CTkButton(self.trig_inner, text=text, command=command, height=40,
                                fg_color="#8E44AD", hover_color="#732D91")
            btn.grid(row=i//2, column=i%2, padx=5, pady=8, sticky="ew")

        # --- PANNELLO AZIONI (In fondo) ---
        self.actions_frame = ctk.CTkFrame(root, fg_color="transparent")
        self.actions_frame.pack(pady=20, padx=30, fill="x")
        self.actions_frame.columnconfigure((0, 1, 2), weight=1)

        ctk.CTkButton(self.actions_frame, text="📜 Cronologia", command=self.mostra_cronologia, 
                      height=40, fg_color="#2C3E50", hover_color="#1A252F").grid(row=0, column=0, padx=10, sticky="ew")
        
        ctk.CTkButton(self.actions_frame, text="🧹 Pulisci", command=self.pulisci, 
                      height=40, fg_color="#E67E22", hover_color="#D35400").grid(row=0, column=1, padx=10, sticky="ew")
        
        ctk.CTkButton(self.actions_frame, text="🚪 Esci", command=root.quit, 
                      height=40, fg_color="#E74C3C", hover_color="#C0392B").grid(row=0, column=2, padx=10, sticky="ew")

        # Rendi l'avvio focalizzato sull'input
        self.input_entry.focus()


    # --- METODI HELPER ---
    def get_input_numbers(self):
        """Legge l'input, gestisce 'ans' e restituisce una lista di float."""
        val = self.input_entry.get().strip()
        if not val:
            messagebox.showwarning("Input mancante", "Inserisci i valori nel campo di input prima di selezionare un'operazione.")
            return None
        
        # Sostituisce la parola 'ans' con l'ultimo risultato salvato
        val_lower = val.lower()
        if 'ans' in val_lower:
            val = re.sub(r'(?i)\bans\b', str(self.ultimo_risultato), val_lower)
            self.input_entry.delete(0, 'end')
            self.input_entry.insert(0, val)

        try:
            return [float(x) for x in val.split()]
        except ValueError:
            messagebox.showerror("Errore", "Input non valido! Assicurati di usare numeri o 'ans', separati da spazio.")
            return None

    def set_output(self, result):
        """Mostra il risultato a schermo e lo salva in 'ans'."""
        self.output_label.configure(text=f"Risultato: {result}")
        if isinstance(result, (int, float)):
            self.ultimo_risultato = result
            self.cronologia.append(f"Risultato: {result}")


    # --- OPERAZIONI MATEMATICHE ---
    def operazione_addizione(self):
        nums = self.get_input_numbers()
        if nums:
            result = sum(nums)
            self.set_output(result)

    def operazione_sottrazione(self):
        nums = self.get_input_numbers()
        if nums:
            result = nums[0]
            for num in nums[1:]:
                result -= num
            self.set_output(result)

    def operazione_moltiplicazione(self):
        nums = self.get_input_numbers()
        if nums:
            result = 1
            for num in nums:
                result *= num
            self.set_output(result)

    def operazione_divisione(self):
        nums = self.get_input_numbers()
        if nums:
            if len(nums) < 2:
                messagebox.showerror("Errore", "Per la divisione servono almeno due numeri (dividendo e divisore).")
                return
            result = nums[0]
            for num in nums[1:]:
                if num == 0:
                    messagebox.showerror("Errore", "Impossibile dividere per zero!")
                    return
                result /= num
            self.set_output(result)

    def operazione_seno(self):
        nums = self.get_input_numbers()
        if nums:
            result = round(math.sin(math.radians(nums[0])), 10)
            self.set_output(result)

    def operazione_coseno(self):
        nums = self.get_input_numbers()
        if nums:
            result = round(math.cos(math.radians(nums[0])), 10)
            self.set_output(result)

    def operazione_tangente(self):
        nums = self.get_input_numbers()
        if nums:
            result = round(math.tan(math.radians(nums[0])), 10)
            self.set_output(result)

    def operazione_arcoseno(self):
        nums = self.get_input_numbers()
        if nums:
            if -1 <= nums[0] <= 1:
                result = round(math.degrees(math.asin(nums[0])), 10)
                self.set_output(result)
            else:
                messagebox.showerror("Errore", "Il valore per l'arcoseno deve essere compreso tra -1 e 1!")

    def operazione_arcocoseno(self):
        nums = self.get_input_numbers()
        if nums:
            if -1 <= nums[0] <= 1:
                result = round(math.degrees(math.acos(nums[0])), 10)
                self.set_output(result)
            else:
                messagebox.showerror("Errore", "Il valore per l'arcocoseno deve essere compreso tra -1 e 1!")

    def operazione_cotangente(self):
        nums = self.get_input_numbers()
        if nums:
            tan_val = math.tan(math.radians(nums[0]))
            if round(tan_val, 10) == 0:
                messagebox.showerror("Errore", "Cotangente indefinita per questo valore!")
                return
            result = round(1 / tan_val, 10)
            self.set_output(result)

    # --- FUNZIONI DI SERVIZIO ---
    def mostra_cronologia(self):
        if not self.cronologia:
            messagebox.showinfo("Cronologia", "Nessuna operazione salvata in cronologia.")
        else:
            history_text = "\n".join(f"{i+1}. {op}" for i, op in enumerate(self.cronologia[-15:])) # Mostra le ultime 15
            messagebox.showinfo("Cronologia (Ultime 15)", history_text)

    def pulisci(self):
        self.input_entry.delete(0, 'end')
        self.output_label.configure(text="Risultato: --")
        self.input_entry.focus()


if __name__ == "__main__":
    root = ctk.CTk()
    app = CalcolatriceGUI(root)
    root.mainloop()