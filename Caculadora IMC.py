from tkinter import *

# Criando uma variavel para iden janela

root = Tk()
class imc():
    def __init__(self):
        self.root = root
        self.janela()
        self.desenho()
        # criando o Loop
        root.mainloop()
    def janela(self):
        self.root.title("Calculadora do índice de massa corporal (IMC)")
        self.root.configure(background= '#00008b')
        self.root.geometry("500x200")
        self.root.resizable(True, True)
    def desenho(self):
        self.quilos = DoubleVar()
        self.lb_quilos = Label(text='Peso (em Kg)',
                                       font=('Verdana', '10', 'bold'),
                                       bg='#D3D3D3', fg='#000000')
        self.lb_quilos.place(relx=0.2, rely=0.05, relwidth=0.35,
                                     relheight=0.1)
        self.input_quilos = Entry(textvariable=self.quilos)
        self.input_quilos.place(relx=0.6, rely=0.05, relwidth=0.2,
                                        relheight=0.1)

        self.altura = DoubleVar()
        self.lb_altura = Label(text='Altura (em M) ',
                                       font=('Verdana', '10', 'bold'),
                                    bg='#D3D3D3', fg='#000000')
        self.lb_altura.place(relx=0.2, rely=0.2,
                                  relwidth=0.35, relheight=0.1)
        self.input_altura = Entry(textvariable=self.altura)
        self.input_altura.place(relx=0.6, rely=0.2,
                                     relwidth=0.2, relheight=0.1)

        self.bt_calcular = Button( text='Calcular o IMC',
                                bg='#808080', fg='#F8F8FF',
                                   font=("verdana", 10, "bold"),
                                   command = self.butaoclick1)
        self.bt_calcular.place(relx=0.3, rely=0.4, relwidth=0.4,
                               relheight=0.17)
        # Resultado
        self.imcfinal = StringVar()
        self.imcfinal1 = Label(textvariable=self.imcfinal)

        self.resultado1 = Label(textvariable=self.imcfinal)
        self.resultado1.place(relx=0.1, rely=0.65, relwidth=0.8,relheight=0.2)

    def butaoclick1(self):
        kg = self.quilos.get()
        mt = self.altura.get()
        mt2= mt*mt
        imc =kg/mt2
        imcaredondado = round(imc,2)
        if imcaredondado <= 16.99:
            final = 'O seu IMC é de '+ str(imcaredondado)\
                    + '.'+'\nPeso muito abaixo do peso!'
        elif imcaredondado >=17 and imcaredondado <= 18.49 :
            final = 'O seu IMC é de ' + str(imcaredondado)\
                    + '.'+ '\nPesoabaixo do peso!'
        elif imcaredondado >=18.5 and imcaredondado <= 24.99:
            final = 'O seu IMC é de ' + str(imcaredondado) \
                    + '.' + '\nPeso normal!'
        elif imcaredondado >= 25 and imcaredondado <= 29.99:
            final = 'O seu IMC é de ' + str(imcaredondado) \
                    + '.' + '\nAcima do peso!'
        elif imcaredondado >= 30 and imcaredondado <= 34.99:
            final = 'O seu IMC é de ' + str(imcaredondado) \
                    + '.' + '\nObesidade Grau I!'
        elif imcaredondado >= 35 and imcaredondado <= 40:
            final = 'O seu IMC é de ' + str(imcaredondado) \
                    + '.' + '\nObesidade Grau II!'
        else:
            final = 'O seu IMC é de ' + str(imcaredondado) \
                    + '.' + '\nObesidade Grau III!'
        return self.imcfinal.set(final)

imc()