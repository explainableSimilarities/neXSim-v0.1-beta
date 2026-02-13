# neXSim-v0.1-beta

### neXSim: a System for Characterizing Nexus of Similarity

The repository of the first released beta version of neXSim, a system for Characterizing Nexus of Similarity between entities of a Knowledge Base. 
The system implements a portion of the framework presented in [A logic-based framework for characterizing nexus of similarity within knowledge bases](https://www.sciencedirect.com/science/article/pii/S0020025524002445).
It consists in a collection RESTful APIs that allow the user to retrieve entities from a Knowledge Graph, extract the portion of knowledge relevant for each entity and characterize their Nexus of Similarity, ending up in a concise while meaningful formula explaning it. 

### Technologies
**neXSim** is implemented in Python, using Flask as web framework. It relies on a Neo4j Graph Database to store the Knowledge Graph and a PostgresQL Database to store information about entities. The system is designed to be easily deployable in a Docker container.

### Project Strucutre

``` text
neXSim-v0.1-beta/
├── neXSim/                       # source code folder
│   ├── characterization.py       # Characterization Algorithm and utilities
│   ├── lca.py                    # Utilities for navigating taxonomical relations 
│   ├── models.py                 # Data Models
│   ├── neo4j_manager.py          # Communication Layer with a Neo4j Graph Database 
│   ├── postgresQL_manager.py     # Communication Layer with a PostgresQL Database 
│   ├── report.py                 # Functions to generate textual report of entities in input (output of all the functionalities in a text file)
│   ├── router.py                 # API Layer
│   ├── search.py                 # Utilities for entity search
│   ├── summary.py                # Algorithms and utilities for entity summarization
│   └── utils.py                  # Additional Utilities
├── .env                          # environment variables (to be set)
├── .gitignore                    # Files to exclude from Git
├── app.py                        # Entry point (Flask)
├── docker-compose.yml            # For installation in a docker container
├── gunicorn_config.py            # Server configuration
├── README.md                     # You are here!
└── requirements.txt              # Python dependencies
```

### Installation

To install and run neXSim, follow these steps:
1. Clone the repository:
  ```bash
   git clone https://github.com/your-username/neXSim-v0.1-beta.git
   cd neXSim-v0.1-beta
  ```
2. Set up environment variables in the `.env` file (e.g., database connection details).
3. Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```
4. Run the application:
  ```bash
  gunicorn -c gunicorn_config.py app:app
  ```

### Usage
Once the application is running, you can access the API endpoints via HTTP to retrieve entities, extract relevant knowledge, and characterize their Nexus of Similarity.

### Api Endpoints

- `GET /api/search/<string:lemma>/<int:page>`: Search for entities in the Knowledge Graph based on a lemma (e.g., "apple", "dog", "New York").
- `POST /api/entities/`: Retrieve information about a list of entities based on their ids.
- `GET /api/entities/<string:ids>`: Retrieve information about a list of entities based on their ids.
- `POST /api/summary`: Given a set of entities in input, outputs the relevant properties of each entity.
- `POST /api/characterize`: Given a set of entities in input and the corresponding summaries, it outputs the core characterization
- `POST /api/lca`: The endpoint computes, for a set of entities, the least common neighbors over taxonomical relations
- `POST /api/kernel`: Given a set of entities in input and the corresponding summaries and least common neighbors, it outputs the core characterization
- `POST /api/oneshot`: It computer summary, characterize, lca, kernel having in input a list of entities
- `/api/unit/report/<string:mode>`: Given a set of entities, it produces a text or json file reporting summaries, characterization, kernel, least common neighbors, plus some extra information

### Online Availability

The system is currently available online [here](http://prode-2.alviano.net/) where a web interface allows even non-technical users to interact with the system and test its main functionalities.

### References

- [A logic-based framework for characterizing nexus of similarity within knowledge bases](https://www.sciencedirect.com/science/article/pii/S0020025524002445)

