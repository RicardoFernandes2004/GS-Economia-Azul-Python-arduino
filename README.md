Detecção de Nível de Petróleo

Equipe
    Ricardo Fernandes de Aquino (RM554597);
    Kauã Soares Guimarães (RM559044);
    Dayana Ticona Quispe (RM558023);
Requisitos
    Python 3.11.7
    Dispositivo leitor de petróleo em Arduino (simulação feita com potenciômetro)
Dependências
Instale as seguintes bibliotecas antes de executar o projeto:

    pyserial
    time
    os
    pandas
    matplotlib
Modo de Uso

Inicie o aplicativo pelo main.py.
No menu, escolha uma das três opções:
Opção 1
O aplicativo realizará 101 medições com base na serial do Arduino e armazenará esses dados em um arquivo .csv. Utilize o database.ipynb para fazer a análise dos dados. Esta ação cria um log que pode ser acessado enquanto o aplicativo estiver aberto.

Opção 2
O aplicativo exibirá a lista com logs de medição. Os logs consistem no último timestamp da última medição.

Opção 3
Fecha o aplicativo.

