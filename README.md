## WSLHOST (Windows subsystem for linux host)
Esse projeto pode ser utilizado com multipass, WSL e WSL2, ou outros bash para windows que possuam o disco do windows montado.

### Objetivo
Esse pequeno projeto tem como objetivo abrir o arquivo de hosts do windows pelo bash e escrever o ip do linux,
sempre que o ambiente for iniciado, inicialmente o projeto foi feito pois o serviço em go [wsl2host](https://github.com/shayne/go-wsl2-host) não funcionou comigo.

### Requisitos

- WSL 1 ou 2 (Windows subsystem for linux ativado):
- - Instalando o WSL: [wsl-ms-docs](https://docs.microsoft.com/pt-br/windows/wsl/install-win10)
- - OBS.: A instalação do WSL2 é similar mas requer a build do windows que estará disponível após 28/05/2020
- Distro linux instalada.
- - A mais popular atualmente é o Ubuntu,
porém estou utilizando o [Arch-Linux](https://github.com/yuk7/ArchWSL)
- Multipass
- - Instalando o multipass no windows 10 pro: [multipass](https://multipass.run/docs/installing-on-windows)
- - Utilizando o multipass para criar vms [multipass-start](https://multipass.run/docs/working-with-instances)
- - referencia de comandos [command-reference](https://multipass.run/docs#command-line-reference)
- Python instalado na versão 3.6+
- - Recomendo utilização do projeto [anaconda](https://www.anaconda.com/distribution/),
ou [miniconda](https://docs.conda.io/en/latest/miniconda.html), porém é opcional pois a maioria das distros já possuem python.




#### Estrutura
A estrutura do projeto.

```
wslhost
├── README.md
├── source
│   └── wslhost.py
└── wslhost.sh
```

#### Como usar
A forma mais simples de usar é executando o shell script wslhost.sh
```
path/./wshost.sh --hp path/hostsfile
```
ou
```
bash path/wshost.sh --hp path/hostsfile
```
#### Modo automatico bashrc
Para que o arquivo seja executado ao iniciar o shell wsl seja ele ubuntu ou qualquer distro,
basta passar o caminho pro shell script no .bashrc do seu perfil.

Ex.:
```
vim ~/.bashrc
```
e adicione as seguintes linhas troque "path" pelo caminho até o arquivo wslhost.sh
obs.: as reticencias no exemplo são apenas ilustrativas.
```
export WSLHOST=path/wslhost.sh
...
alias wslhost="bash $WSLHOST --hp path/hosts"
...
wslhost
```

agora sempre que você abrir um shell do wsl ele ira mapear o ip para o seu hostfile do windows,
agora basta subir seus serviços e acessar no browser seguinte a estrutura abaixo.
```
wsl.local:PORTA
```
Ex.:
```
wsl.local:8888
```

#### Contribuições
Todas as contriuições sugestões e criticas(construtivas) serão bem vindas.

Obrigado!!!
