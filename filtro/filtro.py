from scrapy.selector import Selector
import sys
import re
import w3lib.html
import unicodedata
from uteis import auxiliares, estruturas
from bs4 import BeautifulSoup
import os
import pathlib
import csv

class Filtro():

    def __init__(self, path="", writer=0, **kwargs):
        self.path = path
        self.saidaCSV = writer
    
    def associaUrlFilePath(self, url, file_path):
        myPath = pathlib.Path(file_path)
        self.urls_filePath[url] = pathlib.Path(file_path)

    def montaUrl(self, nomeArquivo:str):
        path_url_idx_start = nomeArquivo.index('http')

        primeiraParteNomeArquivo = nomeArquivo[:path_url_idx_start]
        apenasParteUrl = nomeArquivo[path_url_idx_start:]
        parteUrlModificado = apenasParteUrl.replace(".txt", "").replace("_", "/").replace("}", "_").replace("(", ":").replace("{", "?").replace(")", "=")

        return parteUrlModificado

    def start_requests(self):

        self.urls = []
        self.urls_filePath = dict()
        
        myPath = pathlib.Path(self.path)

        for file in [f for f in myPath.glob("*") if f.is_file()]:

            if str(file).endswith(".txt"):
                file_path = str(file)

                url = self.montaUrl(str(file))
                self.urls.append(url)

                self.associaUrlFilePath(url, file_path)

        for url in self.urls:
            self.parse(url)

    def parse(self, url):

        print("\n\n### PAGINA: {} ###\n\n".format(url))

        urls = estruturas.URLsDeInteresse()
        
        with open(self.urls_filePath[url], 'r', encoding="utf8") as f:

            body = f.read()

        emails = list(set(re.findall('[a-zA-Z0-9_\-\.]+@[a-z]+(?:\.[a-z]+)+', body)))
        
        #-----USE UMA DAS DUAS OPÇÕES ABAIXO-----

        #USANDO BEAUTIFULSOUP
        soup = BeautifulSoup(body, 'lxml')
        trending_links_novo = soup.find_all('a')

        trending_links_novo_texts = []
        for link in trending_links_novo:
            trending_links_novo_texts.append(str(link))

        string_trending_links_novo = " ".join(trending_links_novo_texts)
        #FIM USANDO BEAUTIFULSOUP
        
        #USANDO REGEX
        #trending_links_novo = re.findall('<a.*?href=[\'\"].+[\'\"].*?>.*?<\\/a>', body)
        #string_trending_links_novo = " ".join(trending_links_novo)
        #FIM USANDO REGEX

        trending_links_links = Selector(text=string_trending_links_novo).css("a::attr(href)").extract()
        trending_links_textos = Selector(text=string_trending_links_novo).css("a::text").extract()

        self.lista_pares_link_texto = []

        if len(trending_links_links) == len(trending_links_textos):
            for i in range(len(trending_links_links)):
                if trending_links_links[i].find("javascript:") == -1 and trending_links_links[i].find("../../") == -1:
                    self.lista_pares_link_texto.append((trending_links_links[i], trending_links_textos[i]))
        else:
            for i in range(len(trending_links_links)):
                if trending_links_links[i].find("javascript:") == -1 and trending_links_links[i].find("../../") == -1:
                    self.lista_pares_link_texto.append((trending_links_links[i], ""))       
        
        body = w3lib.html.replace_tags(body, ' ')
        
        lista = auxiliares.splitText(body)

        conjunto = []
        for elemento in lista:
            if len(elemento) > 3:
                conjunto.append(elemento)
        
        nomeSaida = "saida_"+url.replace("entradas/", "").replace("_", "}").replace("/", "_").replace(":", "(").replace("?", "{").replace("=", ")")+".json"


        termosDeInteresse = estruturas.TermosDeInteresse(url, conjunto)
        termosDeInteresse.determinaPrincGovAtendidos(self.saidaCSV, nomeSaida, url, urls, self.lista_pares_link_texto, emails)
    
def main():
    path = sys.argv[1]

    with open('resultadoCSV.csv', mode='w') as saidaCSV:

        campos = ['Site', 'provide_metadata', 'provide_descriptive_metadata', 'provide_data_license_information', 'provide_data_provenance_information', 'provide_data_quality_information', 'provide_a_version_indicator', 'provide_version_history', 'gather_feedback_from_data_consumers', 'make_feedback_available', 'provide_bulk_download', 'provide_data_up_to_date', 'use_persistent_URIs_as_identifiers_of_datasets', 'use_machine_readable_standardized_data_formats', 'provide_data_in_multiple_formats', 'assess_dataset_coverage', 'provide_feedback_to_the_original_publisher', 'cite_the_original_publication']
        writer = csv.DictWriter(saidaCSV, fieldnames=campos)

        writer.writeheader()

        filtro = Filtro(path, writer)
        filtro.start_requests()

main()
