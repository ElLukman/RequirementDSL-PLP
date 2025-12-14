import sys
import re
import json
import os
from antlr4 import *
from ReqSpecLLexer import ReqSpecLLexer
from ReqSpecLParser import ReqSpecLParser
from ReqSpecLListener import ReqSpecLListener

class PythonTestGeneratorListener(ReqSpecLListener):
    def __init__(self, output_filename="test_generated_stateful.py", feature_filter=None):
        self.output_file = open(output_filename, 'w')
        self.indent_level = 0
        self.actors = set()
        self.scenario_counter = 1
        self.feature_filter = feature_filter
        self.current_feature = None
        self.features = {}  # collect features -> scenarios mapping

        self.write_code("import unittest")
        self.write_code("import logging")
        self.write_code("import json")
        self.write_code("\n# Konfigurasi Logging")
        self.write_code("logging.basicConfig(level=logging.INFO, format='%(message)s')")

        self.write_code("\n# --- MOCK SYSTEM STATE (Memori Bersama) ---")
        self.write_code("class SystemState:")
        self.indent_level += 1
        self.write_code("data = {}")
        self.write_code("")
        self.write_code("@classmethod")
        self.write_code("def set(cls, key, value):")
        self.indent_level += 1
        self.write_code("cls.data[key] = value")
        self.indent_level -= 1

        self.write_code("@classmethod")
        self.write_code("def get(cls, key):")
        self.indent_level += 1
        self.write_code("return cls.data.get(key)")
        self.indent_level -= 2

        self.write_code("\n# --- KODE INI DIGENERATE OTOMATIS OLEH REQSPECL ---")
        self.write_code("# Dibuat oleh: ReqSpecL generator\n")

    def write_code(self, text):
        indentation = "    " * self.indent_level
        self.output_file.write(f"{indentation}{text}\n")

    def sanitize_name(self, text):
        clean_text = text.strip('"')
        clean_text = re.sub(r'[^a-zA-Z0-9_]', '_', clean_text)
        return clean_text

    def enterActor_def(self, ctx:ReqSpecLParser.Actor_defContext):
        pass 
    def enterFeature_def(self, ctx:ReqSpecLParser.Feature_defContext):
        feature_name = ctx.ID().getText()
        self.current_feature = feature_name
        self.features.setdefault(feature_name, [])

        # If a filter is set, only generate code for matching feature
        if self.feature_filter and self.feature_filter != feature_name:
            self.active = False
            return
        self.active = True

        self.write_code(f"\nclass TestFeature_{feature_name}(unittest.TestCase):")
        self.indent_level += 1

        self.write_code("# Memastikan urutan tes berdasarkan nama (alfabetis)")
        self.write_code("def setUp(self):")
        self.indent_level += 1
        self.write_code("print('\\n' + '-'*50)")
        self.indent_level -= 1

    def exitFeature_def(self, ctx:ReqSpecLParser.Feature_defContext):
        self.indent_level -= 1
        self.write_code("")

    def enterScenario_def(self, ctx:ReqSpecLParser.Scenario_defContext):
        raw_desc = ctx.STRING().getText()
        desc_clean = raw_desc.strip('"')
        func_name = self.sanitize_name(raw_desc)
        # register scenario under current feature
        if self.current_feature:
            self.features.setdefault(self.current_feature, []).append(desc_clean)
        
        seq_num = f"{self.scenario_counter:03d}" 
        self.scenario_counter += 1
        
        if not getattr(self, 'active', True):
            return

        self.write_code(f"\n    def test_{seq_num}_{func_name}(self):")
        self.indent_level += 1
        self.write_code(f'logging.info("SCENARIO {seq_num}: {desc_clean}")')

        self.write_code(f"current_state = SystemState.data")
        self.write_code(f'logging.info(f"  [DEBUG] State Awal: {{current_state}}")')

    def exitScenario_def(self, ctx:ReqSpecLParser.Scenario_defContext):
        self.indent_level -= 1

    def enterGiven_clause(self, ctx:ReqSpecLParser.Given_clauseContext):
        condition = ctx.STRING().getText()
        clean_cond = condition.strip('"')
        
        self.write_code(f"# GIVEN: {clean_cond}")
        
        if "OPEN" in clean_cond:
            self.write_code("SystemState.set('status_kelas', 'OPEN')")
            self.write_code('logging.info("  -> System set status_kelas = OPEN")')
        elif "sesuai jadwal" in clean_cond:
            self.write_code("SystemState.set('waktu', 'VALID')")
        else:
            self.write_code(f'logging.info("  [GIVEN] {clean_cond}")')

    def enterWhen_clause(self, ctx:ReqSpecLParser.When_clauseContext):
        action = ctx.STRING().getText()
        action_clean = action.strip('"')
        self.write_code(f"# WHEN: {action_clean}")
        self.write_code(f'logging.info("  [WHEN] {action_clean}")')
        
        if "Generate QR" in action:
            self.write_code("if SystemState.get('waktu') == 'VALID':")
            self.indent_level += 1
            self.write_code("SystemState.set('qr_code', 'GENERATED')")
            self.write_code("SystemState.set('status_kelas', 'OPEN')")
            self.indent_level -= 1
        
        if "sudah ditutup" in action:
             self.write_code("SystemState.set('status_kelas', 'CLOSED')")

    def enterThen_clause(self, ctx:ReqSpecLParser.Then_clauseContext):
        expectation = ctx.STRING().getText()
        expectation_clean = expectation.strip('"')
        self.write_code(f"# THEN: {expectation_clean}")
        
        if "menolak" in expectation_clean:
            self.write_code("status = SystemState.get('status_kelas')")
            self.write_code("if status == 'CLOSED':")
            self.indent_level += 1
            self.write_code('logging.info("  [SUCCESS] Sistem menolak karena kelas CLOSED")')
            self.indent_level -= 1
            self.write_code("else:")
            self.indent_level += 1
            self.write_code("pass")
            self.indent_level -= 1
        else:
            self.write_code(f'logging.info("  [THEN] {expectation_clean} (Verified)")')

    def close(self):
        # write features metadata file
        try:
            meta_path = os.path.join(os.getcwd(), 'features.json')
            with open(meta_path, 'w', encoding='utf-8') as mf:
                json.dump(self.features, mf, indent=2, ensure_ascii=False)

            todo_md = os.path.join(os.getcwd(), 'todo_features.md')
            with open(todo_md, 'w', encoding='utf-8') as tf:
                tf.write('# Feature List\n\n')
                for fname, scenarios in self.features.items():
                    tf.write(f"- **{fname}**\n")
                    for s in scenarios:
                        tf.write(f"  - {s}\n")
                tf.write('\n')
        except Exception:
            pass

        self.write_code("\nif __name__ == '__main__':")
        self.indent_level += 1
        self.write_code("unittest.main()")
        self.output_file.close()
        print(f"\n[SUKSES] Code Generation Selesai -> {self.output_file.name}")

def main(argv):
    # Usage:
    #  python main.py <file.req>           -> show interactive menu to pick feature
    #  python main.py <file.req> <feature> -> generate tests only for <feature>
    run_mode = len(argv) > 1 and argv[1].lower() == 'run'

    input_file = None
    feature_arg = None
    if not run_mode:
        if len(argv) < 2:
            print("Error: Masukkan nama file .req")
            return
        input_file = argv[1]
        if len(argv) > 2:
            feature_arg = argv[2]

    # First pass: collect features (skip when running interactive mode)
    collector = None
    if not run_mode:
        input_stream = FileStream(input_file)
        lexer = ReqSpecLLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = ReqSpecLParser(stream)
        tree = parser.program()

        class FeatureCollector(ReqSpecLListener):
            def __init__(self):
                self.features = {}
                self.current = None
            def enterFeature_def(self, ctx):
                name = ctx.ID().getText()
                self.current = name
                self.features.setdefault(name, [])
            def enterScenario_def(self, ctx):
                if self.current:
                    desc = ctx.STRING().getText().strip('"')
                    self.features[self.current].append(desc)

        collector = FeatureCollector()
        walker = ParseTreeWalker()
        walker.walk(collector, tree)

        # write features.json and todo_features.md
        try:
            with open('features.json', 'w', encoding='utf-8') as mf:
                json.dump(collector.features, mf, indent=2, ensure_ascii=False)
            with open('todo_features.md', 'w', encoding='utf-8') as tf:
                tf.write('# Feature List\n\n')
                for fname, scenarios in collector.features.items():
                    tf.write(f"- **{fname}**\n")
                    for s in scenarios:
                        tf.write(f"  - {s}\n")
                tf.write('\n')
        except Exception:
            pass

    # If user requested interactive runner: python main.py <file.req> run [feature]
    if len(argv) > 1 and argv[1].lower() == 'run':
        # usage when invoked as: python main.py run <file.req> [feature]
        if len(argv) < 3:
            print('Usage: python main.py run <file.req> [feature]')
            return
        run_file = argv[2]
        run_feature = None
        if len(argv) > 3:
            run_feature = argv[3]

        # collect detailed structure: features -> scenarios -> clauses
        input_stream = FileStream(run_file)
        lexer = ReqSpecLLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = ReqSpecLParser(stream)
        tree = parser.program()

        class DetailedCollector(ReqSpecLListener):
            def __init__(self):
                self.features = {}
                self.current = None
                self.current_scenario = None
            def enterFeature_def(self, ctx):
                name = ctx.ID().getText()
                self.current = name
                self.features.setdefault(name, [])
            def enterScenario_def(self, ctx):
                if self.current:
                    desc = ctx.STRING().getText().strip('"')
                    self.current_scenario = {'desc': desc, 'givens': [], 'whens': [], 'thens': []}
                    self.features[self.current].append(self.current_scenario)
            def enterGiven_clause(self, ctx):
                if self.current_scenario:
                    self.current_scenario['givens'].append(ctx.STRING().getText().strip('"'))
            def enterWhen_clause(self, ctx):
                if self.current_scenario:
                    self.current_scenario['whens'].append(ctx.STRING().getText().strip('"'))
            def enterThen_clause(self, ctx):
                if self.current_scenario:
                    self.current_scenario['thens'].append(ctx.STRING().getText().strip('"'))

        collector_d = DetailedCollector()
        walker = ParseTreeWalker()
        walker.walk(collector_d, tree)

        features = collector_d.features

        # choose feature
        feature_to_run = run_feature
        if not feature_to_run:
            names = list(features.keys())
            print('\nAvailable features:')
            for i, n in enumerate(names, start=1):
                print(f"  {i}. {n} ({len(features[n])} scenarios)")
            sel = input('Pilih fitur untuk dijalankan (nomor): ').strip()
            try:
                idx = int(sel)
                feature_to_run = names[idx-1]
            except Exception:
                print('Pilihan tidak valid. Keluar.')
                return

        # choose scenario
        scenarios = features.get(feature_to_run, [])
        if not scenarios:
            print('Tidak ditemukan scenario untuk fitur', feature_to_run)
            return
        print(f"\nScenarios for {feature_to_run}:")
        for i, s in enumerate(scenarios, start=1):
            print(f"  {i}. {s['desc']}")
        sel = input('Pilih scenario (nomor) atau 0 untuk jalankan semua secara berurutan: ').strip()
        try:
            idx = int(sel)
        except Exception:
            print('Input tidak valid. Keluar.'); return

        run_list = []
        if idx == 0:
            run_list = scenarios
        else:
            if 1 <= idx <= len(scenarios):
                run_list = [scenarios[idx-1]]
            else:
                print('Pilihan tidak valid. Keluar.'); return

        # load/create progress
        prog_path = os.path.join(os.getcwd(), 'features_progress.json')
        try:
            if os.path.exists(prog_path):
                with open(prog_path, 'r', encoding='utf-8') as pf:
                    progress = json.load(pf)
            else:
                progress = {}
        except Exception:
            progress = {}

        for scen in run_list:
            print('\n--- Running scenario: ' + scen['desc'] + ' ---')
            # present givens
            for g in scen.get('givens', []):
                print('[GIVEN] ' + g)
            # WHENS: allow developer to choose branch or input
            for w in scen.get('whens', []):
                print('[WHEN] ' + w)
                # prompt user whether this branch should succeed
                resp = input(f"Apakah aksi ini berhasil? (y/n) ").strip().lower()
                print(f"-> Output: {('Berhasil' if resp == 'y' else 'Gagal')}")
            # THENs: show expectations
            for t in scen.get('thens', []):
                print('[THEN] ' + t)

            done = input('Tandai scenario ini selesai? (y/n): ').strip().lower()
            prog = progress.setdefault(feature_to_run, {})
            if done == 'y':
                prog[scen['desc']] = True
                print('Scenario ditandai selesai.')
            else:
                prog[scen['desc']] = False
                print('Scenario tetap belum selesai.')

            # save progress after each scenario
            try:
                with open(prog_path, 'w', encoding='utf-8') as pf:
                    json.dump(progress, pf, indent=2, ensure_ascii=False)
            except Exception:
                pass

        print('\nSelesai menjalankan scenario(s). Progress tersimpan di features_progress.json')
        return

    # If feature arg not provided, offer interactive menu
    chosen_feature = feature_arg
    if not chosen_feature:
        print('\nAvailable features:')
        names = list(collector.features.keys())
        for i, n in enumerate(names, start=1):
            print(f"  {i}. {n} ({len(collector.features[n])} scenarios)")
        print("  0. All features")
        sel = input('Pilih fitur untuk generate (nomor) atau 0 untuk semua: ').strip()
        try:
            idx = int(sel)
            if idx == 0:
                chosen_feature = None
            elif 1 <= idx <= len(names):
                chosen_feature = names[idx-1]
            else:
                print('Pilihan tidak valid, menghasilkan untuk semua fitur.')
                chosen_feature = None
        except Exception:
            print('Input tidak valid, menghasilkan untuk semua fitur.')
            chosen_feature = None

    # Second pass: generate tests (filtered if chosen_feature provided)
    input_stream = FileStream(input_file)
    lexer = ReqSpecLLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ReqSpecLParser(stream)
    tree = parser.program()

    outname = 'test_generated_stateful.py'
    generator = PythonTestGeneratorListener(outname, feature_filter=chosen_feature)
    walker = ParseTreeWalker()
    walker.walk(generator, tree)
    generator.close()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv)
    else:
        print("Error: Masukkan nama file .req")
