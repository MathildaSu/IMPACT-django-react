# IMPACT Dementia (Peru)

<h3 align="center">IMPACT: Innovations using Mhealth for People with dementiA
and Co-morbidiTies  </h3>


 The system has a Django installation used for authentication, user management and (eventually) as the basis for a CMS (for the public website). Django provides a Model-View-Controller framework for the different views to access the research data. 
Two views are currently being developed: 
  
- [IMPACT app](https://github.com/ImperialCollegeLondon/IMPACT-dementia/blob/main/impact/README.md): to be used by community health workers to collect data
  
- Ana: a chatbot to provide support to clients (PLWD and families)

- [Notas](https://github.com/ImperialCollegeLondon/IMPACT-dementia/blob/main/backend/notas/README.md): a small demo app 
---

## 📝 Table of Contents
- [About](#about)
- [Getting Started](#getting_started)
- [Deployment](#deployment)
- [Usage](#usage)
- [Built Using](#built_using)
- [TODO](../TODO.md)
- [Contributing](../CONTRIBUTING.md)
- [Authors](#authors)
- [Acknowledgments](#acknowledgement)

## 🧐 About <a name = "about"></a>
This is the source code repository for the IMPACT project. The project is described here:
```
Lúcar, Miriam G., et al. ‘Peru Initiates the IMPACT Project’. The Lancet Neurology, vol. 22, no. 8, Aug. 2023, p. 653. ScienceDirect, https://doi.org/10.1016/S1474-4422(23)00239-9
```


## 🏁 Getting Started <a name = "getting_started"></a>
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

### Prerequisites
What things you need to install the software and how to install them.

```
cd backend
pip install -r requirements.txt
```

### Installing
A step by step series of examples that tell you how to get a development env running.



## 🔧 Running the tests <a name = "tests"></a>
Explain how to run the automated tests for this system.

Create DB
```
cd backend 
createdb impact-db
python manage.py migrate
python manage.py createsuperuser
```

Start server
```
python manage.py runserver  
```
Rest the server at http://127.0.0.1:8000/admin/login/?next=/admin/



## 🚀 Deployment <a name = "deployment"></a>
Add additional notes about how to deploy this on a live system.

## ⛏️ Built Using <a name = "built_using"></a>
- [Postgresql](https://www.postgresql.org) - Database
- [Django](https://www.djangoproject.com) - MVC Server Framework
- [React](https://vuejs.org/) - Web Framework
- [Python](https://www.python.org) - 

## ✍️ Authors <a name = "authors"></a>
- [@rcalvoic](https://github.com/rcalvoic) - Idea
- [@MathildaSu] (https://github.com/MathildaSu) - MVP
- Fernanda Espinoza - MVP Ana
- Marco Da Re - Interaction Design

See also the list of [contributors](https://www.impact-dementia.org) who participated in this project.

## 🎉 Acknowledgements <a name = "acknowledgement"></a>
- IMPACT team
- Paper about ANA: 
