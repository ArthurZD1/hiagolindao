#coding utf-8
def ComissaoSalario():
    nome= input('entre com o nome do vendendor: ')
    salariofixo= float(input('informe o salario: '))
    Vendas=float(input('informe o total de vendas: '))
    Comissao= 0.15*Vendas
    Totalreceber= salariofixo+Comissao
    return nome,Comissao,Totalreceber






if __name__=='__main__':
    nome, Comissao,Totalreceber=ComissaoSalario()
    strg= '{0} obteve RS {1:.2f} de comissao e vai receber {2:.2f}'.format(nome,Comissao,Totalreceber)
    print(strg)

    