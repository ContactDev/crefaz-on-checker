# # import datetime
# # from hashlib import new
# from botcity.core import DesktopBot
# import pandas as pd

# class Bot(DesktopBot):
#     def action(self, execution=None):

#         tabela = pd.read_excel(str(r'C:\Users\efranca\Desktop\checker\crefaz-on-checker\crefazOnChecker\Rech_Neg_Sist_29_11_2022_CrefazOn.xlsx'), dtype=str)

#         self.browse("https://crefazon.com.br/")

#         for i in tabela.index:

#             cpf = tabela.loc[i,'CPF']
#             nome = tabela.loc[i,'Nome']
#             data_nasc = tabela.loc[i,'Data de Nascimento']
#             new_data = str(pd.to_datetime(data_nasc, dayfirst=True).date())
#             splited = new_data.split('-')
#             data = splited[2]+splited[1]+splited[0]
#             telefone = tabela.loc[i,'Telefone']
#             classificacao = tabela.loc[i,'Classificação']
#             cep = tabela.loc[i,'CEP']

#             print('===============================')
#             print(f'CPF: {cpf}')
#             print(f'Nome: {nome}')
#             print(f'Data de Nascimento: {new_data}') 
#             print(f'Data de Nascimento convertida: {splited[2]+splited[1]+splited[0]}')
#             print(f'Telefone: {telefone}')
#             print(f'Classificação: {classificacao}')
#             print(f'CEP: {cep}')
#             print('===============================')
#             self.wait(2000)            

#             if self.find( "creditoFind", matching=0.97, waiting_time=60000):
#                 self.not_found("creditoFind")          
#             self.click()
#             self.wait(100)
            
#             if self.find( "propostaFind", matching=0.97, waiting_time=60000):
#                 self.not_found("propostaFind")
#             self.click()
#             self.wait(100)

#             if self.find( "newProposalFind", matching=0.97, waiting_time=60000):
#                 self.not_found("newProposalFind")
#             self.click()
#             self.wait(100)
            
#             if self.find( "firstParameter", matching=0.97, waiting_time=1000):
#                 self.not_found("firstParameter")
#                 self.click_relative(17, 42)
#                 self.paste(cpf)
#                 self.tab()
#                 self.wait(500)
#                 if self.find( "CPFinvalido", matching=0.97, waiting_time=1000):
#                     self.not_found("CPFinvalido")
#                     self.key_f5()
#                     continue
#                 if self.find( "ofertasFind", matching=0.97, waiting_time=3000):
#                     self.not_found("ofertasFind")
#                     continue                               
#                 #     fpc = cpf
#                 #     name = nome
#                 #     date = data
#                 #     phone = telefone
#                 #     classification = classificacao
#                 #     pec = cep
#                 #     if self.find( "planilhaFind", matching=0.97, waiting_time=250):
#                 #         self.not_found("planilhaFind")
#                 #     self.click()
#                 #     self.wait(50)
#                 #     self.paste(fpc)
#                 #     self.wait(50)
#                 #     self.tab()
#                 #     self.paste(name)
#                 #     self.wait(50)
#                 #     self.tab()
#                 #     self.paste(date)
#                 #     self.wait(50)
#                 #     self.tab()
#                 #     self.paste(phone)
#                 #     self.wait(50)
#                 #     self.tab()
#                 #     self.paste(classification)
#                 #     self.wait(50)
#                 #     self.tab()
#                 #     self.paste(pec)
#                 #     self.wait(50)
#                 #     self.enter()
#                 #     if self.find( "secondChromeFind", matching=0.97, waiting_time=2000):
#                 #         self.not_found("secondChromeFind")                    
#                 #     self.click()                
#                 #     self.key_f5()
#                 #     continue


#             # if self.find( "proposalGoing", matching=0.97, waiting_time=1000):
#             #     self.not_found("proposalGoing")
#             #     self.wait(250)
#             #     self.enter()
#             #     self.key_f5()
#             #     continue

#             if self.find( "nameAvailable", matching=0.97, waiting_time=3000):
#                 self.not_found("nameAvailable")
#             self.control_a()
#             self.paste(nome)
#             self.tab()  
#             self.wait(100)
#             if self.find("nomeINVALIDO", matching=0.97, waiting_time=1000):
#                 self.not_found("nomeINVALIDO")
#                 self.key_f5()
#                 continue
#             self.control_a()
#             self.paste(data)
#             self.tab()
#             self.wait(100)
#             if self.find( "dataINVALIDA", matching=0.97, waiting_time=1000):
#                 self.not_found("dataINVALIDA")
#                 self.key_f5()
#                 continue
#             self.control_a()
#             self.paste(telefone)
#             self.tab()
#             self.wait(100)
#             if self.find( "telefoneINVALIDO", matching=0.97, waiting_time=1000):
#                 self.not_found("telefoneINVALIDO")
#                 self.key_f5()
#                 continue
#             self.control_a()
#             self.paste(classificacao)
#             self.wait(100)
#             self.enter()
#             self.tab()
#             self.control_a()
#             self.paste(cep)
#             self.tab()
#             self.wait(100)
#             if self.find( "CEPinvalido", matching=0.97, waiting_time=1000):
#                 self.not_found("CEPinvalido")
#                 self.key_f5()
#                 continue
#             self.wait(1000)
#             self.enter()
            
#             if self.find( "deniedFind", matching=0.97, waiting_time=15000):
#                 self.not_found("deniedFind")
#                 self.enter()
#                 self.wait(100)
#                 self.key_f5()
#                 continue
                
#             # if self.find( "offerFind", matching=0.97, waiting_time=60000):
#             #     self.not_found("offerFind")                            
#             #     fpc = cpf
#             #     name = nome
#             #     date = data
#             #     phone = telefone
#             #     classification = classificacao
#             #     pec = cep
#             #     if self.find( "planilhaFind", matching=0.97, waiting_time=1000):
#             #         self.not_found("planilhaFind")
#             #     self.click()
#             #     self.wait(50)
#             #     self.paste(fpc)
#             #     self.wait(50)
#             #     self.tab()
#             #     self.paste(name)
#             #     self.wait(50)
#             #     self.tab()
#             #     self.paste(date)
#             #     self.wait(50)
#             #     self.tab()
#             #     self.paste(phone)
#             #     self.wait(50)
#             #     self.tab()
#             #     self.paste(classification)
#             #     self.wait(50)
#             #     self.tab()
#             #     self.paste(pec)
#             #     self.wait(50)
#             #     self.enter()
#             #     self.wait(100)
#             #     if self.find( "secondChromeFind", matching=0.97, waiting_time=1000):
#             #         self.not_found("secondChromeFind")              
#             #     self.click()                
#             #     self.wait(100)
#             #     continue
        
#         else:
            
#             print('===============')
#             print('BUSCA ENCERRADA')
#             print('===============')
            
#     def not_found(self, label):
#         print(f"Element found: {label}")

# if __name__ == '__main__':
#     Bot.main()
