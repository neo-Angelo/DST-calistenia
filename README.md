# Treinos de Calistenia - DST PYTHON PRO

Um aplicativo web desenvolvido em **Python** utilizando o framework **Flask**. Este projeto foi criado com o objetivo de colocar em prática os conceitos de roteamento, renderização de templates, além de aplicar uma lógica de gamificação para incentivar a manutenção da rotina de treinos.

## 🎯 Funcionalidades

* **Gestão de Treinos (CRUD Completo):** * **Create:** Adicionar novos exercícios com número de séries, repetições e data de execução.
  * **Read:** Visualizar o histórico completo de treinos registrados na interface principal.
  * **Update:** Editar informações de treinos já cadastrados ou alternar o status para "Concluído".
  * **Delete:** Excluir registros específicos do histórico.
* **Sistema de Gamificação (RPG):** Ao marcar um treino como concluído, o usuário ganha pontos de experiência (XP). A cada 100 XP acumulados, a barra de progresso enche e o jogador sobe de nível.
* **Sistema de Busca:** Barra de pesquisa implementada no backend para filtrar e localizar rapidamente exercícios no histórico.
* **Interface Dark Mode:** Design moderno, responsivo e focado em usabilidade, construído com HTML e CSS nativos.

## 🛠️ Tecnologias e Bibliotecas Utilizadas

* **Python 3**
* **Flask:** Utilizado para gerenciar rotas, requisições HTTP (`request`), redirecionamentos (`redirect`, `url_for`) e renderização de páginas (`render_template`).
* **Jinja2:** Motor de templates nativo do Flask para integração de variáveis Python no HTML.
* **HTML5 & CSS3**

## ⚙️ Como executar o projeto localmente

1. Certifique-se de ter o Python 3 instalado no seu sistema (compatível com Windows, macOS e distribuições Linux/WSL).
2. Clone este repositório para a sua máquina:
   ```bash
   git clone https://github.com/neo-Angelo/DST-calistenia.git

    ```
3. Instale as pendencias necessarias
   
   ```bash

   pip install -r requirements.txt

   ```
4. execute a plataforma
   
 ```bash

   python app.py

 ```

   OU

 ```bash

   python3 app.py

 ```
5. acessse a plataforma
   
   Abra o seu navegador e acesse: http://127.0.0.1:5000/

## ⚙️ Plataforma

<img width="1477" height="696" alt="Image" src="https://github.com/user-attachments/assets/56d3b702-00da-4669-9a65-b8ecdc610a8f" />

<img width="1524" height="704" alt="Image" src="https://github.com/user-attachments/assets/ba5c7b9a-1e66-4afd-853d-eeba4efc5205" />
