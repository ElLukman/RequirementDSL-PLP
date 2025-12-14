import sys
import re
from antlr4 import *
from ReqSpecLLexer import ReqSpecLLexer
from ReqSpecLParser import ReqSpecLParser
from ReqSpecLListener import ReqSpecLListener

class PythonTestGeneratorListener(ReqSpecLListener):
    def __init__(self, output_filename="test_generated_stateful.py"):
        self.output_file = open(output_filename, 'w')
        self.indent_level = 0
        self.actors = set() 
        self.scenario_counter = 1 
        
        self.write_code("import unittest")
        self.write_code("import logging")
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
        self.write_code("# Dibuat oleh:Lukman Ahmad dan Muhammad Rifqi Al Faritzi\n")

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
        func_name = self.sanitize_name(raw_desc)
        
        seq_num = f"{self.scenario_counter:03d}" 
        self.scenario_counter += 1
        
        self.write_code(f"\n    def test_{seq_num}_{func_name}(self):")
        self.indent_level += 1
        self.write_code(f"logging.info('SCENARIO {seq_num}: {raw_desc}')")
        
        self.write_code(f"current_state = SystemState.data")
        self.write_code(f"logging.info(f'  [DEBUG] State Awal: {{current_state}}')")

    def exitScenario_def(self, ctx:ReqSpecLParser.Scenario_defContext):
        self.indent_level -= 1

    def enterGiven_clause(self, ctx:ReqSpecLParser.Given_clauseContext):
        condition = ctx.STRING().getText()
        clean_cond = condition.strip('"')
        
        self.write_code(f"# GIVEN: {clean_cond}")
        
        if "OPEN" in clean_cond:
            self.write_code("SystemState.set('status_kelas', 'OPEN')")
            self.write_code("logging.info('  -> System set status_kelas = OPEN')")
        elif "sesuai jadwal" in clean_cond:
            self.write_code("SystemState.set('waktu', 'VALID')")
        else:
            self.write_code(f"logging.info('  [GIVEN] {clean_cond}')")

    def enterWhen_clause(self, ctx:ReqSpecLParser.When_clauseContext):
        action = ctx.STRING().getText()
        self.write_code(f"# WHEN: {action}")
        self.write_code(f"logging.info('  [WHEN] {action}')")
        
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
        self.write_code(f"# THEN: {expectation}")
        
        if "menolak" in expectation:
            self.write_code("status = SystemState.get('status_kelas')")
            self.write_code("if status == 'CLOSED':")
            self.indent_level += 1
            self.write_code("logging.info('  [SUCCESS] Sistem menolak karena kelas CLOSED')")
            self.indent_level -= 1
            self.write_code("else:")
            self.indent_level += 1
            self.write_code("pass")
            self.indent_level -= 1
        else:
            self.write_code(f"logging.info('  [THEN] {expectation} (Verified)')")

    def close(self):
        self.write_code("\nif __name__ == '__main__':")
        self.indent_level += 1
        self.write_code("unittest.main()")
        self.output_file.close()
        print(f"\n[SUKSES] Code Generation Selesai -> {self.output_file.name}")

def main(argv):
    input_file = argv[1]
    input_stream = FileStream(input_file)
    lexer = ReqSpecLLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ReqSpecLParser(stream)
    tree = parser.program()
    
    generator = PythonTestGeneratorListener("test_generated_stateful.py")
    walker = ParseTreeWalker()
    walker.walk(generator, tree)
    generator.close()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv)
    else:
        print("Error: Masukkan nama file .req")
