# Python & Flask & Docker
# Arquitetura de Software Aplicada 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Aulas de Python estuda das na UFU 2 semestre de 2019 ,onde a materia é Arquitetura de Software
Aplicada , dando enfaze ao framework FLASK e um software de contêiner chamado DOCKER.
<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Estudo sobre a linguagem Python.

## Rodando os Projetos

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Há muitos pacotes diferentes para cada aula ou projeto a serem utilizado, mas todos deve se utilizar o pip e os container do docker.

- Rodando Docker : [Instale o Docker na sua maquina apartir deste link](https://www.digitalocean.com/community/tutorials/como-instalar-e-usar-o-docker-no-ubuntu-18-04-pt)

# Configuração dos Container

#### Criando container:
docker run --name postgreSQL --network=postgre-network -e "POSTGRES_PASSWORD=banco" -p 5432:5432 -v /home/marciocunha/Util/bdPostgres:/var/lib/postgresql/data -d postgres

#### Criando rede do container: 
docker network create --driver bridge postgre-network

#### Comandos basicos para se utilizar no docker:

docker container ls<br/>docker container -a<br/>docker container ls -a <br/>docker network -ls

- Para iniciar o container do docker usar:<br/>
docker start "numero ip do conatiner" - | exemplo : docker start 5b725675c9a4
- Para parar o container do docker usar<br/>
docker stop "numero ip do conatiner" - | exemplo : docker stop 5b725675c9a4

# Docker Compose

#### Há tambem uma funcionalidade a mais que devera ser utilizada nos projetos chamado Docker Compose,<br/>onde ele irá separar o backend do frontend

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Para utilizar o docker compose deve-se fazer uma junção com o sistema de gerenciamento de pacotes PIP para pegar todos os pacotes instalados no seu projeto , então deverá utilizar o comando:<br/>
python -m pip freeze > requirements.txt

A seguir inicializar o docker compose.

- Comandos basicos a serem utilizados no docker compose são:
<br/>docker-compose up<br/>docker-compose down<br/>docker-compose rm<br/><br/>

# PIP (gerenciador de pacotes)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Irá utilizar o pip nos projetos tambem onde írá gerenciar pacotes dos softwares escritos na linguagem de programação Python.

Para instalar o pip: sudo apt-get install python-pip

Para instalar um pacote na maquina virtual usando o pip usar :<br/>

Exemplo: python3 -m pip install flask <br/>
python3 -m pip install "nome do pacote"

Ver todos pacotes instalados na maquina virtual: pip list

Pegar todos os pacotes do seu projeto para usar no docker: python -m pip freeze > requirements.txt

# Maquina virtual(venv)

baixar maquina virtual - sudo apt-get install python3-venv<br/>
Versão maquina virtual - virtualenv --version<br/>
Criar maquina virtual  - python3 -m venv venv<br/>
Ativar maquina virtual - source venv/bin/activate<br/>

