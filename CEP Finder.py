from tkinter import *
import requests

class BuscadorCEP():
    def __init__(self,app):
        self.app = app
        app.title("CEP Finder")
        self.largura = 300
        self.altura = 200
        self.largura_monitor = self.app.winfo_screenwidth()
        self.altura_monitor = self.app.winfo_screenheight()
        self.posx = self.largura_monitor // 2 - self.largura// 2
        self.posy = self.altura_monitor // 2 - self.altura// 2
        self.app.geometry(f"{self.largura}x{self.altura}+{self.posx}+{self.posy}")
        self.app.resizable(False, False)

        self.widgets()

    def widgets(self):
        self.frame = Frame(self.app, bg="#383838")
        self.label_cep = Label(self.frame, text="CEP:",bg="#383838", fg="#FFFFFF", font="Arial 12 bold")
        self.entry = Entry(self.frame, width=15)
        self.botao = Button(self.frame, text="Pesquisar", font="Arial 7 bold",command=self.cep)
        self.label_endereco = Label(self.frame, text="",width=34, height=6)

        self.frame.place(relwidth=1, relheight=1)
        self.label_cep.place(relx=0.14, rely=0.05)
        self.entry.place(relx=0.30, rely=0.05)
        self.botao.place(relx=0.64, rely=0.05)
        self.label_endereco.place(relx=0.09, rely=0.3)

    def cep(self):
        try:
            cep = self.entry.get()
            response = requests.get("https://cep.awesomeapi.com.br/json/" + cep)
            data = response.json()
            self.label_endereco["text"] = f"Endereço:{data['address']}.\nBairro:{data['district']}.\nCidade:{data['city']}.\nEstado:{data['state']}.\nDDD:{data['ddd']}."
        except KeyError:
            self.label_endereco["text"] = "Endereço não encontrado.\nPor favor, tente outro."

if __name__ == "__main__":
    app = Tk()
    BuscadorCEP(app)
    app.mainloop()