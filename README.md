# Study Tracker

**Study Tracker** é uma aplicação full stack desenvolvida com **FastAPI (Python)** no backend e **Vue 3 + Vite + TailwindCSS** no frontend. Seu objetivo é ajudar os usuários a **organizar e monitorar sessões de estudo e pausa**, registrar as atividades realizadas, e gerar um **dashboard com métricas visuais** para acompanhar o progresso.

---

## Funcionalidades

### Controle de Blocos de Estudo e Pausa
- Adicione blocos de **estudo** ou **pausa** com duração e tags personalizadas
- Timer com contagem regressiva para cada bloco
- **Alerta sonoro** ao final de cada sessão (`finish.mp3`)

### Finalização do Dia
- Sistema para indicar quando todos os blocos do dia foram concluídos
- Botão manual "Finalizar Dia" também disponível

### Dashboard Inteligente
- Exibe **gráficos dinâmicos** com dados de estudo e pausa:
  - Tempo total por tipo (estudo/pausa) no **dia, semana e mês**
  - **Top tags** mais usadas em cada período

---

## 🛠️ Tecnologias Utilizadas

### Backend (FastAPI)
- Python 3.11+
- FastAPI + Uvicorn
- SQLAlchemy + MySQL
- Autenticação com JWT
- Estrutura modular com pastas `app/models`, `schemas`, `services`, `routers`

### Frontend (Vue 3 + Vite)
- Vue 3 + Composition API
- Pinia (store)
- Axios (requisições HTTP)
- TailwindCSS 3
- Chart.js (gráficos)
- Controle de rotas privadas

---

## Como rodar o projeto

### Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Execute o servidor
uvicorn app.main:app --reload
```

### Frontend

```bash
cd frontend
yarn install

# Execute o frontend
yarn dev
```

Acesse em: [http://localhost:5173](http://localhost:5173)

---

## Futuras Melhorias

- Conclusão automática do dia ao final do último bloco (com persistência no backend)
- Relatórios exportáveis em PDF
- Histórico completo de sessões
- Modo escuro
- Integração com Google Calendar

---

## Autor

Desenvolvido por **Thiago Souza** 

---

## 📄 Licença

Este projeto é open-source e está sob a licença MIT.