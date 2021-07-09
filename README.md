# Contatos API 

### Arquitetura:

De acordo com o desafio proposto pela MercaFácil, minha solução foi criar uma arquitetura simples, com um serviço consumindo as duas fontes de dados (Macapa e Varejao).

---

### Tecnologias:

- Python: 3.8
- Django: 2.2.12
- PyJWT
- Swagger
- Docker
- ORM SQLAlchemy
- Docker-compose
- MySQL
- PostgreSQL

---

### Iniciando a aplicação:

- git clone ---
- docker-compose up --build

A construção do container e inicialização da aplicação irá criar as tabelas Contatos Macapa e Contatos Varejao, criará grupos de permissões que e um usuário Admin e por fim irá popular as tabelas criadas com a fonte da dados fornecidas. 

---

### Notas:

- Documentação da API: urlswagger
- Link Admin: link
- Usuário de acesso: { admin, 1234 }
- Executar teste: python manage.py test
- Link aplicação front: link
