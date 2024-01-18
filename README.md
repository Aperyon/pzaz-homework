# Pzaz homework

## Setup

### Backend

**Prerequisites**
- Poetry
- Make

Run 
```bash
cd backend
poetry install
make setup
```


### Frontend

**Prerequisites**
- Node + Npm

Run
```bash
cd frontend
npm i
npm run dev
```

## The App
Navigate to http://localhost:5173 to see the frontend. The backend runs on http://localhost:8000


## Ways to improve the App
- [ ] Filtering
- [ ] Sorting
- [ ] Pagination
- [ ] Translations
- [ ] Toast messages
- [ ] Design (maybe with Tailwind)
- [ ] Replace Vuex with Vue-Query for "server state"
- [ ] Protected routes (instead of manual redirects)
- [ ] Confirmation (before dangerous operations such as delete)
- [ ] Displaying form errors (including non field errors)
- [ ] Add frontend tests

