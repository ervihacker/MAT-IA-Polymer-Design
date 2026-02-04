import json, os, math, sys

class PolymerDesigner:
    def __init__(self):
        self.db_file = "matia_db_v01.json"
        self.data = self.load_or_create_db()
        self.print_banner()

    def print_banner(self):
        print(r"""
        █▀▄▀█ ▄▀█ ▀█▀ █ ▄▀█    █░█ ▄▀█ ░░█ ▄▀█
        █░▀░█ █▀█ ░█░ █ █▀█    ▀▄▀ █▄█ ▀▀█ █▄█
        ===  MAT.IA v0.1 (Beta)  ===
        [ POLYMER DESIGN TOOL - MIT EDITION ]
        """)

    def load_or_create_db(self):
        if os.path.exists(self.db_file):
            try:
                with open(self.db_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                print("[!] Database Error. Creating default...")

        # --- THE VAULT (Default Data) ---
        default_db = {
            "polymers": {
                "PP":    {"name": "Polypropylene Homopolymer", "hsp": [18.0, 0.0, 0.0], "mod": 1.5, "tg": -10, "density": 0.90},
                "PP-CP": {"name": "PP Copolymer Random", "hsp": [17.8, 0.5, 0.5], "mod": 1.0, "tg": -15, "density": 0.89},
                "HDPE":  {"name": "High Density PE", "hsp": [17.5, 0.0, 0.0], "mod": 1.1, "tg": -110, "density": 0.95},
                "LDPE":  {"name": "Low Density PE", "hsp": [16.8, 0.0, 0.0], "mod": 0.3, "tg": -100, "density": 0.92},
                "PS":    {"name": "Polystyrene Crystal", "hsp": [21.3, 5.8, 4.3], "mod": 3.0, "tg": 100, "density": 1.05},
                "HIPS":  {"name": "High Impact Polystyrene", "hsp": [18.5, 4.0, 3.0], "mod": 2.2, "tg": 95, "density": 1.04},
                "PVC":   {"name": "Rigid PVC", "hsp": [18.2, 7.5, 3.4], "mod": 3.0, "tg": 80, "density": 1.38},
                "ABS":   {"name": "ABS Standard", "hsp": [15.3, 6.1, 3.9], "mod": 2.3, "tg": 105, "density": 1.06},
                "PC":    {"name": "Polycarbonate", "hsp": [19.2, 5.9, 4.1], "mod": 2.4, "tg": 145, "density": 1.20},
                "PA6":   {"name": "Polyamide 6 (Nylon)", "hsp": [17.0, 11.0, 13.0], "mod": 2.8, "tg": 50, "density": 1.13},
                "PA66":  {"name": "Polyamide 6.6", "hsp": [16.0, 12.0, 11.0], "mod": 3.2, "tg": 70, "density": 1.14},
                "POM":   {"name": "Polyacetal (POM)", "hsp": [16.5, 9.0, 12.0], "mod": 2.9, "tg": -70, "density": 1.41},
                "PBT":   {"name": "PBT", "hsp": [18.3, 5.4, 7.5], "mod": 2.6, "tg": 66, "density": 1.31},
                "PET-G": {"name": "PET-G", "hsp": [19.1, 7.4, 9.5], "mod": 2.1, "tg": 80, "density": 1.27},
                "PET-A": {"name": "Amorphous PET", "hsp": [18.2, 6.3, 8.1], "mod": 2.5, "tg": 75, "density": 1.33},
                "PMMA":  {"name": "Acrylic (PMMA)", "hsp": [18.6, 10.5, 7.5], "mod": 3.1, "tg": 105, "density": 1.18},
                "PEEK":  {"name": "PEEK", "hsp": [19.5, 8.2, 4.5], "mod": 3.8, "tg": 143, "density": 1.32}
            },
            "fillers": {
                "GF":    {"name": "Glass Fiber (Short)", "factor": 4.5},
                "CF":    {"name": "Carbon Fiber", "factor": 12.0},
                "TALC":  {"name": "Talc Mineral", "factor": 1.8},
                "CACO3": {"name": "Calcium Carbonate", "factor": 1.2},
                "GB":    {"name": "Glass Beads", "factor": 1.1}
            },
            "compatibilizers": {
                "G_MA":   {"name": "PP-g-MA (Grafted)", "hsp": [17.8, 6.0, 8.0], "recovery": 0.95},
                "SEBS":   {"name": "SEBS Elastomer", "hsp": [17.2, 0.5, 1.0], "recovery": 0.90},
                "EVA-C":  {"name": "Modified EVA", "hsp": [16.5, 3.0, 4.0], "recovery": 0.88},
                "CORE-S": {"name": "Core-Shell (MBS)", "hsp": [18.5, 7.0, 5.0], "recovery": 0.98}
            },
            "additives": {
                "UV":     {"name": "HALS UV Stabilizer", "func": "UV Protection 5+ Years"},
                "V0":     {"name": "Halogenated FR", "func": "Flame Retardant UL94 V0"},
                "AO":     {"name": "Phenolic Antioxidant", "func": "Processing Stability"},
                "PLAST":  {"name": "Phthalate Plasticizer", "func": "Tg Reducer (Flexibility)"},
                "IMPACT": {"name": "Impact Modifier", "func": "Toughness Booster"}
            }
        }
        self.save_db(default_db)
        return default_db

    def save_db(self, data):
        with open(self.db_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def view_catalog(self):
        print("\n" + "═"*75)
        print(f"{'MATERIAL DATABASE (CATALOG)':^75}")
        print("═"*75)
        print(f"\n[1] POLYMER MATRICES")
        print(f" {'ID':<8} | {'NAME':<30} | {'MOD(GPa)':<8} | {'Tg(°C)':<6}")
        print("-" * 75)
        for k, v in self.data['polymers'].items():
            print(f" {k:<8} | {v['name']:<30} | {v['mod']:<8} | {v['tg']:<6}")
        print(f"\n[2] FILLERS & REINFORCEMENT")
        print(f" {'ID':<8} | {'NAME':<30} | {'REINFORCEMENT'}")
        print("-" * 75)
        for k, v in self.data['fillers'].items():
            print(f" {k:<8} | {v['name']:<30} | {v['factor']}x")
        print(f"\n[3] COMPATIBILIZERS")
        print(f" {'ID':<8} | {'NAME':<30} | {'RECOVERY'}")
        print("-" * 75)
        for k, v in self.data['compatibilizers'].items():
            print(f" {k:<8} | {v['name']:<30} | {v['recovery']*100:.0f}%")
        print(f"\n[4] FUNCTIONAL ADDITIVES")
        print(f" {'ID':<8} | {'FUNCTION'}")
        print("-" * 75)
        for k, v in self.data['additives'].items():
            print(f" {k:<8} | {v['func']}")
        print("═"*75 + "\n")

    def edit_database(self):
        while True:
            print("\n--- DATABASE EDITOR (v0.1 Beta) ---")
            print("1. Add Polymer (Matrix)")
            print("2. Add Filler")
            print("3. Add Compatibilizer")
            print("4. REMOVE Material")
            print("5. Back")
            
            op = input("Option >> ")
            
            if op == '5':
                break
            
            # --- REMOVE ROUTINE ---
            if op == '4':
                target = input("Enter ID to delete (e.g., PP): ").strip().upper()
                found = False
                for category in ['polymers', 'fillers', 'compatibilizers']:
                    if target in self.data[category]:
                        del self.data[category][target]
                        self.save_db(self.data)
                        print(f"[OK] '{target}' removed from {category}.")
                        found = True
                        break
                if not found:
                    print(f"[Error] ID '{target}' not found.")
                continue

            # --- ADD ROUTINES ---
            try:
                if op == '1':
                    pid = input("ID Tag (e.g., PLA): ").strip().upper()
                    if pid in self.data['polymers']:
                        print(f"[!] ID '{pid}' exists! Delete first to overwrite.")
                        continue
                    name = input("Full Name: ")
                    dd = float(input("Dispersion (dD): ").replace(',', '.'))
                    dp = float(input("Polarity (dP): ").replace(',', '.'))
                    dh = float(input("Hydrogen (dH): ").replace(',', '.'))
                    mod = float(input("Modulus (GPa): ").replace(',', '.'))
                    tg = float(input("Tg (°C): ").replace(',', '.'))
                    self.data['polymers'][pid] = {"name": name, "hsp": [dd, dp, dh], "mod": mod, "tg": tg, "density": 1.0}
                    print(f"[OK] Polymer {pid} saved!")

                elif op == '2':
                    fid = input("ID Tag (e.g., GF): ").strip().upper()
                    if fid in self.data['fillers']:
                        print(f"[!] ID '{fid}' exists!")
                        continue
                    name = input("Name: ")
                    fac = float(input("Reinforcement Factor: ").replace(',', '.'))
                    self.data['fillers'][fid] = {"name": name, "factor": fac}
                    print(f"[OK] Filler {fid} saved!")

                elif op == '3':
                    cid = input("ID Tag (e.g., GMA): ").strip().upper()
                    if cid in self.data['compatibilizers']:
                        print(f"[!] ID '{cid}' exists!")
                        continue
                    name = input("Name: ")
                    rec = float(input("Recovery Rate (0-1): ").replace(',', '.'))
                    self.data['compatibilizers'][cid] = {"name": name, "hsp": [0,0,0], "recovery": rec}
                    print(f"[OK] Compatibilizer {cid} saved!")
                
                self.save_db(self.data)

            except ValueError:
                print("[!] Error: Use valid numbers (use '.' for decimals).")

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
        status = "STABLE (Miscible)"
        if instability > 6.0:
            status = "UNSTABLE (Phase Separation)"
            st_factor = 0.60
            if compat_mix:
                best_rec = max([self.data['compatibilizers'][c['id']]['recovery'] for c in compat_mix])
                st_factor = best_rec
                status = f"COMPATIBILIZED ({int(best_rec*100)}%)"

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

    def ai_reverse(self):
        print("\n--- INVERSE DESIGN AI (FULL SCAN) ---")
        try:
            t_mod = float(input("Target Modulus (GPa): ").replace(',', '.'))
            t_tg = float(input("Target Tg (°C): ").replace(',', '.'))
            
            print("\nWHAT IS CRITICAL?")
            print("[1] Stiffness (Prioritize GPa)")
            print("[2] Temperature (Prioritize Tg)")
            prio = input("Option [1/2]: ")
        except ValueError: return

        print("[AI] Scanning formulations (Matrices, Fillers, Chemistry)...")
        best = None
        min_err = float('inf')
        
        polys = list(self.data['polymers'].keys())
        fillers = list(self.data['fillers'].keys())
        
        candidates = []
        # 1. Pure
        for p in polys: candidates.append(f"{p}:100")
        
        # 2. With Fillers
        for p in polys:
            for f in fillers:
                for per in [10, 20, 30, 40, 50]:
                    candidates.append(f"{p}:{100-per}, {f}:{per}")

        # 3. With Additives
        for p in polys:
            for a in ['PLAST', 'IMPACT']:
                for per in [5, 10, 15, 20]:
                     candidates.append(f"{p}:{100-per}, {a}:{per}")

        for mix in candidates:
            res = self.calculate_physics(mix)
            if res:
                diff_mod = abs(res['modulus'] - t_mod)
                diff_tg = abs(res['tg'] - t_tg)

                if prio == '2': # Prio Tg
                    err = (diff_tg * 15) + (diff_mod * 0.5)
                else: # Prio GPa
                    err = (diff_mod * 15) + (diff_tg * 0.5)

                if err < min_err: 
                    min_err = err
                    best = mix

        print(f"\n[SUGGESTION] Best formulation found: {best}")
        if best: self.print_report(self.calculate_physics(best))

    def print_report(self, res):
        if not res: return
        print("\n" + "═"*50)
        print(f"{'FINAL TECHNICAL DATASHEET':^50}")
        print("═"*50)
        print("COMPOSITION:")
        for c in res['comps']: print(f" > {c['perc']:.1f}% {c['id']}")
        print("─"*50)
        print(f"Modulus (Stiffness): {res['modulus']:.2f} GPa")
        print(f"Tg (Thermal):        {res['tg']:.1f} °C")
        print(f"Hansen (Ra):         {res['ra']:.2f}")
        print(f"Status:              {res['status']}")
        if res['notes']:
            print("─"*50)
            for n in res['notes']: print(f" [Additive] {n}")
        print("═"*50 + "\n")

    def run(self):
        while True:
            print("\n" + "="*40)
            print(" MAT.IA v0.1 (Beta) - Polymer Design Tool")
            print("="*40)
            print("1. Design Formulation (Inverse Design)")
            print("2. Check Compatibility (Hansen)")
            print("3. Show Database")
            print("4. Database Editor (Add/Remove)")
            print("5. Exit")
            print("-" * 40)
            
            op = input("Select Option >> ")
            
            if op == '1': self.ai_reverse()
            elif op == '2':
                print("\n[TIP] Use IDs. Ex: PP:70, GF:30")
                s = input("Mix: ")
                res = self.calculate_physics(s)
                if res: self.print_report(res)
                else: print("[!] Invalid Input.")
            elif op == '3': self.view_catalog()
            elif op == '4': self.edit_database()
            elif op == '5': 
                print("Exiting MAT.IA... See you!")
                break
            else:
                print("[!] Invalid Option.")

if __name__ == "__main__":
    PolymerDesigner().run()


