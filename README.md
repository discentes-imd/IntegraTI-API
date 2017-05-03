# IntegraTI

Veja nossa [wiki com a documentação](https://github.com/bti-imd/IntegraTI-API/wiki) 
Ideias iniciais do projeto:
* Autogerência de minicursos e eventos discentes e docentes (“horizontalmente”) (exposição de temas, voluntariado de apresentadores etc), com anexo dos materiais usados no evento e talvez funções de divulgaço por e-mail;
* Organizar grupos de estudos (temporários ou não);
* Exposição de reclamações isoladas (como chamados) na infraestrutura;
* Repositório de trabalhos (sistemas, artigos etc) do curso com fácil contato aos criadores, como um portfólio avaliado pelos outros discentes usando vários critérios técnicos ou não;
* Autenticação via SIGAA;
* Área pública e área privada;
* Área para monitorias com contatos, agenda e outras informações fornecidas pelos monitores;
* FAQs para os ingressantes, ou um guia rápido do calouro;
* Publicitar agendas dos laboratórios;
* Fácil acesso a vagas de bolsas, estágios etc. vindos filtrados do bd do SIGAA.

## Sobre a implementação
A implementação será feita utilizando uma abordagem de RESTful API. Na qual [IntegraTI-API](https://github.com/bti-imd/IntegraTI-AP) fornecerá a API utilizada pela interface implementada na [IntegraTI-Web](https://github.com/bti-imd/IntegraTI-Web).
### Tecnologias utilizadas
* Python
* Flask
* MySQL / PostgreSQL
