# Ponderada 4

Esta ponderada consiste em criar uma aplicação completa de machine learning, com modelo treinado a partir de um dataset, implementação de uma API com autenticação por JWT e frontend com visualização de dados.

Assim, o repositório é dividido em três partes:

1. Machine learning, contendo o notebook de treinamento.
2. Backend, contendo o servidor em Node.js, API e lógica de autenticação, com conexão com banco de dados não relacional, hospedado no Atlas MongoDB. Foi escolhido o MongoDB pela facilidade de conexão e free tier sem necessidade de cartão de crédito. Já o Node foi escolhido pela maior familiaridade com a estrutura MVC nesse formato.
3. Frontend, contendo interface de login, predição e visualização de dados em Streamlit. Essa biblioteca foi escolhida pela construção mais rápida de interface juntamente da possibilidade de se implementar gráficos diretamente com pandas e matplotlib.

O modelo em si se trata de um classificador de diabetes com base em sexo, IMC, idade, Hba1c, glicose no sangue, doença cardíaca e hipertensão. Ele foi treinado a partir de um dataset do Kaggle (https://www.kaggle.com/datasets/iammustafatz/diabetes-prediction-dataset/) com modelos de classificação como regressão logísitica, Naive Bayes, Random Forest e Extra Trees. O modelo foi salvo como um pickle e implementado no backend.

No frontend, é possível fazer login, criar um novo usuário, fazer requisições de predição e visualizar alguns gráficos provenientes do dataset original.

As imagens estão disponíveis nestes links:
https://hub.docker.com/repository/docker/elisaflemer/p4back
https://hub.docker.com/repository/docker/elisaflemer/p4front

Para conectar com o banco não relacional, foi necessário criar um Cluster no Atlas e utilizar a biblioteca 'mongoose' no arquivo backend/config/db.js. Foi utilizada a URI de conexão juntamente do usuário e senha da conta. Após o deploy na nuvem, foi necessário adicionar o IP da máquina virtual na lista de whitelist.

Para deployar tudo na AWS, foram criadas duas EC2 em Ubuntu. O acesso a elas foi configurado como público, a partir de todos os endereços http e https. Foram ainda criados IP elásticos para cada uma delas e os grupos de segurança foram atualizados para expor as portas necessárias (8501 e 5000). Em cada uma delas, foi instalado o Docker. Depois, foi feito o download das imagens a partir do Dockerhub para posterior execução.

## Funcionamento da predição

Para que as rotas de predição fossem protegidas, foi criado um subprocesso de Python dentro do Node, que executa o script predict.py quando a rota /api/predict é acessada com um JWT válido. Já para a visualização de dados, como o dataset é público, ele foi disponibilizado diretamente no frontendp para consumo do Streamlit.

## Como executar localmente
Em dois terminais distintos, rode:

```
sudo docker run -p 5000:5000 elisaflemer/p4back
```

```
sudo docker run -p 8501:8501 elisaflemer/p4front
```

Então, acesse: http://localhost:8501

## Como executar em EC2

Crie uma EC2 para o backend e uma EC2 para o frontend. Associe IPs elásticos a cada uma delas e instale o Docker, executando:

```
sudo snap install docker
```

Na máquina de backend, rode:

```
sudo docker run -p 5000:5000 elisaflemer/p4back
```

Na máquina de frontend, rode:

```
sudo docker run -p 8501:8501 elisaflemer/p4front
```

Então, abra as respectivas portas nos grupos de segurança de cada EC2.