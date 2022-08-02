import json
from . import auxiliares

class formatosSaidas():
    def __init__(self):
        self.dicionarioJson = {
            "urlPaginaPrincipal":"",
            "dataAvaliacao":"",
            "principiosGovernanca": { #dictPrincGovernanca
                "completos": { #dictRegras
                    "regras": {
                        "informacoesSobreMetadados": {
                            "found": False,
                            "presencaTokens": False,
                            "tokens": [],
                            "presencaURLsArquivosMetadadosAnexos": False,
                            "URLsArquivosMetadadosAnexos": []
                        },  
                        "informacoesSobreLicenca": {
                            "presencaTokens": False,
                            "tokens": []
                        },      
                        "informacoesSobreProcedenciaDados": {
                            "presencaTokens": False,
                            "tokens": []
                        },      
                        "informacoesSobreQualidadeDados": {
                            "presencaTokens": False,
                            "tokens": []
                        },      
                        "informacoesSobreVersionamentoDados": {
                            "presencaTokens": False,
                            "tokens": []
                        },      
                        "informacoesSobreFeedback": {
                            "presencaTokens": False,
                            "tokens": [],
                            "emails": []
                        } 
                    }
                },
                "primarios": {
                    "regras": {
                        "informacoesSobreProcedenciaDados": {
                            "presencaTokens": False,
                            "tokens": []
                        },      
                        "informacoesSobreQualidadeDados": {
                            "presencaTokens": False,
                            "tokens": []
                        },         
                        "informacoesSobreFeedback": {
                            "presencaTokens": False,
                            "tokens": [],
                            "emails": []
                        }           
                    }
                },
                "atuais": {
                    "regras": {
                        "informacoesSobreVersionamentoDados": {
                            "presencaTokens": False,
                            "tokens": []
                        },
                        "informacoesSobreGarantirAcessoAosDados": { #dictInf
                            "found": False,
                            "download": { #dictDownload
                                "extensoesUrlsVolumeDados": False,
                                "urlsVolumeDados": [],
                                "presencaTokensUrlsDadosAtualizados": False,
                                "tokensUrlsDadosAtualizados":[]  
                            },
                            "APIs": { #dictAPIs
                                "presencaTokensPaginaAPI": False,
                                "tokensPaginaAPI": [], #Entendi que são na página como um todo e não URLs
                                "URLsDadosIndisponiveis": False,
                                "presencaTokensURLsDoc": False,
                                "tokensURLsDoc": []
                            }   
                        }
                    }
                },
                "facilidadeAcessoFisicoOuEletronico": {
                    "regras": {
                        "informacoesSobreGarantirAcessoAosDados": { #dictInf
                            "found": False,
                            "download": { #dictDownload
                                "extensoesUrlsVolumeDados": False,
                                "urlsVolumeDados": [],
                                "presencaTokensUrlsDadosAtualizados": False,
                                "tokensUrlsDadosAtualizados":[]  
                            },
                            "APIs": { #dictAPIs
                                "presencaTokensPaginaAPI": False,
                                "tokensPaginaAPI": [], #Entendi que são na página como um todo e não URLs
                                "URLsDadosIndisponiveis": False,
                                "presencaTokensURLsDoc": False,
                                "tokensURLsDoc": []
                            }   
                        }
                    }
                },
                "processaveisPorMaquina": {
                    "regras": {
                        "informacoesSobreIdentificadoresDeDados": {
                            "presencaDeURLsPersistentes": {
                                "URLsSubdominiosAdmSeparadosPrincipal": True,
                                "indicativosURLsConjDados": {
                                    "presencaTokensURL": False,
                                    "tokensURL": [],
                                    "presencaFormatosDados": False,
                                    "formatosDados": [],
                                    "urlsComFormatoDados": []
                                    #"datasDados": false,
                                    #"versaoDados": false
                                }
                            }
                        },
                        "informacoesSobreFormatosDeDados": {
                            "presencaTokens": False,
                            "tokens": []
                        }
                    }
                }, 
                "naoDiscriminatorio": {
                    "regras": {
                        "informacoesSobreGarantirAcessoAosDados": { #dictInf
                            "found": False,
                            "download": { #dictDownload
                                "extensoesUrlsVolumeDados": False,
                                "urlsVolumeDados": [],
                                "presencaTokensUrlsDadosAtualizados": False,
                                "tokensUrlsDadosAtualizados":[]  
                            },
                            "APIs": { #dictAPIs
                                "presencaTokensPaginaAPI": False,
                                "tokensPaginaAPI": [], #Entendi que são na página como um todo e não URLs
                                "URLsDadosIndisponiveis": False,
                                "presencaTokensURLsDoc": False,
                                "tokensURLsDoc": []
                            }   
                        },
                        "informacoesSobrePreservacaoDosDados": {
                            "referenciamentoURL": False, #URLs com código resposta 410 ou 303 ; URL e código
                            "presencaTokens": False,
                            "tokens": []
                        },
                        "informacoesSobreLicenca": {
                            "presencaTokens": False,
                            "tokens": []
                        },
                        "informacoesSobreMetadados": {
                            "presencaTokens": False,
                            "tokens": [],
                            "presencaURLsArquivosMetadadosAnexos": False,
                            "URLsArquivosMetadadosAnexos": []
                        }, 
                        "informacoesSobreFeedback": {
                            "presencaTokens": False,
                            "tokens": [],
                            "emails": []
                        }
                    }
                }, 
                "formatosDePropriedadeComumOuAberto": {
                    "regras": {
                        "informacoesSobreFormatosDeDados": {
                            "presencaTokens": False,
                            "tokens": []
                        },
                        "informacoesSobreLicenca": {
                            "presencaTokens": False,
                            "tokens": []
                        },
                        "informacoesSobreGarantirAcessoAosDados": { #dictInf
                            "found": False,
                            "download": { #dictDownload
                                "extensoesUrlsVolumeDados": False,
                                "urlsVolumeDados": [],
                                "presencaTokensUrlsDadosAtualizados": False,
                                "tokensUrlsDadosAtualizados":[]  
                            },
                            "APIs": { #dictAPIs
                                "presencaTokensPaginaAPI": False,
                                "tokensPaginaAPI": [], #Entendi que são na página como um todo e não URLs
                                "URLsDadosIndisponiveis": False,
                                "presencaTokensURLsDoc": False,
                                "tokensURLsDoc": []
                            }   
                        }  
                    }
                }, 
                "licencasLivres": {
                    "regras": {
                        "informacoesSobreRepublicacaoDosDados": {
                            "presencaTokens": False,
                            "tokens": []
                        },
                        "informacoesSobreLicenca": {
                            "presencaTokens": False,
                            "tokens": []
                        }                        
                    }
                }, 
                "permanencia": {
                    "regras": {#dictRegras
                        "informacoesSobreIdentificadoresDeDados": {
                            "presencaDeURLsPersistentes": {
                                "URLsSubdominiosAdmSeparadosPrincipal": True,
                                "indicativosURLsConjDados": {
                                    "presencaTokensURL": False,
                                    "tokensURL": [], #/dataset etc
                                    "presencaFormatosDados": False,
                                    "formatosDados": [], #extensoes
                                    "urlsComFormatoDados": []
                                    #"datasDados": false, #URL e a data
                                    #"versaoDados": false #URL e a versao
                                }
                            }
                        },
                        "informacoesSobrePreservacaoDosDados": {
                            "referenciamentoURL": False,#URLs com código resposta 410 ou 303 ; URL e código
                            "presencaTokens": False,
                            "tokens": []
                        },
                        "informacoesSobreGarantirAcessoAosDados": { #dictInf
                            "found": False,
                            "download": { #dictDownload
                                "extensoesUrlsVolumeDados": False,
                                "urlsVolumeDados": [],
                                "presencaTokensUrlsDadosAtualizados": False,
                                "tokensUrlsDadosAtualizados":[]  
                            },
                            "APIs": { #dictAPIs
                                "presencaTokensPaginaAPI": False,
                                "tokensPaginaAPI": [], #Entendi que são na página como um todo e não URLs
                                "URLsDadosIndisponiveis": False,
                                "presencaTokensURLsDoc": False,
                                "tokensURLsDoc": []
                            }   
                        },
                        "informacoesSobreRepublicacaoDosDados": {
                            "presencaTokens": False,
                            "tokens": []
                        },
                        "informacoesSobreVersionamentoDados": {
                            "presencaTokens": False,
                            "tokens": []
                        }
                    } 
                }, 
                "custosDeUtilizacao": { 
                    "regras": {#dictRegras
                        "informacoesSobreGarantirAcessoAosDados": { #dictInf
                            "found": False,
                            "download": { #dictDownload
                                "extensoesUrlsVolumeDados": False,
                                "urlsVolumeDados": [],
                                "presencaTokensUrlsDadosAtualizados": False,
                                "tokensUrlsDadosAtualizados":[]  
                            },
                            "APIs": { #dictAPIs
                                "presencaTokensPaginaAPI": False,
                                "tokensPaginaAPI": [], #Entendi que são na página como um todo e não URLs
                                "URLsDadosIndisponiveis": False,
                                "presencaTokensURLsDoc": False,
                                "tokensURLsDoc": []
                            }   
                        },
                        "informacoesSobreFeedback": {
                            "presencaTokens": False,
                            "tokens": [],
                            "emails": []
                        }
                    } 
                } 
            }
        }

class TermosDeInteresse():
    def __init__(self, enderecoPagina, listaPalavrasPortal): #Como maiúsculas fazem diferença, aplicar uma função nas palavras da página como .lower()
        
        self.URLPagina = enderecoPagina
        self.listaPalavrasPortal = listaPalavrasPortal

        self.cacheTokens = {'metadados':[], 'informações':[], 'adicionais':[], 'dicionário':[], 'dicionários':[], 
        'dados':[], 'taxonomia':[], 'critério':[], 'critérios':[], 'descrição':[], 'conjunto':[], 
        'título':[], 'URI':[], 'palavra':[], 'palavras':[], 'chave':[], 'data':[], 'publicação':[], 'criação':[], 
        'frequência':[], 'atualização':[], 'contato':[], 'granularidade':[], 
        'referência':[], 'referências':[], 'responsável':[], 'responsáveis':[], 'idioma':[], 'fonte':[], 'fontes':[], 'versão':[],
        'mantenedor':[], 'mantenedores':[], 'tema':[], 'formato':[], 'metadado':[], 'estrutural':[], 
        'estruturais':[], 'campo':[], 'campos':[], 'tipo':[], 'métrica':[], 'última':[], 'modificação':[],
        'descrição':[], 'cobertura':[], 'geográfica':[], 'temporal':[], 'escopo':[], 'geopolítico':[], 'autor':[], 'autores':[], 
        'criado':[], 'entidade':[], 'ponto':[], 'período':[],
        'temas':[], 'categorias':[], 'formatos':[], 'mídia':[], 'licença':[], 'identificador':[], 'relação':[], 
        'conteúdo':[], 'recursos':[], 'termos':[], 'restrições':[], 'restrição':[], 'criador':[], 'criadores':[], 'área':[],
        'editor':[], 'editora':[], 'editores':[], 'editoras':[], 'qualidade':[], 'integridade':[], 'disponibilidade':[],
        'atual':[], 'histórico':[], 'obsoleto':[], 'mudanças':[], 'modificações':[], 'últimas':[], 'periodicidade':[],
        'feedback':[], 'formulário':[], 'rank':[], 'ranqueamento':[], 'esperado':[], 
        'avaliação':[], 'avaliações':[], 'botão':[], 'botões':[], 'comentário':[],
        'questionamento':[], 'classifica':[], 'classificação':[], 'correção':[], 'revisão':[], 'compartilhar':[], 'compartilhe':[],
        'informe':[], 'fale':[], 'entre':[], 'sugestões':[], 'original':[], 'procedência':[], 'citação':[], 'publicador':[],
        #Outros
        'atualizado':[], 'validade':[],
        'API':[], 'documentação':[], 'manual':[], 
        'parâmetros':[], 'especificação':[], 'webservice':[], 'REST':[], 'RESTful':[], 'consumo':[], 'retorno':[], 
        'resultados':[], 'método':[], 'GET':[], 'URL':[], 'URI':[], 'cabeçalhos':[], 'headers':[], 'csv':[], 
        'xml':[], 'json':[], 'rdf':[], 'linguagem':[], 'padrão':[], 'exportar':[], 'explorar':[], 'estruturados':[],
        'estrutura':[], 'escolher':[], 'manutenção':[], 'breve':[], 'arquivado':[], 'arquivamento':[], 'cópia':[],
        'substituição':[], 'substituído':[], 'removido':[], 'remoção':[], 'tempo':[], 'adotado':[]}

        ##### VOCABULÁRIOS DE TERMOS #####

        self.infMetadados = {'metadados':0, 'informações adicionais':0, 'dicionário':0, 'dicionários':0, 
        'dicionário dados':0, 'taxonomia':0, 'critério':0, 'critérios':0, 'descrição conjunto dados':0, 
        'título':0, 'URI':0, 'palavra chave':0, 'palavras chave':0, 'data publicação':0, 'data criação':0, 
        'criação':0, 'frequência':0, 'atualização':0, 'data atualização':0, 'contato':0, 'granularidade':0, 
        'referência':0, 'referências':0, 'responsável':0, 'responsáveis':0, 'idioma':0, 'fonte':0, 'fontes':0, 'versão':0,
        'mantenedor':0, 'mantenedores':0, 'tema':0, 'formato data':0, 'metadado estrutural':0, 'metadados estruturais':0, 
        'campo':0, 'campos':0, 'tipo dados':0, 'métrica':0, 'última modificação':0, 'última atualização':0,
        'descrição':0, 'cobertura geográfica':0, 'cobertura temporal':0, 'escopo geopolítico':0, 'autor':0, 'autores':0, 
        'criado':0, 'entidade responsável':0, 'ponto contato':0, 'período temporal':0, 'data última modificação':0, 
        'temas':0, 'categorias':0, 'formato':0, 'formato mídia':0, 'licença':0, 'identificador':0, 'relação':0, 
        'tipo conteúdo':0, 'recursos':0}

        self.infLicenca = {'licença':0, 'tipo licença':0, 'termos licença':0, 
        'restrições':0, 'restrição':0}

        self.infProcedenciaDados = {'fonte':0, 'fontes':0, 'criador':0, 'criadores':0, 'responsável':0, 'responsáveis':0,
        'área responsável':0, 'mantenedor':0, 'mantenedores':0, 'autor':0, 'autores':0, 'data publicação':0, 'editor':0,
        'editores':0, 'editoras':0}

        #sugestão de ter uma forma de testar a disponibilidade dos dados - link disponível e com código HTTP que garanta 
        # essa disponibilidade
        self.infQualidadePublicacaoDados = {'qualidade dados':0, 'qualidade':0, 'integridade':0, 
        'integridade dados':0, 'métrica':0, 'disponibilidade':0, 'disponibilidade dados':0}

        self.infVersionamentoDados = {'versão':0, 'versão atual':0, 'atualização':0, 'última atualização':0, 'data':0, 
        'data criação':0, 'última versão':0, 'histórico':0, 'obsoleto':0, 'frequência':0, 'frequência atualização':0, 
        'histórico mudanças':0, 'histórico modificações':0, 'histórico modificação':0, 'última modificação':0,
        'últimas modificações':0, 'periodicidade':0}

        self.infFeedback = {'contato':0, 'feedback':0, 'formulário':0, 'rank':0, 'ranqueamento':0, 'esperado':0, 
        'avaliação':0, 'avaliações':0, 'botão':0, 'botões':0, 'qualidade dados':0, 'qualidade':0, 'comentário':0,
        'questionamento':0, 'classifica':0, 'classificação':0, 'correção':0, 'revisão':0, 'compartilhar':0, 'compartilhe':0,
        'informe':0, 'fale':0, 'entre':0, 'sugestões':0}

        self.infRepublicacaoDados = {'fonte original':0, 'procedência':0, 'citação':0, 'publicação original':0, 'licença':0,
        'publicador':0}

        self.infGarantirAcessoDadosDownload = {'data':0, 'atualização':0, 'última':0, 'frequência':0, 'criado':0, 
        'criação':0, 'atualizado':0, 'cobertura':0, 'temporal':0, 'validade':0}
        self.infGarantirAcessoDadosAPI = {'API':0, 'documentação':0, 'documentação API':0, 'manual':0, 'descrição':0, 
        'parâmetros':0, 'especificação':0, 'webservice':0, 'REST':0, 'RESTful':0, 'consumo':0, 'retorno':0, 
        'resultados':0, 'método':0, 'GET':0, 'URL':0, 'URI':0, 'cabeçalhos':0, 'headers':0}

        self.infFormatosDados = {'formato':0, 'formatos':0, 'csv':0, 'xml':0, 'json':0, 'rdf':0, 'linguagem':0, 
        'formato data':0, 'formato tempo':0, 'padrão data':0, 'padrão tempo':0, 'padrão':0, 'padrão adotado':0,
        'exportar':0, 'explorar':0, 'dados':0, 'estruturados':0, 'estrutura':0, 'formato':0, 'escolher':0}

        self.infPreservacaoDados = {'manutenção':0, 'breve':0, 'arquivado':0, 'arquivamento':0, 'cópia':0,
        'substituição':0, 'substituído':0, 'removido':0, 'remoção':0}

        self.dicionarioVocabularios = {'infMetadados':self.infMetadados, 'infLicenca':self.infLicenca, 
        'infProcedenciaDados':self.infProcedenciaDados, 'infQualidadePublicacaoDados':self.infQualidadePublicacaoDados,
        'infVersionamentoDados':self.infVersionamentoDados, 'infFeedback':self.infFeedback, 
        'infRepublicacaoDados':self.infRepublicacaoDados, 'infGarantirAcessoDadosDownload':self.infGarantirAcessoDadosDownload,
        'infGarantirAcessoDadosAPI':self.infGarantirAcessoDadosAPI, 'infFormatosDados':self.infFormatosDados,
        'infPreservacaoDados':self.infPreservacaoDados}
        self.dicionarioVocabulariosCount = {'infMetadados':0, 'infLicenca':0, 
        'infProcedenciaDados':0, 'infQualidadePublicacaoDados':0,
        'infVersionamentoDados':0, 'infFeedback':0, 
        'infRepublicacaoDados':0, 'infGarantirAcessoDadosDownload':0, 'infGarantirAcessoDadosAPI':0, 'infFormatosDados':0,
        'infPreservacaoDados':0}

        #---------------------------------------------------------------------------

        ##### VOCABULÁRIOS DE TERMOS ASSOCIADOS A CADA PRINCÍPIO DE GOVERNANÇA #####
        #Acho que não precisaria ter todos os repetidos... Bastaria consultar um dicionário só com feedback por exemplo e coloca 
        # 1 em todos que usavam o feedback

        self.princGovernCompletos = {'infMetadados':0, 'infLicenca':0, 
        'infProcedenciaDados':0, 'infQualidadePublicacaoDados':0,
        'infVersionamentoDados':0, 'infFeedback':0}

        self.princGovernPrimarios = {'infProcedenciaDados':0, 
        'infQualidadePublicacaoDados':0, 'infFeedback':0}

        self.princGovernAtuais = {'infVersionamentoDados':0, 'infGarantirAcessoDadosDownload':0, 'infGarantirAcessoDadosAPI':0}

        self.princGovernFacilidadeAcessoFisicoEletrônico = {'infGarantirAcessoDadosDownload':0, 'infGarantirAcessoDadosAPI':0}

        #VERIFICAR CADA UM
        self.princGovernProcessaveisPorMaquina = {'infFormatosDados':0}

        self.princGovernNaoDiscriminatorio = {'infGarantirAcessoDadosDownload':0, 'infGarantirAcessoDadosAPI':0, 
        'infLicenca':0, 'infMetadados':0, 'infFeedback':0, 'infPreservacaoDados':0}

        self.princGovernFormatosDePropriedadeComumOuAberto = {'infLicenca':0, 'infFormatosDados':0, 'infGarantirAcessoDadosDownload':0, 'infGarantirAcessoDadosAPI':0}

        self.princGovernLicencasLivres = {'infRepublicacaoDados':0, 'infLicenca':0}

        self.princGovernPermanencia = {'infVersionamentoDados':0, 'infRepublicacaoDados':0, 
        'infGarantirAcessoDadosDownload':0, 'infGarantirAcessoDadosAPI':0, 'infPreservacaoDados':0}

        self.princGovernCustosUtilizacao = {'infGarantirAcessoDadosDownload':0, 'infGarantirAcessoDadosAPI':0, 'infFeedback':0}

        self.dicionarioPrincGovern = {'princGovernCompletos':self.princGovernCompletos, 'princGovernPrimarios':self.princGovernPrimarios,
        'princGovernAtuais':self.princGovernAtuais, 'princGovernFacilidadeAcessoFisicoEletrônico':self.princGovernFacilidadeAcessoFisicoEletrônico, 
        'princGovernProcessaveisPorMaquina':self.princGovernProcessaveisPorMaquina, 'princGovernNaoDiscriminatorio':self.princGovernNaoDiscriminatorio, 
        'princGovernFormatosDePropriedadeComumOuAberto':self.princGovernFormatosDePropriedadeComumOuAberto, 
        'princGovernLicencasLivres':self.princGovernLicencasLivres, 'princGovernPermanencia':self.princGovernPermanencia, 
        'princGovernCustosUtilizacao':self.princGovernCustosUtilizacao}

        self.dicionarioPrincGovernCount = {'princGovernCompletos':0, 'princGovernPrimarios':0,
        'princGovernAtuais':0, 'princGovernFacilidadeAcessoFisicoEletrônico':0, 
        'princGovernProcessaveisPorMaquina':0, 'princGovernNaoDiscriminatorio':0, 
        'princGovernFormatosDePropriedadeComumOuAberto':0, 
        'princGovernLicencasLivres':0, 'princGovernPermanencia':0, 
        'princGovernCustosUtilizacao':0}

        ##### PRINCÍPIOS DE GOVERNANÇA ATENDIDOS #####

        self.princGovernAtendidos = {'princGovernCompletos':0, 'princGovernPrimarios':0,
        'princGovernAtuais':0, 'princGovernFacilidadeAcessoFisicoEletrônico':0, 
        'princGovernProcessaveisPorMaquina':0, 'princGovernNaoDiscriminatorio':0, 
        'princGovernFormatosDePropriedadeComumOuAberto':0, 
        'princGovernLicencasLivres':0, 'princGovernPermanencia':0, 
        'princGovernCustosUtilizacao':0}

##################################################################################################################

    def determinaPrincGovAtendidos(self, saidaCSV, nomeSaida, enderecoPagina, urls, trending_links, emails):
        auxiliares.encontraTermoATermoCache(self.listaPalavrasPortal, self.cacheTokens)

        auxiliares.encontraTermosVocabularios(
            self.dicionarioVocabularios, self.cacheTokens, self.dicionarioVocabulariosCount)

        auxiliares.encontraVocabulariosDosPrincGov(
            self.dicionarioPrincGovern, self.dicionarioVocabulariosCount, self.dicionarioPrincGovernCount)
            
        auxiliares.encontraPrincGovAtendidos(self.dicionarioPrincGovernCount, self.princGovernAtendidos)
        #################
        auxiliares.preencheSaida(saidaCSV, nomeSaida, enderecoPagina, urls, trending_links, self.dicionarioVocabulariosCount, 
                                    self.infMetadados, self.infLicenca, self.infProcedenciaDados, self.infVersionamentoDados,
                                    self.infFeedback, self.infGarantirAcessoDadosDownload, self.infGarantirAcessoDadosAPI,
                                    self.infQualidadePublicacaoDados, self.infFormatosDados, self.infRepublicacaoDados,
                                    self.infPreservacaoDados, emails)

class URLsDeInteresse():
    def __init__(self):
        self.dicionarioURLsTextos = dict()

        self.cacheURLsTextos = {'dados abertos':0, 'biblioteca':0, 'base':0, 'base dados':0,
                                'base de dados':0, 'metadados':0, 'informacoes adicionais':0, 'dicionario':0, 'dicionarios':0, 
                                'dicionario dados':0, 'dicionario de dados':0, 'taxonomia':0, 'descricao conjunto dados':0,
                                'descricao do conjunto de dados':0, 'descricao conjunto de dados':0, 'atualizacao':0, 'atualizacoes':0, 
                                'referencia':0, 'referencias':0, 'fonte':0, 'fontes':0, 'versao':0, 'formato data':0, 'metadado estrutural':0,
                                'metadados estruturais':0, 'tipo dados':0, 'descricao':0, 'temas':0, 'categorias':0, 'formato':0, 
                                'formato midia':0, 'licenca':0, 'relacao':0, 'tipo conteudo':0, 'recursos':0, '.csv':0, '.json':0, '.xml':0,
                                '.rdf':0, '.xlsx':0, '.pdf':0, '.xls':0, 'resource':0, '.ods':0, '.zip':0, '.dat':0, '.id':0, '.ind':0, '.map':0, '.tab':0, '.asp':0}

        self.cacheURLsTextosValidaInfIdentificadoresDados = {'dataset':0, 'dados abertos':0, 'dados':0,
                                                             'conjunto de dados':0, 'conjunto dados':0,
                                                             '.csv':0, '.json':0, '.xml':0, '.rdf':0,
                                                             '.xlsx':0, '.pdf':0, '.ods':0, '.zip':0, 
                                                             '.dat':0, '.id':0, '.ind':0, '.map':0, 
                                                             '.tab':0, '.asp':0}

        self.variacoesURLsTextos = dict()

        self.palavrasInteressantesLinks = dict()

        self.variacoesURLsTextosValidaInfIdentificadoresDados = dict()

        for texto in self.cacheURLsTextos.keys():
            variacoes = self.possiveisVariacoesTexto(texto)
            self.variacoesURLsTextos[texto] = variacoes

        for texto in self.cacheURLsTextosValidaInfIdentificadoresDados.keys():
            variacoes = self.possiveisVariacoesTexto(texto)
            self.variacoesURLsTextosValidaInfIdentificadoresDados[texto] = variacoes            

    def contaSeInteressante(self, textoUrl):
        diretorios = "/".join(textoUrl.split("/")[3:]).lower()

        for chave, listaVariacoes in self.variacoesURLsTextos.items():
            for variacao in listaVariacoes:
                if variacao in diretorios:
                    self.cacheURLsTextos[chave] += 1
                    if variacao not in list(self.palavrasInteressantesLinks.keys()):
                        self.palavrasInteressantesLinks[variacao] = [textoUrl]
                    else:
                        self.palavrasInteressantesLinks[variacao].append(textoUrl)

        for chave, listaVariacoes in self.variacoesURLsTextosValidaInfIdentificadoresDados.items():
            for variacao in listaVariacoes:
                if variacao in diretorios:
                    self.cacheURLsTextosValidaInfIdentificadoresDados[chave] += 1
                    break

    def possiveisVariacoesTexto(self, texto):
        splitTexto = texto.lower().split()

        variacoes = [texto.lower()]

        if len(splitTexto) > 1:
            variacoes.append("_".join(splitTexto))
            variacoes.append("-".join(splitTexto))
            variacoes.append("".join(splitTexto)) #lembrar de comparar com .lower()

        return variacoes