# 📱 TL Phone API

API RESTful desenvolvida com Django Rest Framework para gerenciamento de produtos (iPhones), com infraestrutura completa de CI/CD e ambientes de Homologação e Produção.

## 🚀 Links do Projeto

| Ambiente | Status | API URL | Documentação (Swagger) |
| :--- | :--- | :--- | :--- |
| **Produção** (Estável) | 🟢 Online | [Acessar API](https://tl.aaleff.me/api/products/) | [Ver Docs](https://tl.aaleff.me/swagger/) |
| **Homologação** (Testes) | 🟡 Dev | [Acessar API](https://homolog.tl.aaleff.me/api/products/) | [Ver Docs](https://homolog.tl.aaleff.me/swagger/) |

---

## 🛠️ Tecnologias Utilizadas

* **Backend:** Python, Django, Django Rest Framework (DRF).
* **Infraestrutura:** AWS EC2 (Ubuntu), Nginx (Reverse Proxy), Gunicorn (App Server).
* **Banco de Dados:** PostgreSQL (Produção) / SQLite (Local).
* **DevOps:** GitHub Actions (CI/CD Automático), Systemd services.
* **Segurança:** Certbot (SSL/HTTPS), CORS Headers, Permissions (Auth/ReadOnly).
* **Documentação:** Swagger (drf-yasg).

---

## ⚙️ Fluxo de CI/CD (Deploy Automático)

O projeto utiliza **GitHub Actions** para deploy contínuo:

1.  **Branch `homolog`**:
    * Qualquer push dispara o deploy para o ambiente de *Staging*.
    * URL: `homolog.tl.aaleff.me`
    * Uso: Testes de novas features antes de ir para o ar.

2.  **Branch `main`**:
    * Apenas via **Pull Request** aprovado.
    * Dispara o deploy para o ambiente de *Produção*.
    * URL: `tl.aaleff.me`
    * Uso: Versão estável para o usuário final.

---

## 💻 Como rodar localmente

Se quiser rodar o projeto na sua máquina:

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/oafarias/TL-Phone.git](https://github.com/oafarias/TL-Phone.git)
    cd TL-Phone
    ```

2.  **Crie e ative o ambiente virtual:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure o .env:**
    Crie um arquivo `.env` na raiz baseado no exemplo ou use as configs locais.

5.  **Execute as migrações e rode o servidor:**
    ```bash
    python manage.py migrate
    python manage.py runserver
    ```

---

## 🔒 Endpoints Principais

Acesse `/swagger/` para ver a lista completa e testar.

* `GET /api/products/` - Lista todos os produtos (Público).
* `POST /api/products/` - Cria novo produto (Requer Auth).
* `GET /api/products/{id}/` - Detalhes de um produto.
* `PUT /api/products/{id}/` - Atualiza produto (Requer Auth).
* `DELETE /api/products/{id}/` - Remove produto (Requer Auth).

---

Developed by **Alef Farias**