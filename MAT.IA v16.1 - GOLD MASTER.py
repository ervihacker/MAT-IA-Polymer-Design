import json, os, math, sys

class MatIA_FinalArchitect:
    def __init__(self):
        self.db_file = "matia_final_db.json"
        self.data = self.load_or_create_db()
        self.print_banner()

    def print_banner(self):
        print(r"""
        █▀▄▀█ ▄▀█ ▀█▀ █ ▄▀█    █░█ ▄H▄ ▀█ █▀
        █░▀░█ █▀█ ░█░ █ █▀█    ▀▄▀ ░16░ █▄ █
        ===  THE FINAL ARCHITECT v16.1  ===
        [  LABORATORY EDITION: FULL AI  ]
        """)

    def load_or_create_db(self):
        if os.path.exists(self.db_file):
            try:
                with open(self.db_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                print("[!] Erro ao ler DB. Recriando padrão...")

        # --- O BIG VAULT (DADOS REAIS DE ENGENHARIA) ---
        default_db = {
            "polymers": {
                "PP":    {"name": "Polipropileno Homo", "hsp": [18.0, 0.0, 0.0], "mod": 1.5, "tg": -10, "density": 0.90},
                "PP-CP": {"name": "PP Copolímero Random", "hsp": [17.8, 0.5, 0.5], "mod": 1.0, "tg": -15, "density": 0.89},
                "HDPE":  {"name": "PE Alta Densidade", "hsp": [17.5, 0.0, 0.0], "mod": 1.1, "tg": -110, "density": 0.95},
                "LDPE":  {"name": "PE Baixa Densidade", "hsp": [16.8, 0.0, 0.0], "mod": 0.3, "tg": -100, "density": 0.92},
                "PS":    {"name": "Poliestireno Cristal", "hsp": [21.3, 5.8, 4.3], "mod": 3.0, "tg": 100, "density": 1.05},
                "HIPS":  {"name": "Poliestireno Alto Impacto", "hsp": [18.5, 4.0, 3.0], "mod": 2.2, "tg": 95, "density": 1.04},
                "PVC":   {"name": "PVC Rígido", "hsp": [18.2, 7.5, 3.4], "mod": 3.0, "tg": 80, "density": 1.38},
                "ABS":   {"name": "ABS Standard", "hsp": [15.3, 6.1, 3.9], "mod": 2.3, "tg": 105, "density": 1.06},
                "PC":    {"name": "Policarbonato", "hsp": [19.2, 5.9, 4.1], "mod": 2.4, "tg": 145, "density": 1.20},
                "PA6":   {"name": "Poliamida 6 (Nylon)", "hsp": [17.0, 11.0, 13.0], "mod": 2.8, "tg": 50, "density": 1.13},
                "PA66":  {"name": "Poliamida 6.6", "hsp": [16.0, 12.0, 11.0], "mod": 3.2, "tg": 70, "density": 1.14},
                "POM":   {"name": "Poliacetal", "hsp": [16.5, 9.0, 12.0], "mod": 2.9, "tg": -70, "density": 1.41},
                "PBT":   {"name": "Polibutileno Tereftalato", "hsp": [18.3, 5.4, 7.5], "mod": 2.6, "tg": 66, "density": 1.31},
                "PET-G": {"name": "PET Glicolizado", "hsp": [19.1, 7.4, 9.5], "mod": 2.1, "tg": 80, "density": 1.27},
                "PET-A": {"name": "PET Amorfo", "hsp": [18.2, 6.3, 8.1], "mod": 2.5, "tg": 75, "density": 1.33},
                "PMMA":  {"name": "Acrílico (PMMA)", "hsp": [18.6, 10.5, 7.5], "mod": 3.1, "tg": 105, "density": 1.18},
                "PEEK":  {"name": "Poli-Éter-Éter-Cetona", "hsp": [19.5, 8.2, 4.5], "mod": 3.8, "tg": 143, "density": 1.32}
            },
            "fillers": {
                "GF":   {"name": "Fibra de Vidro Curta", "factor": 4.5},
                "CF":   {"name": "Fibra de Carbono", "factor": 12.0},
                "TALC": {"name": "Talco Mineral", "factor": 1.8},
                "CACO3":{"name": "Carbonato de Cálcio", "factor": 1.2},
                "GB":   {"name": "Microesferas de Vidro", "factor": 1.1}
            },
            "compatibilizers": {
                "G_MA":   {"name": "PP Enxertado Maleico", "hsp": [17.8, 6.0, 8.0], "recovery": 0.95},
                "SEBS":   {"name": "Elastômero SEBS", "hsp": [17.2, 0.5, 1.0], "recovery": 0.90},
                "EVA-C":  {"name": "EVA Modificado", "hsp": [16.5, 3.0, 4.0], "recovery": 0.88},
                "CORE-S": {"name": "Core-Shell (MBS)", "hsp": [18.5, 7.0, 5.0], "recovery": 0.98}
            },
            "additives": {
                "UV":     {"name": "Estabilizante HALS UV", "func": "Proteção Solar 5+ Anos"},
                "V0":     {"name": "Retardante Chama Halogenado", "func": "Segurança Fogo UL94 V0"},
                "AO":     {"name": "Antioxidante Fenólico", "func": "Proteção Processamento"},
                "PLAST":  {"name": "Plastificante Ftalato", "func": "Redutor de Tg (Flexível)"},
                "IMPACT": {"name": "Modificador de Impacto", "func": "Aumento de Tenacidade"}
            }
        }
        self.save_db(default_db)
        return default_db

    def save_db(self, data):
        with open(self.db_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def view_catalog(self):
        print("\n" + "═"*75)
        print(f"{'CATÁLOGO DE MATERIAIS (BIG VAULT)':^75}")
        print("═"*75)
        print(f"\n[1] MATRIZES POLIMÉRICAS (Base)")
        print(f" {'ID':<8} | {'NOME TÉCNICO':<30} | {'MOD(GPa)':<8} | {'Tg(°C)':<6}")
        print("-" * 75)
        for k, v in self.data['polymers'].items():
            print(f" {k:<8} | {v['name']:<30} | {v['mod']:<8} | {v['tg']:<6}")
        print(f"\n[2] CARGAS & REFORÇOS")
        print(f" {'ID':<8} | {'NOME':<30} | {'FATOR REFORÇO'}")
        print("-" * 75)
        for k, v in self.data['fillers'].items():
            print(f" {k:<8} | {v['name']:<30} | {v['factor']}x")
        print(f"\n[3] COMPATIBILIZANTES (A 'Cola')")
        print(f" {'ID':<8} | {'NOME':<30} | {'RECUPERAÇÃO'}")
        print("-" * 75)
        for k, v in self.data['compatibilizers'].items():
            print(f" {k:<8} | {v['name']:<30} | {v['recovery']*100:.0f}%")
        print(f"\n[4] ADITIVOS FUNCIONAIS")
        print(f" {'ID':<8} | {'FUNÇÃO'}")
        print("-" * 75)
        for k, v in self.data['additives'].items():
            print(f" {k:<8} | {v['func']}")
        print("═"*75 + "\n")

    def edit_database(self):
        while True:
            # Limpa a tela (opcional, se tiver a função)
            print("\n--- EDITOR DE BANCO DE DADOS (v16.2) ---")
            print("1. Adicionar Polímero")
            print("2. Adicionar Carga")
            print("3. Adicionar Compatibilizante")
            print("4. REMOVER Material")  # NOVA OPÇÃO
            print("5. Voltar")
            
            op = input("Opção >> ")
            
            if op == '5':
                break
                
            # --- ROTINA DELETAR ---
            if op == '4':
                target = input("Digite a Sigla ID para apagar: ").strip().upper()
                found = False
                # Procura em todas as categorias
                for category in ['polymers', 'fillers', 'compatibilizers']:
                    if target in self.data[category]:
                        del self.data[category][target]
                        self.save_db(self.data)
                        print(f"[OK] '{target}' foi removido de {category}.")
                        found = True
                        break
                if not found:
                    print(f"[Erro] ID '{target}' não encontrado em nenhuma lista.")
                continue

            # --- ROTINAS DE ADICIONAR ---
            try:
                # 1. POLIMERO
                if op == '1':
                    pid = input("Sigla ID (Ex: PLA): ").strip().upper()
                    # Proteção Duplicata
                    if pid in self.data['polymers']:
                        print(f"[!] O ID '{pid}' já existe! Use a opção de remover antes se quiser alterar.")
                        continue
                        
                    name = input("Nome Completo: ")
                    dd = float(input("dD: ").replace(',', '.'))
                    dp = float(input("dP: ").replace(',', '.'))
                    dh = float(input("dH: ").replace(',', '.'))
                    mod = float(input("Módulo (GPa): ").replace(',', '.'))
                    tg = float(input("Tg (°C): ").replace(',', '.'))
                    
                    self.data['polymers'][pid] = {
                        "name": name, "hsp": [dd, dp, dh], 
                        "mod": mod, "tg": tg, "density": 1.0
                    }
                    print(f"[OK] Polímero {pid} salvo!")

                # 2. CARGA
                elif op == '2':
                    fid = input("Sigla ID (Ex: GF): ").strip().upper()
                    if fid in self.data['fillers']:
                        print(f"[!] O ID '{fid}' já existe!")
                        continue
                        
                    name = input("Nome: ")
                    fac = float(input("Fator de Reforço: ").replace(',', '.'))
                    self.data['fillers'][fid] = {"name": name, "factor": fac}
                    print(f"[OK] Carga {fid} salva!")

                # 3. COMPATIBILIZANTE
                elif op == '3':
                    cid = input

    def calculate_physics(self, mixture_str):
        components = []
        raw_parts = mixture_str.replace(' ', '').upper().split(',')
        temp_sum = 0
        for p in raw_parts:
            if not p: continue
            try:
                if ':' not in p: raise ValueError
                pid, perc_str = p.split(':')
                perc = float(perc_str.replace(',', '.'))
                temp_sum += perc
                if pid in self.data['polymers']: ctype = 'polymer'
                elif pid in self.data['fillers']: ctype = 'filler'
                elif pid in self.data['compatibilizers']: ctype = 'compatibilizer'
                elif pid in self.data['additives']: ctype = 'additive'
                else: return None
                components.append({'id': pid, 'perc': perc, 'type': ctype})
            except: return None

        if temp_sum <= 0: return None
        if not (99.9 <= temp_sum <= 100.1):
            for c in components: c['perc'] = (c['perc'] / temp_sum) * 100

        poly_mix = [c for c in components if c['type'] == 'polymer']
        compat_mix = [c for c in components if c['type'] == 'compatibilizer']
        filler_mix = [c for c in components if c['type'] == 'filler']
        addit_mix  = [c for c in components if c['type'] == 'additive']

        if not poly_mix: return None

        cm_dd, cm_dp, cm_dh = 0, 0, 0
        inv_tg_sum = 0
        base_modulus = 0
        total_poly = sum(c['perc'] for c in poly_mix)

        for p in poly_mix:
            d = self.data['polymers'][p['id']]
            w = p['perc'] / total_poly
            cm_dd += d['hsp'][0] * w
            cm_dp += d['hsp'][1] * w
            cm_dh += d['hsp'][2] * w
            inv_tg_sum += w / (d['tg'] + 273.15)
            base_modulus += d['mod'] * w

        tg_final = (1 / inv_tg_sum) - 273.15
        
        instability = 0
        for p in poly_mix:
            d = self.data['polymers'][p['id']]
            dist = math.sqrt(4*(d['hsp'][0]-cm_dd)**2 + (d['hsp'][1]-cm_dp)**2 + (d['hsp'][2]-cm_dh)**2)
            instability += dist * (p['perc'] / total_poly)

        st_factor = 1.0
        status = "ESTÁVEL (Miscível)"
        if instability > 6.0:
            status = "INSTÁVEL (Separado)"
            st_factor = 0.60
            if compat_mix:
                best_rec = max([self.data['compatibilizers'][c['id']]['recovery'] for c in compat_mix])
                st_factor = best_rec
                status = f"COMPATIBILIZADO ({int(best_rec*100)}%)"

        current_modulus = base_modulus * st_factor
        for f in filler_mix:
            fdata = self.data['fillers'][f['id']]
            current_modulus *= (1 + ((f['perc']/100) * fdata['factor']))

        notes = []
        for a in addit_mix:
            adata = self.data['additives'][a['id']]
            notes.append(adata['func'])
            if a['id'] == "PLAST": current_modulus *= 0.85; tg_final -= 15
            if a['id'] == "IMPACT": current_modulus *= 0.80

        return {"modulus": current_modulus, "tg": tg_final, "ra": instability, "status": status, "notes": notes, "comps": components}

    # --- IA REVERSA V16.1 (PRIORIDADE + ADITIVOS CORRIGIDO) ---
    def ai_reverse(self):
        print("\n--- IA REVERSA (FULL SCAN) ---")
        try:
            t_mod = float(input("Módulo Alvo (GPa): ").replace(',', '.'))
            t_tg = float(input("Tg Alvo (°C): ").replace(',', '.'))
            
            print("\nO QUE É MAIS CRÍTICO?")
            print("[1] Rigidez (Priorizar GPa)")
            print("[2] Temperatura (Priorizar Tg)")
            prio = input("Opção [1/2]: ")
        except ValueError: return

        print("[IA] Iniciando varredura (Matrizes, Cargas e Química Fina)...")
        best = None
        min_err = float('inf')
        
        polys = list(self.data['polymers'].keys())
        fillers = list(self.data['fillers'].keys())
        
        candidates = []
        # 1. Puros
        for p in polys: candidates.append(f"{p}:100")
        
        # 2. Com Cargas (Reforço)
        for p in polys:
            for f in fillers:
                for per in [10, 20, 30, 40, 50]:
                    candidates.append(f"{p}:{100-per}, {f}:{per}")

        # 3. Com Aditivos (AQUI ESTÁ A CORREÇÃO!)
        # Agora a IA sabe usar PLAST para baixar Tg
        for p in polys:
            for a in ['PLAST', 'IMPACT']:
                for per in [5, 10, 15, 20]:
                     candidates.append(f"{p}:{100-per}, {a}:{per}")

        for mix in candidates:
            res = self.calculate_physics(mix)
            if res:
                diff_mod = abs(res['modulus'] - t_mod)
                diff_tg = abs(res['tg'] - t_tg)

                if prio == '2': # Prioridade Temperatura (Tg)
                    err = (diff_tg * 15) + (diff_mod * 0.5)
                else: # Prioridade Rigidez (GPa)
                    err = (diff_mod * 15) + (diff_tg * 0.5)

                if err < min_err: 
                    min_err = err
                    best = mix

        print(f"\n[SUGESTÃO] Melhor formulação encontrada: {best}")
        if best: self.print_report(self.calculate_physics(best))

    def print_report(self, res):
        if not res: return
        print("\n" + "═"*50)
        print(f"{'FICHA TÉCNICA FINAL':^50}")
        print("═"*50)
        print("COMPOSIÇÃO:")
        for c in res['comps']: print(f" > {c['perc']:.1f}% {c['id']}")
        print("─"*50)
        print(f"Módulo (Rigidez): {res['modulus']:.2f} GPa")
        print(f"Tg (Térmica):     {res['tg']:.1f} °C")
        print(f"Hansen (Ra):      {res['ra']:.2f}")
        print(f"Status:           {res['status']}")
        if res['notes']:
            print("─"*50)
            for n in res['notes']: print(f" [Aditivo] {n}")
        print("═"*50 + "\n")

    def run(self):
        while True:
            print("\n=== MENU PRINCIPAL ===")
            print("1. VER CATÁLOGO")
            print("2. MISTURAR")
            print("3. IA REVERSA")
            print("4. EDITAR BANCO")
            print("5. SAIR")
            op = input(">> ")
            if op == '1': self.view_catalog()
            elif op == '2':
                print("\n[DICA] Use IDs. Ex: PP:70, GF:30")
                s = input("Mistura: ")
                res = self.calculate_physics(s)
                if res: self.print_report(res)
                else: print("[!] Entrada inválida.")
            elif op == '3': self.ai_reverse()
            elif op == '4': self.edit_database()
            elif op == '5': break

if __name__ == "__main__":
    MatIA_FinalArchitect().run()

