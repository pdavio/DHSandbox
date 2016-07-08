from SPARQLWrapper import SPARQLWrapper, JSON

def get_country_description():
    query = "PREFIX dbres: <http://dbpedia.org/resource/>DESCRIBE dbres:United_States"

    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    sparql.setReturnFormat(JSON)

    sparql.setQuery(query)  # the previous query as a literal string

    return sparql.query().convert()