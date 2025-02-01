import fitz #PyMuPDF
from googletrans import Translator
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os
import re
from tkinter import Tk, Label, Button, filedialog, messagebox, ttk, Entry

#Funções do tradutor do PDF
def extract_text_from_pdf(pdf_path):
    """
    Extrai texto de um PDF, preservando a estrutura de páginas 
    
    """
    doc = fitz.open(pdf_path) #abre o arquivo PDF
    text = ""

    for page_num in range(len(doc)): #itera sobre cada página
        page = doc.load_page(page_num) #carrega a página atual
        text += f"---Página {page_num + 1} ---\n" #adiciona um marcador de página
        text += page.get_text() + "\n\n" #Extrai o texto da página
    return text

def translate_text(text, dest_language='pt'):
    """
    Traduz o texto para o idioma de destino 
    """

    translator = Translator()
    try:
        max_chars = 5000 #Limute de caracteres por requisição
        parts = [text[i:i + max_chars] for i in range (0, len(text), max_chars)] #Divide o texto 
        translated_text = ""

        for part in parts:
            translation = translator.translate(part, dest=dest_language) #Traduz cada parte
            translated_text += translation.text + " " #Concatena o texto traduzido
        return translated_text.strip() #Remove espaços extras
    except Exception as e:
        print(f"Erro na tradução: {e}")
        return text #Retorna o texto original em caso de erro
    

def create_pdf_with_text(text, output_pdf_path):
    """
    Cria um novo PDF com o texto traduzido.
    """

    c = canvas.Canvas(output_pdf_path, pagesize=letter)
    width, height = letter
    c.setFont("Helvetica", 12)

    lines = text.split('\n') #Divide o texto em linhas 
    y_position = height - 40 #Define a posição inicial Y (topo da página)
    for line in lines:
        if y_position < 40: #Verifica se a posição Y chegou ao final da página
            c.showPage() #Cria uma nova página 
            y_position = height - 40 #Reinicia a posição Y
        c.drawString(40, y_position, line) #Escreve a linha no PDF
        y_position -= 15 #Move para a próxima linha (espaçamento)
 
    c.save() #Salva o PDF


#Funções da Interface gráfica
def selecionar_arquivo():
    """
    Abre uma janela para selecionar o arquivo PDF.
    """

    arquivo = filedialog.askopenfilename(
        title="Selecione um arquivo PDF",
        filetypes=[("Arquivos PDF", "*.pdf")]
    )
    if arquivo:
        entrada_arquivo.delete(0, "end")
        entrada_arquivo.insert(0, arquivo)

def selecionar_pasta():
    """
    Abre uma janela para selecionar a pasta onde o arquivo será salvo.
    """
    pasta = filedialog.askdirectory(title="Selecione a pasta para salvar o arquivo")
    if pasta:
        entrada_pasta.delete(0, "end")
        entrada_pasta.insert(0, pasta)


def validar_nome_arquivo(nome):
    """
    Verifica se o nome do arquivo contém caracteres inválidos
    """

    caracteres_invalidos = r'[\/:*?"<>|]' #Expressão regular para caracteres inválidos
    if re.search(caracteres_invalidos, nome):
        return False
    return True


def traduzir_pdf():
    """
    Executa a tradução do PDF com base nas escolhas do usuário.
    """
    pdf_path = entrada_arquivo.get()
    dest_language = combo_idioma.get()
    pasta_salvar = entrada_pasta.get()
    nome_arquivo = entrada_nome.get()


    if not pdf_path:
        messagebox.showerror("Erro", "Selecione um arquivo PDF!")
        return

    #Verifica se o arquivo PDF existe
    if not os.path.exists(pdf_path):
        print(f"Erro: O arquivo '{pdf_path}' não foi encontrado.")
        return #Encerra a função se o arquivo não existir

    
    if not pasta_salvar:
        messagebox.showerror("Erro", "Selecione uma pasta para salvar o arquivo")
        return

    if not nome_arquivo:
        messagebox.showerror("Erro", "Digite um nome para o arquivo")
        return

    if not validar_nome_arquivo(nome_arquivo):
        messagebox.showerror("Erro", "O nome do arquivo contém caracteres inválidos (\\/:*?\"<>|).")
        return

    try:

        #Atualiza a barra de progresso 
        barra_progresso['value'] = 0
        janela.update_idletasks()

        #Extrai o texto do PDF
        print("Extraindo texto do PDF...")
        text = extract_text_from_pdf(pdf_path)
        barra_progresso['value'] = 33 #33% completo
        janela.update_idletasks()

        #Traduz o texto
        print("Traduzindo texto...")
        translated_text = translate_text(text, dest_language)
        if translated_text is None: #Verifica se a tradução falhou
            messagebox.showerror("Erro", "Falha na tradução. Verifique sua conexão com a internet.")
            return
        barra_progresso['value'] = 66 #66% completo
        janela.update_idletasks()


        #Define o caminho completo do arquivo de saída
        output_pdf_path = os.path.join(pasta_salvar, f"{nome_arquivo}.pdf")
    
        #Salva o PDF traduzido
        print("Criando PDF traduzido...")
        create_pdf_with_text(translated_text, output_pdf_path)
        barra_progresso['value'] = 100 #100% completo
        janela.update_idletasks()


        #Exibe mensagem de sucesso
        messagebox.showinfo("Sucesso", f"PDF traduzido salvo em:\n{output_pdf_path}")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro durante a tradução:\n{e}")
    finally:
        #Reseta a barra de progresso
        barra_progresso['value'] = 0

#Configuração da interface gráfica
janela = Tk()
janela.title("Tradutor de PDF")
janela.geometry("600x300")

#Componetes da interface
Label(janela, text="Selecione o arquivo PDF:").grid(row=0, column=0, padx=10, pady=10)
entrada_arquivo = ttk.Entry(janela, width=40)
entrada_arquivo.grid(row=0, column=1, padx=10, pady=10)
Button(janela, text="Procurar", command=selecionar_arquivo).grid(row=0, column=2, padx=10, pady=10)

Label(janela, text="Selecione o idioma de destino:").grid(row=1, column=0, padx=10, pady=10)
combo_idioma = ttk.Combobox(janela, values=["pt", "en", "es", "fr", "de"], state="readonly")
combo_idioma.set("pt")  # Define o valor padrão
combo_idioma.grid(row=1, column=1, padx=10, pady=10)

Label(janela, text="Selecione a pasta para salvar:").grid(row=2, column=0, padx=10, pady=10)
entrada_pasta = ttk.Entry(janela, width=40)
entrada_pasta.grid(row=2, column=1, padx=10, pady=10)
Button(janela, text="Procurar", command=selecionar_pasta).grid(row=2, column=2, padx=10, pady=10)

Label(janela, text="Nome do arquivo (sem extensão):").grid(row=3, column=0, padx=10, pady=10)
entrada_nome = ttk.Entry(janela, width=40)
entrada_nome.grid(row=3, column=1, padx=10, pady=10)

# Barra de progresso
barra_progresso = ttk.Progressbar(janela, orient="horizontal", length=400, mode="determinate")
barra_progresso.grid(row=4, column=0, columnspan=3, padx=10, pady=20)

Button(janela, text="Traduzir PDF", command=traduzir_pdf).grid(row=5, column=0, columnspan=3, padx=10, pady=10)

#Inicia a interface
janela.mainloop()
