lista_tarefas = []

def adicionar_tarefa(lista_tarefas, descricao, status, prioridade):
    #status: ("pendente", "em andamento", "concluída")
    #prioridade: ("alta", "média", "baixa")
    if lista_tarefas:
        id = max(tarefa["id"] for tarefa in lista_tarefas)+1        
    else:
        id = 1
    nova_tarefa = {"id":id,"descricao":descricao, "status":status, "prioridade":prioridade}
    lista_tarefas.append(nova_tarefa)

def visualizar_tarefas(lista_tarefas):
    for tarefa in lista_tarefas:
        print(f'ID: {tarefa["id"]}\nDescrição: {tarefa["descricao"]} | Status: {tarefa["status"]} | Prioridade: {tarefa["prioridade"]}\n{'=~'*40}')

def filtrar_tarefas(lista_tarefas, status=None, prioridade=None):
    if status is None and prioridade is None:
        visualizar_tarefas(lista_tarefas)
    
    elif status is None:
        print(f"{'='*100}\nRelatório de Tarefas com o filtro: {prioridade}\n{'='*100}")
        lista_filtrada = [tarefa for tarefa in lista_tarefas if tarefa['prioridade'] == prioridade]
        visualizar_tarefas(lista_filtrada)
    
    elif prioridade is None:
        print(f"{'='*100}\nRelatório de Tarefas com o filtro: {status}\n{'='*100}")
        lista_filtrada = [tarefa for tarefa in lista_tarefas if tarefa['status'] == status]
        visualizar_tarefas(lista_filtrada)
        
    else:
        print(f"{'='*100}\nRelatório de Tarefas com os filtros: {status} e {prioridade}\n{'='*100}")
        lista_filtrada = [tarefa for tarefa in lista_tarefas if tarefa["status"] == status and tarefa['prioridade'] == prioridade]
        visualizar_tarefas(lista_filtrada)
        

adicionar_tarefa(lista_tarefas,"Tarefa 1", "Em andamento", "Alta")
adicionar_tarefa(lista_tarefas,"Tarefa 2", "Pendente", "Média")
adicionar_tarefa(lista_tarefas,"Tarefa 3", "Concluída", "Alta")
adicionar_tarefa(lista_tarefas,"Tarefa 4", "Concluída", "Baixa")
adicionar_tarefa(lista_tarefas,"Tarefa 5", "Pendente", "Baixa")

#filtrar_tarefas(lista_tarefas)
#filtrar_tarefas(lista_tarefas, "Pendente")
#filtrar_tarefas(lista_tarefas, "Concluída", "Alta")
filtrar_tarefas(lista_tarefas, prioridade="Alta")