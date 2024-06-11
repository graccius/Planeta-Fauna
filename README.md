# 🌍 PLANETA FAUNA

Bem-vindo ao protótipo 1.0 do Projeto Planeta Fauna! Este protótipo apresenta uma aplicação inicial que permite explorar diferentes reinos da vida animal, visualizando filos, subfilos e espécies associadas.

## 📜 Escopo do Projeto

O Projeto Planeta Fauna visa criar uma plataforma que forneça informações detalhadas sobre as diversas formas de vida em nosso planeta, organizadas em uma hierarquia taxonômica. O objetivo final é criar uma ferramenta educacional e de pesquisa para estudantes, cientistas e entusiastas da vida selvagem.

## 📚 Casos de Uso

### 🔍 Explorar Reinos
- Os usuários podem selecionar um reino da lista de reinos disponíveis.
- Após selecionar um reino, são apresentadas informações sobre os filos associados a esse reino.

### 🔍 Explorar Filos
- Os usuários podem visualizar os filos associados a um determinado reino.
- Cada filo é exibido com uma imagem representativa e um link para visualizar os subfilos associados.

### 🔍 Explorar Subfilos
- Os usuários podem visualizar os subfilos associados a um determinado filo.
- Cada subfilo é exibido com uma lista de espécies associadas.

### 🔍 Explorar Espécies
- Os usuários podem visualizar as espécies associadas a um determinado subfilo.
- Cada espécie é exibida com informações detalhadas, como nome científico, habitat, comportamento, etc.

### 🔍 Pesquisar
- Os usuários podem pesquisar por um reino, filo, subfilo ou espécie específicos.
- A pesquisa é realizada em tempo real à medida que o usuário digita, sugerindo resultados correspondentes.
- Ao selecionar um item da lista de resultados da pesquisa, o usuário é redirecionado para a página de detalhes desse item.
- Se nenhum resultado correspondente for encontrado, uma mensagem informando que nenhum resultado foi encontrado é exibida ao usuário.

## 🛠️ Configuração do Ambiente de Desenvolvimento

Para rodar a aplicação localmente, siga os passos abaixo:

### 1. Clonar o Repositório
 - git clone https://github.com/graccius/planeta-fauna.git
 - cd planeta-fauna

 
### 2. Criar e Ativar um Ambiente Virtual 
 - No Windows: 
    - python -m venv venv
    - venv\Scripts\activate
 - No macOS/Linux
    - python3 -m venv venv
    - source venv/bin/activate
### 3. Instalar Dependências
 - pip install -r requirements.txt
### 4. Configurar Variáveis de Ambiente
 - Crie um arquivo .env na raiz do projeto e adicione as seguintes variáveis de ambiente:
 - SECRET_KEY=sua_chave_secreta
 - DEBUG=True
### 5. Rodar Migrações do Banco de Dados
 - python manage.py migrate
### 6. Iniciar o Servidor de Desenvolvimento
 - python manage.py runserver


