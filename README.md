# 🧠 ChatGPT Clone

Um clone simplificado do ChatGPT utilizando **Django** e a **API da OpenAI**. Ideal para estudo, testes com a API de linguagem natural e construção de assistentes personalizados.

---

## 📌 Tecnologias Utilizadas

* [Python 3.x](https://www.python.org/)
* [Django](https://www.djangoproject.com/)
* [OpenAI API](https://platform.openai.com/docs/)
* [UV](https://github.com/astral-sh/uv)

---

## ⚙️ Pré-requisitos

Antes de iniciar, verifique se você possui os seguintes requisitos instalados:

* Python 3.13 ou superior
* `uv` instalado globalmente:

  ```bash
  pip install uv
  ```

---

## 🚀 Instalação

Siga os passos abaixo para configurar o ambiente local do projeto:

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/matheusfabiao/chatgptclone.git
   cd chatgptclone
   ```

2. **Instale as dependências com UV:**

   ```bash
   uv sync
   ```

3. **Ative o ambiente virtual:**
    ```bash
    source .venv/bin/activate        # Linux/macOS
    .venv\Scripts\activate           # Windows
    ```

4. **Configure a variável de ambiente da OpenAI:**

    Renomeie o arquivo `secrets/.env.example` para `.env` e insira as suas credenciais em cada uma das variáveis:

    ```
    OPENAI_API_KEY=your_openai_api_key_here
    OPENAI_API_BASE=your_openai_api_base_here  # Optional
    OPENAI_AI_MODEL=your_openai_ai_model_here

    SECRET_KEY=your_secret_key_here
    DEBUG=True
    ALLOWED_HOSTS=localhost,127.0.0.1
    ```

---

## 💻 Como Usar

1. **Execute as migrações (se necessário):**

   ```bash
   python manage.py migrate
   ```

2. **Inicie o servidor de desenvolvimento:**

   ```bash
   python manage.py runserver
   ```

3. **Acesse no navegador:**

   ```
   http://localhost:8000
   ```

4. **Utilize a interface web para interagir com o modelo de linguagem da OpenAI.**

---

## 🗂 Estrutura do Projeto

```bash
chatgptclone/
├── chat/           # Aplicação principal do chat (views, urls, forms)
├── core/           # Configurações globais do projeto Django
├── static/         # Arquivos estáticos (CSS, JS, imagens)
├── templates/      # Templates HTML (base, chat, etc.)
├── pyproject.toml  # Configurações e dependências do projeto
├── uv.lock         # Versiona as dependências do projeto
└── manage.py       # Arquivo gerenciador do Django
```

---

## 📄 Licença

Distribuído sob a licença [MIT](LICENSE).

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Para colaborar:

1. Faça um fork do projeto
2. Crie uma nova branch: `git checkout -b minha-feature`
3. Faça suas alterações e commit: `git commit -m "feat: minha nova feature"`
4. Envie para seu fork: `git push origin minha-feature`
5. Abra um Pull Request

---

## 📫 Contato

Desenvolvido com 💻 por [Matheus Fabião](https://github.com/matheusfabiao)
