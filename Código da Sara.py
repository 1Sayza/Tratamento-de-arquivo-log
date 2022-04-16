arquivo = input('Digite o nome do arquivo: ')
arquivoNome = arquivo + ".txt"
import csv
ip, data, hora, metodo, codigo, tamanho, sistema= [], [], [], [], [], [], []
try:
    with open(arquivoNome, "r") as arquivoLoad:
        for linha in arquivoLoad.readlines():
            ip.append(linha.split(' ',1)[0])
            data.append(((linha.split(' ')[3]).split('[')[1]).split(':',1)[0])
            hora.append(((linha.split(' ')[3]).split('[')[1]).split(':',1)[1])
            metodo.append((linha.split('"')[1]).split(' ',1)[0])
            codigo.append((linha.split('"',2)[2]).split(' ',2)[1])
        #normalização de requisições sem dados de tamanho
            if (linha.split('"',2)[2]).split(' ',3)[2] == "-":
                tamanho.append(0)
            else:
                tamanho.append((linha.split('"',2)[2]).split(' ',3)[2])
        #padronização de Sistemas:
            if 'Windows' in (linha.split('"',6)[5]):
                sistema.append('Windows')
            elif 'Linux' in (linha.split('"',6)[5]):
                sistema.append('Linux')
            elif 'Mac OS' in (linha.split('"',6)[5]):
                sistema.append('Mac OS')
            else:
                sistema.append('Outros')
except:
    print("Arquivo não encontrado")

#Criação do CSV
try:
    nome = arquivo + ".csv"
    with open(nome, 'w', newline='') as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow(["IP", "Data", "Hora","Metodo" ,"Codigo", "Tamanho", "Sistema"])
        for i in range(len(ip)):
            writer.writerow([ip[i], data[i], hora[i], metodo[i], codigo[i], tamanho[i], sistema[i]])
except:
    print("Arquivo não encontrado!")