# projet_supply-chain
 Les codes nécessaires pour récupérer les données se trouvent dans le dossier "scripts", tandis que les données elles-mêmes sont stockées dans le dossier "data"
 
### Découverte des sources de données
Nous disposons de deux catégories de données. La première regroupe des informations générales sur les entreprises, telles que le domaine d'activité, le nombre d'avis, la note Trustscore et les pourcentages correspondant à chaque classe de commentaires (notamment le pourcentage d'avis excellents). La seconde catégorie regroupe l'ensemble des commentaires pour une entreprise spécifique ayant plus de 10 000 avis (par exemple, ShowRoom), accompagnés des informations liées à chaque avis (nombre d'étoiles attribuées, indication si l'entreprise a répondu à un avis négatif). Nous avons extrait ces deux types de données en utilisant la méthode de webscraping. 

### Organisation des données
nous avons organisé ces données en utilisant différentes bases de données, à savoir une base de données relationnelle (MySQL) et une base de données NoSQL avec Elasticsearch.

