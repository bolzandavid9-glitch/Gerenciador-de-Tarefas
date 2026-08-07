import json
import os

class lista_de_tarefas:
    def __init__ (self, tarefas):
        self.tarefas = tarefas
        self.dic= {}

    def mostrar_tarefas(self):
        print("todas as suas tarefas")
        with open(dataB, 'r',encoding="utf=8") as tarefas_json:
            tarefas = json.load(tarefas_json)
        for tarefa ,prazo in tarefas.items():
            print(f"{tarefa} até as {prazo}")


    def adicionar_tarefa(self, tarefa, hora, data):
        tarefas_json = open(dataB, 'w', encoding="utf=8")
        json.dump(self.dic, tarefas_json, indent=4, ensure_ascii=False)
        if tarefa not in tarefas:
            x = data.split('/')
            dia = x[0]
            mes = x[1]
            ano = x[2]
            dia_de_conclusao = f"{hora}: {dia}/{mes}/{ano}"
            self.dic.update({tarefa: dia_de_conclusao})
            tarefas_json = open(dataB, 'a', encoding="utf=8")
            json.dump(self.dic, tarefas_json, indent=4, ensure_ascii=False)

            print("tarefa adicionada")
        else:
            print("essa tarefa ja foi adicionada")
        tarefas_json.close()

    def tirar_tarefa(self, tarefa):
        tarefa_json = open(dataB, 'r', encoding="utf=8")
        arquivo = json.load(tarefa_json)
        tarefa_json.close()

        if tarefa in arquivo:
            del arquivo[tarefa]
            print("tarefa retirada")
        else:
            print("não tem essa tarefa na lista")

        ar = open(dataB, 'w', encoding="utf=8")
        json.dump(arquivo, ar, indent=4, ensure_ascii=False)
        ar.close()
        

    def editar_tarefa(self, tarefa, tarefa_nova):
        tarefa_json = open(dataB, 'r', encoding="utf=8")
        arquivo = json.load(tarefa_json)
        tarefa_json.close()
        if tarefa in arquivo:
            arquivo[tarefa_nova] = arquivo[tarefa]
            del arquivo[tarefa]
            print("tarefa editada")
        else:
            print("A tarefa antiga não foi encontrada")

        ar = open(dataB, 'w', encoding="utf=8")
        json.dump(arquivo, ar, indent=4, ensure_ascii=False)
        ar.close()

    def editar_data_conclusao(self, tarefa, data, hora):
        tarefa_json = open(dataB, 'r', encoding="utf=8")
        arquivo = json.load(tarefa_json)
        tarefa_json.close()
        x = data.split('/')
        dia= x[0]
        mes= x[1]
        ano= x[2]
        data_nova = f"{hora}: {dia}/{mes}/{ano}"
        if tarefa in arquivo:
            arquivo[tarefa] = data_nova
            print("data editada com sucesso")
        else:
            print("tarefa não encontrada")

        ar = open(dataB, 'w', encoding="utf=8")
        json.dump(arquivo, ar, indent=4, ensure_ascii=False)
        ar.close()

    def mostra_por_data(self, data_tarefa):
        tarefa_json = open(dataB, 'r', encoding="utf=8")
        arquivo = json.load(tarefa_json)
        tarefa_json.close()

        encontrou = False
        print(f"Tarefas agendadas para o dia {data_tarefa}")

        for tarefa, data in arquivo.items():
            if data == data_tarefa:
                print(f"-{tarefa}")
                encontrou = True
        if not encontrou:
            print("nenhuma tarefa encontrada nessa data")
        



def main():
    while(True):
        print(f"lista de tarefas")
        choice = """
        _____________________________________
        |                                   |
        |   1.Mostrar tarefas               |
        |   2.Adicionar tarefa              |
        |   3.tirar tarefa                  |
        |   4.Editar tarefa                 |
        |   5.Editar data                   |
        |   6.Mostrar tarefas na data       |
        |___________________________________|
        """
    
        print(choice)
    
        entrada = input("precione S para sair e C para continuar: ")
        if entrada == 'C':
            escolha_user = (input("seleciona uma opção: "))
            if escolha_user == '1':
                Lista_de_tarefas.mostrar_tarefas()
    
            elif escolha_user == '2':
                tarefa = input("digite a tarefa que deseja fazer: ")
                hora = input("hora maxima que a terefa deve ser realizada: ")
                data = input("digite a data separada por /: ")
                Lista_de_tarefas.adicionar_tarefa(tarefa, hora, data)
    
            elif escolha_user == '3':
                tarefa = input("digite uma tarefa para remove-la: ")
                Lista_de_tarefas.tirar_tarefa(tarefa)

            elif escolha_user == '4':
                tarefa = input("digite a tarefa que deseja editar: ")
                tarefa_nova = input("digite a tarefa editada")
                Lista_de_tarefas.editar_tarefa(tarefa, tarefa_nova)

            elif escolha_user == '5':
                tarefa = input("digite a tarefa que deseja adiar: ")
                hora = input("hora maxima que a terefa deve ser realizada: ")
                data = input("digite a nova data separada por /: ")
                Lista_de_tarefas.editar_data_conclusao(tarefa, data, hora)

            elif escolha_user == '6':
                data_tarefa = input("digite a data que deseja ver as tarefas: ")
                Lista_de_tarefas.mostra_por_data(data_tarefa)

            else:
                print("selecione um opção valida")
    
        elif entrada == 'S':
            break
    
        else:
            print("selecione um opção valida")

if __name__ == '__main__':
    tarefas = []
    pasta_atual = os.path.dirname(os.path.abspath(__file__))
    dataB = os.path.join(pasta_atual, "tarefas.json")
         
    with open(dataB, "r", encoding="utf-8") as tarefas_json:
        Lista_de_tarefas = json.load(tarefas_json)
Lista_de_tarefas = lista_de_tarefas(tarefas)
main()
