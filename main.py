import sys
from antlr4 import *
from ReqSpecLLexer import ReqSpecLLexer
from ReqSpecLParser import ReqSpecLParser
from ReqSpecLListener import ReqSpecLListener

class SmartListener(ReqSpecLListener):
    def __init__(self):
        self.context_vars = {} 
        self.seen_scenarios = set() 
        self.current_feature = ""

    def enterVar_def(self, ctx):
        var_name = ctx.ID().getText()
        var_value = ctx.STRING().getText().replace('"', '')
        self.context_vars[var_name] = var_value
        print(f" [MEMORY] Menyimpan Context: {var_name}")

    def enterEndpoint_def(self, ctx):
        api_name = ctx.ID().getText()
        method = ctx.method().getText()
        url = ctx.STRING().getText()
        print(f" [API] Endpoint Terdaftar: {api_name} [{method} {url}]")

    def enterFeature_def(self, ctx):
        self.current_feature = ctx.ID().getText()
        print(f"\n [FEATURE] Memeriksa Fitur: {self.current_feature}")
        print("=" * 60)

    def enterScenario_def(self, ctx):
        raw_desc = ctx.STRING().getText()
        
        unique_key = f"{self.current_feature}_{raw_desc}"
        if unique_key in self.seen_scenarios:
            print(f" [CRITICAL ERROR] Skenario Duplikat Terdeteksi: {raw_desc}")
            print("   Sistem menolak redundansi dalam satu fitur!")
            sys.exit(1) 
        else:
            self.seen_scenarios.add(unique_key)
            print(f"   Test Case: {raw_desc}")

    def enterGiven_clause(self, ctx):
        if ctx.STRING():
            text = ctx.STRING().getText()
        elif ctx.ID():
            var_name = ctx.ID().getText()
            if var_name in self.context_vars:
                text = f"[{var_name}] {self.context_vars[var_name]}"
            else:
                print(f" [ERROR] Variabel '{var_name}' tidak ditemukan!")
                text = "UNDEFINED"
        
        print(f"      Given: {text}")

    def exitThen_clause(self, ctx):
        print(f"      Expect: {ctx.STRING().getText()}")

    def exitError_clause(self, ctx):
        print(f"      CAUGHT: {ctx.STRING().getText()} (Negative Test)")

def main(argv):
    input_file = argv[1]
    input_stream = FileStream(input_file)
    lexer = ReqSpecLLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ReqSpecLParser(stream)
    tree = parser.program()

    if parser.getNumberOfSyntaxErrors() > 0:
        print(" Gagal Parsing: Cek Syntax Error di atas.")
        return

    printer = SmartListener()
    walker = ParseTreeWalker()
    
    print(f"--- START VALIDATION: {input_file} ---\n")
    walker.walk(printer, tree) 
    print("\n--- VALIDATION FINISHED ---")

if __name__ == '__main__':
    main(sys.argv)