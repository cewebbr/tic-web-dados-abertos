from . import estruturas
import json
import csv
from datetime import date
import unicodedata
import pathlib

##################################################################################################################

def encontraTermoATermoCache(listaPalavrasPortal, cacheTokens):
    contador = 0

    posicao = 1
    copiaCache = cacheTokens.copy()
    palavrasNaCache = copiaCache.keys()

    for palavraPortal in listaPalavrasPortal:
        for palavraCache in palavrasNaCache:
            if palavraCache.lower() == palavraPortal.lower():

                if cacheTokens[palavraCache] == []:
                    contador += 1
                
                cacheTokens[palavraCache].append(posicao)

        posicao += 1

def encontraTermosVocabularios(dicionarioVocabularios, cacheTokens, dicionarioVocabulariosCount):
    termos_presentes = set()

    for vocabularioChaves, vocabularioValores in dicionarioVocabularios.items():
        for termo in vocabularioValores:
            termoSplit = tuple(termo.split(" "))

            if termoExiste(termoSplit, cacheTokens):
                termos_presentes.add(termo)

                vocabularioValores[termo] = 1
                dicionarioVocabulariosCount[vocabularioChaves] += 1

def termoExiste(palavrasTermo:tuple, posicoesPalavras:dict()) -> bool: 
    if todasPalavrasTermoForamEncontradas(palavrasTermo, posicoesPalavras):
        return sequenciaExisteEm(palavrasTermo, posicoesPalavras)
    else:
        return False
    
def todasPalavrasTermoForamEncontradas(palavras:tuple, posicoesPalavras:dict()) -> bool: 
    for palavra in palavras:
        if len(posicoesPalavras[palavra]) == 0:
            return False
    
    return True

def sequenciaExisteEm(palavrasTermo:tuple, posicoesPalavrasTermo:dict()):
    
    if len(palavrasTermo) == 1:
        return True
    
    posicoesPrimeiraPalavra = posicoesPalavrasTermo[palavrasTermo[0]]
    for posicao in posicoesPrimeiraPalavra:
        posicoesOutrasPalavrasTermoDevemEstar = range(posicao+1, posicao+len(palavrasTermo))

        todasPalavrasLocaisCorretos = True
        for idxPalavra, posQueAPalavraDeveEstar in enumerate(posicoesOutrasPalavrasTermoDevemEstar, start = 1):
            if posQueAPalavraDeveEstar not in posicoesPalavrasTermo[palavrasTermo[idxPalavra]]:
                todasPalavrasLocaisCorretos = False
                break

        
        if todasPalavrasLocaisCorretos:
            return True
    
    return False

def encontraVocabulariosDosPrincGov(dicionarioPrincGovern, dicionarioVocabulariosCount, dicionarioPrincGovernCount):
    for principioChaves, principioValores in dicionarioPrincGovern.items():

        for nomeVocabulario in principioValores.keys():
            if dicionarioVocabulariosCount[nomeVocabulario] > 0:
                principioValores[nomeVocabulario] = 1
                dicionarioPrincGovernCount[principioChaves] += 1

def encontraPrincGovAtendidos(dicionarioPrincGovernCount, princGovernAtendidos):
    for princGovChave, princGovValor in dicionarioPrincGovernCount.items():
        if princGovValor > 0:
            princGovernAtendidos[princGovChave] = 1

##################################################################################################################

def padronizaString(texto):
    texto2 = unicodedata.normalize("NFD", texto)
    texto2 = texto2.encode("ascii", "ignore")
    texto2 = texto2.decode("utf-8")

    return texto2

def validaInfMetadados(linhaCSV, saida, enderecoPagina, urls, trending_links, principio, dicionarioVocabulariosCount, infMetadados):

    encontrouTokens = False
    encontrouLinksMetadados = False

    if (dicionarioVocabulariosCount['infMetadados'] != 0):
        saida.dicionarioJson['principiosGovernanca'][principio]['regras']['informacoesSobreMetadados']['found'] = True
        saida.dicionarioJson['principiosGovernanca'][principio]['regras']['informacoesSobreMetadados']['presencaTokens'] = True

        encontrouTokens = True

        for token, valor in infMetadados.items():
            if valor != 0:
                saida.dicionarioJson['principiosGovernanca'][principio]['regras']['informacoesSobreMetadados']['tokens'].append(padronizaString(token))
    
    for valor in urls.cacheURLsTextos.values():
        if (valor != 0):
            saida.dicionarioJson['principiosGovernanca'][principio]['regras']['informacoesSobreMetadados']['presencaURLsArquivosMetadadosAnexos'] = True
            saida.dicionarioJson['principiosGovernanca'][principio]['regras']['informacoesSobreMetadados']['found'] = True
            break
    
    linksMetadadosEncontrados = set()
    
    for palavra, links in urls.palavrasInteressantesLinks.items():
        for link in links:
            #Link não completo
            if link[0] == '/':
                endereco_split = enderecoPagina.split("/")
                link_completo = endereco_split[0]+"//"+endereco_split[2]+link
                linksMetadadosEncontrados.add(link_completo)
        
            else:
                linksMetadadosEncontrados.add(link)

    listaLinks = list(linksMetadadosEncontrados)

    if len(linksMetadadosEncontrados) > 0:
        encontrouLinksMetadados = True

    saida.dicionarioJson['principiosGovernanca'][principio]['regras']['informacoesSobreMetadados']['URLsArquivosMetadadosAnexos'] = listaLinks

    if encontrouTokens or encontrouLinksMetadados:
        return True
    else:
        return False

def validaInfLicenca(linhaCSV, saida, principio, dicionarioVocabulariosCount, infLicenca):
    encontrouTokens = False

    if (dicionarioVocabulariosCount['infLicenca'] != 0):
        saida.dicionarioJson['principiosGovernanca'][principio]['regras']['informacoesSobreLicenca']['presencaTokens'] = True
        encontrouTokens = True

        for token, valor in infLicenca.items():
            if valor != 0:
                saida.dicionarioJson['principiosGovernanca'][principio]['regras']['informacoesSobreLicenca']['tokens'].append(padronizaString(token))

    if encontrouTokens: 
        return True
    else:
        return False

def validaInfProcedenciaDados(linhaCSV, saida, principio, dicionarioVocabulariosCount, infProcedenciaDados):
    encontrouTokens = False

    if (dicionarioVocabulariosCount['infProcedenciaDados'] != 0):
        saida.dicionarioJson['principiosGovernanca'][principio]['regras']['informacoesSobreProcedenciaDados']['presencaTokens'] = True
        encontrouTokens = True

        for token, valor in infProcedenciaDados.items():
            if valor != 0:
                saida.dicionarioJson['principiosGovernanca'][principio]['regras']['informacoesSobreProcedenciaDados']['tokens'].append(padronizaString(token))

    if encontrouTokens: 
        return True
    else:
        return False

def validaInfQualidadePublicacaoDados(linhaCSV, saida, principio, dicionarioVocabulariosCount, infQualidadePublicacaoDados):
    encontrouTokens = False

    if (dicionarioVocabulariosCount['infQualidadePublicacaoDados'] != 0):
        saida.dicionarioJson['principiosGovernanca'][principio]['regras']['informacoesSobreQualidadeDados']['presencaTokens'] = True
        encontrouTokens = True

        for token, valor in infQualidadePublicacaoDados.items():
            if valor != 0:
                saida.dicionarioJson['principiosGovernanca'][principio]['regras']['informacoesSobreQualidadeDados']['tokens'].append(padronizaString(token))
    
    if encontrouTokens: 
        return True
    else:
        return False

def validaInfVersionamentoDados(linhaCSV, saida, principio, dicionarioVocabulariosCount, infVersionamentoDados):
    encontrouTokens = False

    if (dicionarioVocabulariosCount['infVersionamentoDados'] != 0):
        saida.dicionarioJson['principiosGovernanca'][principio]['regras']['informacoesSobreVersionamentoDados']['presencaTokens'] = True
        encontrouTokens = True

        for token, valor in infVersionamentoDados.items():
            if valor != 0:
                saida.dicionarioJson['principiosGovernanca'][principio]['regras']['informacoesSobreVersionamentoDados']['tokens'].append(padronizaString(token))

    if encontrouTokens: 
        return True
    else:
        return False
    
def validaInfFeedback(linhaCSV, saida, principio, dicionarioVocabulariosCount, infFeedback, emails):
    encontrouTokens = False

    if (dicionarioVocabulariosCount['infFeedback'] != 0):
        saida.dicionarioJson['principiosGovernanca'][principio]['regras']['informacoesSobreFeedback']['presencaTokens'] = True
        encontrouTokens = True

        for token, valor in infFeedback.items():
            if valor != 0:
                saida.dicionarioJson['principiosGovernanca'][principio]['regras']['informacoesSobreFeedback']['tokens'].append(padronizaString(token))

    saida.dicionarioJson['principiosGovernanca'][principio]['regras']['informacoesSobreFeedback']['emails'] = emails

    if encontrouTokens: 
        return True
    else:
        return False

def validaInfRepublicacaoDados(linhaCSV, saida, principio, dicionarioVocabulariosCount, infRepublicacaoDados):
    encontrouTokens = False

    if (dicionarioVocabulariosCount['infRepublicacaoDados'] != 0):
        saida.dicionarioJson['principiosGovernanca'][principio]['regras']['informacoesSobreRepublicacaoDosDados']['presencaTokens'] = True
        encontrouTokens = True

        for token, valor in infRepublicacaoDados.items():
            if valor != 0:
                saida.dicionarioJson['principiosGovernanca'][principio]['regras']['informacoesSobreRepublicacaoDosDados']['tokens'].append(padronizaString(token))

    if encontrouTokens: 
        return True
    else:
        return False

def validaInfGarantirAcessoDados(linhaCSV, saida, urls, trending_links, principio, infGarantirAcessoDadosDownload, infGarantirAcessoDadosAPI):
    
    extensoesVolumeDados = ['zip', 'rar', '7z', 'tar', 'gz']
    #Download
        #Extensões zip, rar, 7z, tar, gz
    for extensao in extensoesVolumeDados:
        for link in trending_links:
            if extensao in link[0].lower() or extensao in link[1].lower():
                saida.dicionarioJson['principiosGovernanca'][principio]['regras']['informacoesSobreGarantirAcessoAosDados']['download']['extensoesUrlsVolumeDados'] = True
                saida.dicionarioJson['principiosGovernanca'][principio]['regras']['informacoesSobreGarantirAcessoAosDados']['found'] = True
                break

    linksComExtensao = set()
    for extensao in extensoesVolumeDados:
        for link in trending_links:
            if extensao in link[0].lower():
                linksComExtensao.add(link[0])

    listaLinksComExtensao = list(linksComExtensao)

    saida.dicionarioJson['principiosGovernanca'][principio]['regras']['informacoesSobreGarantirAcessoAosDados']['download']['urlsVolumeDados'] = listaLinksComExtensao
        
        #Dados atualizados tokens
    for elemento in infGarantirAcessoDadosDownload.values():
        if elemento != 0:
            saida.dicionarioJson['principiosGovernanca'][principio]['regras']['informacoesSobreGarantirAcessoAosDados']['download']['presencaTokensUrlsDadosAtualizados'] = True
            break
        
    for token, valor in infGarantirAcessoDadosDownload.items():
        if valor != 0:
            saida.dicionarioJson['principiosGovernanca'][principio]['regras']['informacoesSobreGarantirAcessoAosDados']['download']['tokensUrlsDadosAtualizados'].append(padronizaString(token))

    #API
    palavrasURLs = ['API', 'documentacao', 'swagger', 'docs', 'io-docs', 'openApis']

    for elemento in infGarantirAcessoDadosAPI.values():
        if elemento != 0:
            saida.dicionarioJson['principiosGovernanca'][principio]['regras']['informacoesSobreGarantirAcessoAosDados']['APIs']['presencaTokensPaginaAPI'] = True
            saida.dicionarioJson['principiosGovernanca'][principio]['regras']['informacoesSobreGarantirAcessoAosDados']['found'] = True
            break
        
    for token, valor in infGarantirAcessoDadosAPI.items():
        if valor != 0:
            saida.dicionarioJson['principiosGovernanca'][principio]['regras']['informacoesSobreGarantirAcessoAosDados']['APIs']['tokensPaginaAPI'].append(padronizaString(token))

        #URLs documentação API
    for token in palavrasURLs:
        for link in trending_links:
            if token in link[0].lower() or token in link[1].lower():
                saida.dicionarioJson['principiosGovernanca'][principio]['regras']['informacoesSobreGarantirAcessoAosDados']['APIs']['presencaTokensURLsDoc'] = True
                saida.dicionarioJson['principiosGovernanca'][principio]['regras']['informacoesSobreGarantirAcessoAosDados']['found'] = True

                if padronizaString(token) not in saida.dicionarioJson['principiosGovernanca'][principio]['regras']['informacoesSobreGarantirAcessoAosDados']['APIs']['tokensURLsDoc']:
                    saida.dicionarioJson['principiosGovernanca'][principio]['regras']['informacoesSobreGarantirAcessoAosDados']['APIs']['tokensURLsDoc'].append(padronizaString(token))

    return True


def validaInfIdentificadoresDados(linhaCSV, saida, urls, trending_links, principio):

    #Indicativos de que a URL identifica um conjunto de dados
    for valor in urls.cacheURLsTextosValidaInfIdentificadoresDados.values():
        if valor != 0:
            saida.dicionarioJson['principiosGovernanca'][principio]['regras']['informacoesSobreIdentificadoresDeDados']['presencaDeURLsPersistentes']['indicativosURLsConjDados']['presencaTokensURL'] = True
            break

    for token, valor in urls.cacheURLsTextosValidaInfIdentificadoresDados.items():
        if valor != 0:
            saida.dicionarioJson['principiosGovernanca'][principio]['regras']['informacoesSobreIdentificadoresDeDados']['presencaDeURLsPersistentes']['indicativosURLsConjDados']['tokensURL'].append(padronizaString(token))

    #Extensões
    extensoesDeInteresse = ['csv', 'json', 'xml', 'rdf', 'xlsx', 'xls', 'pdf', 'ods', 'zip', 'dat', 'id', 'ind', 'map', 'tab', 'asp']

    for extensao in extensoesDeInteresse:
        for link in trending_links:
            if extensao in link[0].lower() or extensao in link[1].lower():
                saida.dicionarioJson['principiosGovernanca'][principio]['regras']['informacoesSobreIdentificadoresDeDados']['presencaDeURLsPersistentes']['indicativosURLsConjDados']['presencaFormatosDados'] = True
                break

    for extensao in extensoesDeInteresse:
        for link in trending_links:
            if extensao in link[0].lower() or extensao in link[1].lower():
                if extensao not in saida.dicionarioJson['principiosGovernanca'][principio]['regras']['informacoesSobreIdentificadoresDeDados']['presencaDeURLsPersistentes']['indicativosURLsConjDados']['formatosDados']:
                    saida.dicionarioJson['principiosGovernanca'][principio]['regras']['informacoesSobreIdentificadoresDeDados']['presencaDeURLsPersistentes']['indicativosURLsConjDados']['formatosDados'].append(padronizaString(extensao))

    linksComExtensao = set()
    for extensao in extensoesDeInteresse:
        for link in trending_links:
            if extensao in link[0].lower():
                linksComExtensao.add(link[0])

    listaLinksComExtensao = list(linksComExtensao)

    saida.dicionarioJson['principiosGovernanca'][principio]['regras']['informacoesSobreIdentificadoresDeDados']['presencaDeURLsPersistentes']['indicativosURLsConjDados']['urlsComFormatoDados'] = listaLinksComExtensao

    return True

def validaInfFormatosDados(linhaCSV, saida, principio, infFormatosDados):
    encontrouTokens = False

    for elemento in infFormatosDados.values():
        if elemento != 0:
            saida.dicionarioJson['principiosGovernanca'][principio]['regras']['informacoesSobreFormatosDeDados']['presencaTokens'] = True
            encontrouTokens = True
            break
        
    for token, valor in infFormatosDados.items():
        if valor != 0:
            saida.dicionarioJson['principiosGovernanca'][principio]['regras']['informacoesSobreFormatosDeDados']['tokens'].append(padronizaString(token))

    if encontrouTokens: 
        return True
    else:
        return False

def validaInfPreservacaoDados(linhaCSV, saida, principio, infPreservacaoDados):
    encontrouTokens = False

    for elemento in infPreservacaoDados.values():
        if elemento != 0:
            saida.dicionarioJson['principiosGovernanca'][principio]['regras']['informacoesSobrePreservacaoDosDados']['presencaTokens'] = True
            encontrouTokens = True
            break
        
    for token, valor in infPreservacaoDados.items():
        if valor != 0:
            saida.dicionarioJson['principiosGovernanca'][principio]['regras']['informacoesSobrePreservacaoDosDados']['tokens'].append(padronizaString(token))
            
    if encontrouTokens: 
        return True
    else:
        return False

##################################################################################################################

def verificaPrincGovCompletos(linhaCSV, saida, enderecoPagina, urls, trending_links, emails, dicionarioVocabulariosCount, infMetadados, infLicenca, infProcedenciaDados, infVersionamentoDados, infFeedback, infQualidadePublicacaoDados):
    ###############
    validouInfMetadados = validaInfMetadados(linhaCSV, saida, enderecoPagina, urls, trending_links, 'completos', dicionarioVocabulariosCount, infMetadados)
    validouInfLicenca = validaInfLicenca(linhaCSV, saida, 'completos', dicionarioVocabulariosCount, infLicenca)
    validouInfProcedenciaDados = validaInfProcedenciaDados(linhaCSV, saida, 'completos', dicionarioVocabulariosCount, infProcedenciaDados)
    validouInfQualidadePublicacaoDados = validaInfQualidadePublicacaoDados(linhaCSV, saida, 'completos', dicionarioVocabulariosCount, infQualidadePublicacaoDados)
    validouInfVersionamentoDados = validaInfVersionamentoDados(linhaCSV, saida, 'completos', dicionarioVocabulariosCount, infVersionamentoDados)
    validouInfFeedback = validaInfFeedback(linhaCSV, saida, 'completos', dicionarioVocabulariosCount, infFeedback, emails)   

    if validouInfMetadados:
        linhaCSV['provide_metadata'] = 1
        linhaCSV['provide_descriptive_metadata'] = 1

    if validouInfLicenca:
        linhaCSV['provide_data_license_information'] = 1

    if validouInfProcedenciaDados:
        linhaCSV['provide_data_provenance_information'] = 1

    if validouInfQualidadePublicacaoDados:
        linhaCSV['provide_data_quality_information'] = 1

    if validouInfVersionamentoDados:
        linhaCSV['provide_a_version_indicator'] = 1
        linhaCSV['provide_version_history'] = 1

    if validouInfFeedback: 
        linhaCSV['gather_feedback_from_data_consumers'] = 1
        linhaCSV['make_feedback_available'] = 1


def verificaPrincGovPrimarios(linhaCSV, saida, emails, dicionarioVocabulariosCount, infProcedenciaDados, infFeedback, infQualidadePublicacaoDados):
    validouInfProcedenciaDados = validaInfProcedenciaDados(linhaCSV, saida, 'primarios', dicionarioVocabulariosCount, infProcedenciaDados)
    validouInfQualidadePublicacaoDados = validaInfQualidadePublicacaoDados(linhaCSV, saida, 'primarios', dicionarioVocabulariosCount, infQualidadePublicacaoDados)
    validouInfFeedback = validaInfFeedback(linhaCSV, saida, 'primarios',  dicionarioVocabulariosCount, infFeedback, emails)

def verificaPrincGovAtuais(linhaCSV, saida, urls, trending_links, dicionarioVocabulariosCount, infVersionamentoDados, infGarantirAcessoDadosDownload, infGarantirAcessoDadosAPI):
    validouInfVersionamentoDados = validaInfVersionamentoDados(linhaCSV, saida, 'atuais', dicionarioVocabulariosCount, infVersionamentoDados)
    validouInfGarantirAcessoDados = validaInfGarantirAcessoDados(linhaCSV, saida, urls, trending_links, 'atuais', infGarantirAcessoDadosDownload, infGarantirAcessoDadosAPI)

    if validouInfGarantirAcessoDados:
        linhaCSV['provide_bulk_download'] = 1
        linhaCSV['provide_data_up_to_date'] = 1

def verificaPrincGovFacilidadeAcessoFisicoOuEletronico(linhaCSV, saida, urls, trending_links, infGarantirAcessoDadosDownload, infGarantirAcessoDadosAPI):
    validouInfGarantirAcessoDados = validaInfGarantirAcessoDados(linhaCSV, saida, urls, trending_links, 'facilidadeAcessoFisicoOuEletronico', infGarantirAcessoDadosDownload, infGarantirAcessoDadosAPI)

def verificaPrincGovProcessaveisPorMaquina(linhaCSV, saida, urls, trending_links, infFormatosDados):
    validouInfIdentificadoresDados = validaInfIdentificadoresDados(linhaCSV, saida, urls, trending_links, 'processaveisPorMaquina')
    validouInfFormatosDados = validaInfFormatosDados(linhaCSV, saida, 'processaveisPorMaquina', infFormatosDados)

    if validouInfIdentificadoresDados:
        linhaCSV['use_persistent_URIs_as_identifiers_of_datasets'] = 1

    if validouInfFormatosDados:
        linhaCSV['use_machine_readable_standardized_data_formats'] = 1
        linhaCSV['provide_data_in_multiple_formats'] = 1

def verificaPrincGovNaoDiscriminatorio(linhaCSV, saida, enderecoPagina, urls, trending_links, emails, dicionarioVocabulariosCount, infMetadados, infLicenca, infFeedback, infGarantirAcessoDadosDownload, infGarantirAcessoDadosAPI, infPreservacaoDados):
    validouInfGarantirAcessoDados = validaInfGarantirAcessoDados(linhaCSV, saida, urls, trending_links, 'naoDiscriminatorio', infGarantirAcessoDadosDownload, infGarantirAcessoDadosAPI)
    validouInfPreservacaoDados = (linhaCSV, saida, 'naoDiscriminatorio', infPreservacaoDados)
    validouInfLicenca = validaInfLicenca(linhaCSV, saida, 'naoDiscriminatorio', dicionarioVocabulariosCount, infLicenca)
    #######################
    validouInfMetadados = validaInfMetadados(linhaCSV, saida, enderecoPagina, urls, trending_links, 'naoDiscriminatorio', dicionarioVocabulariosCount, infMetadados)
    validouInfFeedback = validaInfFeedback(linhaCSV, saida, 'naoDiscriminatorio', dicionarioVocabulariosCount, infFeedback, emails)

    if validouInfPreservacaoDados:
        linhaCSV['assess_dataset_coverage'] = 1

def verificaPrincGovFormatosPropriedadeComumOuAberto(linhaCSV, saida, urls, trending_links, infFormatosDados, dicionarioVocabulariosCount, infLicenca, infGarantirAcessoDadosDownload, infGarantirAcessoDadosAPI):
    validouInfFormatosDados = validaInfFormatosDados(linhaCSV, saida, 'formatosDePropriedadeComumOuAberto', infFormatosDados)
    validouInfLicenca = validaInfLicenca(linhaCSV, saida, 'formatosDePropriedadeComumOuAberto', dicionarioVocabulariosCount, infLicenca)
    validouInfGarantirAcessoDados = validaInfGarantirAcessoDados(linhaCSV, saida, urls, trending_links, 'formatosDePropriedadeComumOuAberto', infGarantirAcessoDadosDownload, infGarantirAcessoDadosAPI)

def verificaPrincGovLicencasLivres(linhaCSV, saida, dicionarioVocabulariosCount, infRepublicacaoDados, infLicenca):
    validouInfRepublicacaoDados = validaInfRepublicacaoDados(linhaCSV, saida, 'licencasLivres', dicionarioVocabulariosCount, infRepublicacaoDados)
    validouInfLicenca = validaInfLicenca(linhaCSV, saida, 'licencasLivres', dicionarioVocabulariosCount, infLicenca)

def verificaPrincGovPermanecia(linhaCSV, saida, urls, trending_links, infGarantirAcessoDadosDownload, infGarantirAcessoDadosAPI, dicionarioVocabulariosCount, infRepublicacaoDados, infVersionamentoDados, infPreservacaoDados):
    validouInfIdentificadoresDados = validaInfIdentificadoresDados(linhaCSV, saida, urls, trending_links, 'permanencia')
    validouInfPreservacaoDados = validaInfPreservacaoDados(linhaCSV, saida, 'permanencia', infPreservacaoDados)
    validouInfGarantirAcessoDados = validaInfGarantirAcessoDados(linhaCSV, saida, urls, trending_links, 'permanencia', infGarantirAcessoDadosDownload, infGarantirAcessoDadosAPI)
    validouInfRepublicacaoDados = validaInfRepublicacaoDados(linhaCSV, saida, 'permanencia', dicionarioVocabulariosCount, infRepublicacaoDados)
    validouInfVersionamentoDados = validaInfVersionamentoDados(linhaCSV, saida, 'permanencia', dicionarioVocabulariosCount, infVersionamentoDados)

    if validouInfRepublicacaoDados:
        linhaCSV['provide_feedback_to_the_original_publisher'] = 1
        linhaCSV['cite_the_original_publication'] = 1

def verificaPrincGovCustosDeUtilizacao(linhaCSV, saida, urls, trending_links, emails, infGarantirAcessoDadosDownload, infGarantirAcessoDadosAPI, dicionarioVocabulariosCount, infFeedback):
    validouInfGarantirAcessoDados = validaInfGarantirAcessoDados(linhaCSV, saida, urls, trending_links, 'custosDeUtilizacao', infGarantirAcessoDadosDownload, infGarantirAcessoDadosAPI)
    validouInfFeedback = validaInfFeedback(linhaCSV, saida, 'custosDeUtilizacao', dicionarioVocabulariosCount, infFeedback, emails)

##################################################################################################################

def preencheSaida(saidaCSV, nomeSaida, enderecoPagina, urls, trending_links, dicionarioVocabulariosCount, infMetadados, infLicenca, infProcedenciaDados, infVersionamentoDados, infFeedback, infGarantirAcessoDadosDownload, infGarantirAcessoDadosAPI, infQualidadePublicacaoDados, infFormatosDados, infRepublicacaoDados, infPreservacaoDados, emails):

    caminhoEnderecoPagina = pathlib.Path(enderecoPagina)
    enderecoPaginaCerto = enderecoPagina.replace("\\", "/")
    linhaCSV = {'Site':enderecoPaginaCerto}

    linhaCSV['provide_metadata'] = 0
    linhaCSV['provide_descriptive_metadata'] = 0
    linhaCSV['provide_data_license_information'] = 0
    linhaCSV['provide_data_provenance_information'] = 0
    linhaCSV['provide_data_quality_information'] = 0
    linhaCSV['provide_a_version_indicator'] = 0
    linhaCSV['provide_version_history'] = 0
    linhaCSV['gather_feedback_from_data_consumers'] = 0
    linhaCSV['make_feedback_available'] = 0
    linhaCSV['provide_bulk_download'] = 0
    linhaCSV['provide_data_up_to_date'] = 0
    linhaCSV['use_persistent_URIs_as_identifiers_of_datasets'] = 0
    linhaCSV['use_machine_readable_standardized_data_formats'] = 0
    linhaCSV['provide_data_in_multiple_formats'] = 0
    linhaCSV['assess_dataset_coverage'] = 0
    linhaCSV['provide_feedback_to_the_original_publisher'] = 0
    linhaCSV['cite_the_original_publication'] = 0


    
    saidaJSON = estruturas.formatosSaidas()
    
    saidaJSON.dicionarioJson['urlPaginaPrincipal'] = enderecoPaginaCerto

    data_atual = date.today()
    data_em_texto = data_atual.strftime('%d/%m/%Y')

    saidaJSON.dicionarioJson['dataAvaliacao'] = data_em_texto

    for link in trending_links:
        if link[0] in urls.dicionarioURLsTextos:
            urls.dicionarioURLsTextos[link[0]].append(link[1])
        else:
            urls.dicionarioURLsTextos[link[0]] = [link[1]]

        urls.contaSeInteressante(link[0])

    verificaPrincGovCompletos(linhaCSV, saidaJSON, enderecoPagina, urls, trending_links, emails, dicionarioVocabulariosCount, infMetadados, infLicenca, infProcedenciaDados, infVersionamentoDados, infFeedback, infQualidadePublicacaoDados)
    verificaPrincGovPrimarios(linhaCSV, saidaJSON, emails, dicionarioVocabulariosCount, infProcedenciaDados, infFeedback, infQualidadePublicacaoDados)
    verificaPrincGovAtuais(linhaCSV, saidaJSON, urls, trending_links, dicionarioVocabulariosCount, infVersionamentoDados, infGarantirAcessoDadosDownload, infGarantirAcessoDadosAPI)
    verificaPrincGovFacilidadeAcessoFisicoOuEletronico(linhaCSV, saidaJSON, urls, trending_links, infGarantirAcessoDadosDownload, infGarantirAcessoDadosAPI)
    verificaPrincGovProcessaveisPorMaquina(linhaCSV, saidaJSON, urls, trending_links, infFormatosDados)
    verificaPrincGovNaoDiscriminatorio(linhaCSV, saidaJSON, enderecoPagina, urls, trending_links, emails, dicionarioVocabulariosCount, infMetadados, infLicenca, infFeedback, infGarantirAcessoDadosDownload, infGarantirAcessoDadosAPI, infPreservacaoDados)
    verificaPrincGovFormatosPropriedadeComumOuAberto(linhaCSV, saidaJSON, urls, trending_links, infFormatosDados, dicionarioVocabulariosCount, infLicenca, infGarantirAcessoDadosDownload, infGarantirAcessoDadosAPI)
    verificaPrincGovLicencasLivres(linhaCSV, saidaJSON, dicionarioVocabulariosCount, infRepublicacaoDados, infLicenca)
    verificaPrincGovPermanecia(linhaCSV, saidaJSON, urls, trending_links, infGarantirAcessoDadosDownload, infGarantirAcessoDadosAPI, dicionarioVocabulariosCount, infRepublicacaoDados, infVersionamentoDados, infPreservacaoDados)
    verificaPrincGovCustosDeUtilizacao(linhaCSV, saidaJSON, urls, trending_links, emails, infGarantirAcessoDadosDownload, infGarantirAcessoDadosAPI, dicionarioVocabulariosCount, infFeedback)

    json_object = json.dumps(saidaJSON.dicionarioJson, indent = 4)

    with open("./saidas/"+nomeSaida, "w") as outfile:
        outfile.write(json_object)

    saidaCSV.writerow(linhaCSV)
    
def splitText(htmlText):
    textList = [line for line in str(htmlText).replace("\t"," ").replace(",", " ").split("\r\n") if line != ""]
    textList = splitTextListWith("\n", textList)
    textList = splitTextListWith(" - ", textList)
    textList = splitTextListWith("- ", textList)
    textList = splitTextListWith(" -", textList)
    textList = splitTextListWith(" ", textList)

    return textList

def splitTextListWith(sep, textList):
    result = []
    for line in textList:
        lineSplited = line.split(sep)
        #Remove possíveis elementos nulos
        for split in lineSplited:
            if(split.strip(" \n\t\r\v") != ""):
                result.append(split.strip(" \n\t\r\v"))

    return result