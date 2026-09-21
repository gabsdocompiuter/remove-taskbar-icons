# Remove Taskbar Icons

Script simples para remover automaticamente ícones fixados na barra de tarefas do Windows.

## Como funciona

O arquivo `main.py` usa a automação de interface do Windows para:

1. localizar a barra de tarefas;
2. verificar se cada aplicativo configurado está fixado;
3. abrir o menu do ícone com o botão direito;
4. selecionar a opção para desafixá-lo da barra de tarefas.

Por padrão, o script tenta remover os seguintes ícones:

- Outlook (classic)
- Excel
- Word

Para alterar essa lista, edite as chamadas `unpin_icon(...)` no final do arquivo `main.py`. O nome informado deve corresponder ao texto exibido pelo Windows para o aplicativo.

## Dependências

- Windows 10 ou Windows 11
- Python 3
- `pywinauto`: automação da interface do Windows
- `pywin32`: acesso a APIs do Windows
- `comtypes`: integração com componentes COM
- `six`: compatibilidade utilizada pelas dependências

As versões utilizadas estão fixadas no arquivo `requirements.txt`.

## Como rodar localmente

Abra o Prompt de Comando ou PowerShell na pasta do projeto e crie o ambiente virtual:

```powershell
python -m venv venv
```

Ative o ambiente:

```powershell
.\venv\Scripts\Activate.ps1
```

Instale as dependências:

```powershell
pip install -r requirements.txt
```

Execute o script:

```powershell
python main.py
```

Como alternativa, execute `remove_taskbar_icons.bat`. Ele aguarda 5 segundos, cria e configura o ambiente virtual na primeira execução e, depois, executa o script.

## Executar ao iniciar o Windows

Para executar o script automaticamente ao entrar no Windows, coloque um **atalho** do arquivo `remove_taskbar_icons.bat` na pasta de Inicialização:

1. Clique com o botão direito em `remove_taskbar_icons.bat` e selecione **Criar atalho**.
2. Pressione `Win + R` para abrir a janela **Executar**.
3. Digite `shell:startup` e pressione Enter.
4. Mova o atalho criado para a pasta que foi aberta.

Na próxima entrada no Windows, o atalho será executado automaticamente. O arquivo `.bat` deve continuar dentro da pasta do projeto, pois ele utiliza `main.py`, `requirements.txt` e o ambiente virtual local.
