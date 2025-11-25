import sys
from antlr4 import *
from ReqSpecLLexer import ReqSpecLLexer
from ReqSpecLParser import ReqSpecLParser
from ReqSpecLListener import ReqSpecLListener # Kita panggil Listener bawaan

# Ini adalah 'Mata-mata' yang akan mencuri data saat Parser membaca file
class PrinterListener(ReqSpecLListener):
    def enterFeature_def(self, ctx):
        # Setiap kali ketemu "def_feature", ambil namanya
        nama_fitur = ctx.ID().getText()
        print(f"\n[SISTEM] Mendeteksi Fitur Baru: {nama_fitur}")
        print("=" * 40)

    def enterScenario_def(self, ctx):
        # Setiap kali ketemu "scenario", ambil teksnya
        # ctx.STRING() mengambil teks "...", getText() menjadikannya string
        deskripsi = ctx.STRING().getText()
        print(f"  --> Menguji Skenario: {deskripsi}")

    def exitThen_clause(self, ctx):
         # Ambil ekspektasi output
         hasil = ctx.STRING().getText()
         print(f"     ✅ Harapan Output: {hasil}")

def main(argv):
    input_file = argv[1]
    input_stream = FileStream(input_file)
    lexer = ReqSpecLLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ReqSpecLParser(stream)
    
    # Buat tree
    tree = parser.program()

    # --- BAGIAN AJAIBNYA ---
    # Kita tempelkan 'Mata-mata' (Listener) ke proses parsing
    printer = PrinterListener()
    walker = ParseTreeWalker()
    
    print(f"MEMPROSES FILE: {input_file}...\n")
    walker.walk(printer, tree) # Jalankan mata-mata!

if __name__ == '__main__':
    main(sys.argv)