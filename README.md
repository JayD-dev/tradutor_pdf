# 🛠️ Tradutor de PDF
**Este é um projeto em Python que permite traduzir o texto de um arquivo PDF para um idioma de destino e salvar o resultado em um novo arquivo PDF. O projeto utiliza as bibliotecas PyMuPDF para extrair o texto do PDF, googletrans para traduzir o texto e ReportLab para criar o novo PDF com o texto traduzido.**
-----------------------------------------------------------------------------------------------
## ⚙️Funcionalidades

1. Extrair texto de PDF: Extrai o texto de um arquivo PDF, preservando a estrutura por páginas.

2. Traduzir texto: Traduz o texto extraído para um idioma de destino (por exemplo, português, inglês, espanhol, etc.).

3. Criar novo PDF: Gera um novo arquivo PDF com o texto traduzido.

4. Interface gráfica: Oferece uma interface gráfica simples para selecionar o arquivo PDF, escolher o idioma de destino, selecionar a pasta de saída e definir o nome do arquivo traduzido.

5. Validação de nome de arquivo: Verifica se o nome do arquivo contém caracteres inválidos.

6. Barra de progresso: Exibe o progresso da tradução em tempo real.
-----------------------------------------------------------------------------------------------
## 📥Requisitos
Para executar este projeto, você precisará das seguintes bibliotecas Python:

- ** PyMuPDF (também conhecida como fitz)
- ** googletrans
- ** ReportLab
- ** tkinter (já vem instalado com o Python)
-----------------------------------------------------------------------------------------------
Você pode instalar as bibliotecas necessárias usando o pip:
```bash
pip install pymupdf googletrans==4.0.0-rc1 reportlab
```
## 🚀Como Usar
Execute o script:

1. Execute o script main.py em um ambiente Python.
2. Uma interface gráfica será aberta.
3. Selecione o arquivo PDF:
Clique em "Procurar" ao lado do campo "Selecione o arquivo PDF" e escolha um arquivo PDF.

5. Escolha o idioma de destino:
Selecione o idioma de destino na lista suspensa (por exemplo, "pt" para português).

6. Selecione a pasta de saída:
Clique em "Procurar" ao lado do campo "Selecione a pasta para salvar" e escolha uma pasta.

7. Digite o nome do arquivo:
Digite o nome do arquivo traduzido (sem extensão) no campo "Nome do arquivo".

8. Traduzir PDF:
Clique em "Traduzir PDF" para iniciar o processo.

A barra de progresso será atualizada durante a tradução.
Após a conclusão, o arquivo traduzido será salvo na pasta selecionada.
-----------------------------------------------------------------------------------------------
## 📝Exemplo de Uso
1. Selecione o arquivo artigo.pdf.
2. Escolha o idioma "pt" (português).
3. Selecione a pasta C:\Documentos.
4. Digite o nome artigo_traduzido.
5. Clique em "Traduzir PDF".
6. O arquivo será salvo como:

```bash
C:\Documentos\artigo_traduzido.pdf
Estrutura do Projeto
Copy
tradutor_pdf/
│
├── main.py                # Script principal do projeto
├── README.md              # Documentação do projeto
└── requirements.txt       # Lista de dependências (opcional)
```
-----------------------------------------------------------------------------------------------
## 🔧 Melhorias Futuras
* Adicionar suporte a mais idiomas.
* Melhorar a interface gráfica com mais funcionalidades.
* Adicionar suporte a PDFs com imagens e tabelas.
* Implementar uma barra de progresso mais detalhada.
* Adicionar opção para traduzir apenas partes específicas do PDF (por exemplo, apenas o resumo).
-----------------------------------------------------------------------------------------------
## 🤝 Contribuição
Contribuições são bem-vindas! Se você quiser melhorar este projeto, siga os passos abaixo:

* Faça um fork do repositório.
* Crie uma branch para sua feature 
```bash
git checkout -b feature/nova-feature.
```
* Commit suas mudanças 
```bash
git commit -m 'Adicionando nova feature'.
```
* Faça um push para a branch 
```bash
git push origin feature/nova-feature.
```
* Abra um Pull Request.

## 📜Licença
Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.


**Nome:** 👤 Janiele Nogueira
**GitHub:** ✍️ JayD-dev# tradutor_pdf
